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

import numpy as np
import xarray as xr


def calc_dt(inp=None):
    """Computes time step of the input time series.

    Parameters
    ----------
    inp : xarray.DataArray
        Time series of the input variable.

    Returns
    -------
    out : float
        Time step in seconds.

    """

    if inp is None:
        raise ValueError("calc_dt requires at least one argument")

    if not isinstance(inp, xr.DataArray):
        raise TypeError("Input must be a DataArray")

    out = np.median(np.diff(inp.time.data)).astype(float) * 1e-9

    return out
