#!/usr/bin/env python

import agate
from matplotlib import pyplot

from fever.base import Chart

class Scatter(Chart):
    """
    Plots a scatter plot.

    :param x_column_name: Column containing X values for the points to plot.
        Must refer to a :class:`agate.NumberColumn`.
    :param y_column_name: Column containing Y values for the points to plot.
        Must refer to a :class:`agate.NumberColumn`.
    """
    def __init__(self, x_column_name, y_column_name):
        self._x_column_name = x_column_name
        self._y_column_name = y_column_name

    def _show_legend(self):
        return False

    def _plot(self, table):
        x_column = table.columns[self._x_column_name]
        y_column = table.columns[self._y_column_name]

        if not isinstance(x_column, agate.NumberColumn):
            raise ValueError('Only NumberColumn is supported for scatter chart X axis values.')

        if not isinstance(y_column, agate.NumberColumn):
            raise ValueError('Only NumberColumn is supported for scatter chart Y axis values.')

        pyplot.scatter(
            x_column,
            y_column
        )

        pyplot.xlabel(self._x_column_name)
        pyplot.ylabel(self._y_column_name)
