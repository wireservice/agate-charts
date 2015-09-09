#!/usr/bin/env python

import agate
from matplotlib import pyplot

from fever.base import Chart

class Scatter(Chart):
    """
    Plots a scatter plot.

    :param x_column_name: Column containing x values for the points to plot.
    :param y_column_name: Column containing y values for the points to plot.
    """
    def __init__(self, x_column_name, y_column_name):
        self._x_column_name = x_column_name
        self._y_column_name = y_column_name

    def _show_legend(self):
        return False

    def _plot(self, table):
        pyplot.scatter(
            table.columns[self._x_column_name],
            table.columns[self._y_column_name]
        )

        pyplot.xlabel(self._x_column_name)
        pyplot.ylabel(self._y_column_name)
