# MIT License
#
# Copyright (c) 2020 Louis Richard
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so.

import xarray as xr

from astropy import constants

from .avg_4sc import avg_4sc
from .c_4_grad import c_4_grad
from .cross import cross


def c_4_j(r_list=None, b_list=None):
    """Calculate current density :math:`\\mathbf{J}` from using 4 spacecraft technique [4]_, the
    divergence of the magnetic field :math:`\\nabla . \\mathbf{B}`, magnetic field at the center
    of mass of the tetrahedron, :math:`\\mathbf{J}\\times\\mathbf{B}` force, part of the
    divergence of stress associated with curvature :math:`\\nabla.\\mathbf{T}_{shear}` and
    gradient of the magnetic pressure :math:`\\nabla P_b`. Where :

    .. math::

        \\mathbf{J} = \\frac{\\nabla \\times \\mathbf{B}}{\\mu_0}

        \\mathbf{J}\\times\\mathbf{B} = \\nabla.\\mathbf{T}_{shear} + \\nabla P_b

        \\nabla.\\mathbf{T}_{shear} = \\frac{(\\mathbf{B}.\\nabla) \\mathbf{B}}{\\mu_0}

        \\nabla P_b = \\nabla \\frac{B^2}{2\\mu_0}

    The divergence of the magnetic field is current density units as it shows the error on the
    estimation of the current density [5]_ .

    Parameters
    ----------
    r_list : list of xarray.DataArray
        Time series of the spacecraft position [km].

    b_list : list of xarray.DataArray
        Time series of the magnetic field [nT].

    Returns
    -------
    j : xarray.DataArray
        Time series of the current density [A.m^{-2}].

    div_b : xarray.DataArray
        Time series of the divergence of the magnetic field [A.m^{-2}].

    b_avg : xarray.DataArray
        Time series of the magnetic field at the center of mass of the tetrahedron,
        sampled at 1st SC time steps [nT].

    jxb : xarray.DataArray
        Time series of the :math:`\\mathbf{J}\\times\\mathbf{B}` force [T.A].

    div_t_shear : xarray.DataArray
        Time series of the part of the divergence of stress associated with curvature units
        [T A/m^2].

    div_pb : xarray.DataArray
        Time series of the gradient of the magnetic pressure.

    See also
    --------
    pyrfu.pyrf.c_4_k : Calculates reciprocal vectors in barycentric coordinates.
    pyrfu.pyrf.c_4_grad : Calculate gradient of physical field using 4 spacecraft technique.

    References
    ----------
    .. [4]	Dunlop, M. W., A. Balogh, K.-H. Glassmeier, and P. Robert (2002a), Four-point Cluster
            application of magnetic field analysis tools: The Curl- ometer, J. Geophys. Res.,
            107(A11), 1384, doi : https://doi.org/10.1029/2001JA005088.

    .. [5]	Robert, P., et al. (1998), Accuracy of current determination, in Analysis Methods for
            Multi-Spacecraft Data, edited by G. Paschmann and P. W. Daly, pp. 395–418, Int. Space S
            ci. Inst., Bern. url : http://www.issibern.ch/forads/sr-001-16.pdf

    Examples
    --------
    >>> import numpy as np
    >>> from pyrfu import mms, pyrf
    >>> # Time interval
    >>> tint = ["2019-09-14T07:54:00.000", "2019-09-14T08:11:00.000"]
    >>> # Spacecraft indices
    >>> mms_list = np.arange(1,5)
    >>> # Load magnetic field and spacecraft position
    >>> b_mms = [mms.get_data("B_gse_fgm_srvy_l2", tint, mms_id) for mms_id in mms_list]
    >>> r_mms = [mms.get_data("R_gse", tint, mms_id) for mms_id in mms_list]
    >>> j, divB, B, jxB, divTshear, divPb = pyrf.c_4_j(r_mms, b_mms)

    """
    assert r_list is not None and isinstance(r_list, list) and len(r_list) == 4
    assert b_list is not None and isinstance(b_list, list) and len(b_list) == 4

    for i in range(4):
        if not isinstance(r_list[i], xr.DataArray):
            raise TypeError("Spacecraft position must be DataArray")

        if not isinstance(b_list[i], xr.DataArray):
            raise TypeError("Magnetic field must be DataArray")

    mu0 = constants.mu0.value

    b_avg = avg_4sc(b_list)

    # Estimate divB/mu0. unit is A/m2
    div_b = c_4_grad(r_list, b_list, "div")

    # to get right units
    div_b *= 1.0e-3 * 1e-9 / mu0

    # estimate current j [A/m2]
    curl_b = c_4_grad(r_list, b_list, "curl")

    # to get right units [A.m^{-2}]
    j = curl_b * 1.0e-3 * 1e-9 / mu0

    # estimate jxB force [T A/m2]
    jxb = 1e-9 * cross(j, b_avg)

    # estimate divTshear = (1/muo) (B*div)B [T A/m2]
    b_div_b = c_4_grad(r_list, b_list, "bdivb")

    # to get right units [T.A.m^{-2}]
    div_t_shear = b_div_b * 1.0e-3 * 1e-9 * 1e-9 / mu0

    # estimate divPb = (1/muo) grad (B^2/2) = divTshear-jxB
    div_pb = div_t_shear - jxb

    return j, div_b, b_avg, jxb, div_t_shear, div_pb
