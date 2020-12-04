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

import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def colorbar(im, ax, pad=0.01):
    """Add colorbar to ax corresponding to im.

    Parameters
    ----------
    im : to fill
        to fill.

    ax : matplotlib.pyplot.subplotsaxes
        Axis of plot.

    pad : float, optional


    Returns
    -------
    cax : coloraxis

    """
    pos = ax.get_position()
    fig = plt.gcf()
    cax = fig.add_axes([pos.x0 + pos.width + pad, pos.y0, pad, pos.height])
    fig.colorbar(im, cax)

    return cax
