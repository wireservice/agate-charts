#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot
import agate

from way.base import Chart

class Line(Chart):
    """
    Plots a line chart.

    :param x_column_name: The name of a column in the source to be used for
        the horizontal axis.
    :param y_column_names: A sequence of column names in the source, each of
        which will be used for the vertical axis.
    """
    def __init__(self, x_column_name, y_column_names):
        self._x_column_name = x_column_name
        self._y_column_names = y_column_names

    def _plot(self, table):
        """
        Plot a single line chart, regardless of whether it is part of a small
        multiples series.
        """
        for i, y_column_name in enumerate(self._y_column_names):
            pyplot.plot(
                table.columns[self._x_column_name],
                table.columns[y_column_name],
                label=y_column_name
            )

        pyplot.xlabel(self._x_column_name)

        if len(self._y_column_names) == 1:
            pyplot.ylabel(self._y_column_names[0])
        else:
            pyplot.legend()

    def run(self, source, filename=None):
        """
        Execute a line plot of source which can be either a :class:`Table`
        or a :class:`TableSet`. In the latter case the output will be in small
        multiples format.
        """
        if isinstance(source, agate.TableSet):
            for i, (key, table) in enumerate(source.items()):
                pyplot.subplot(1, len(source), i + 1)
                # pyplot.tight_layout(pad=0, w_pad=3)

                self._plot(table)

                pyplot.title(key)
        else:
            self._plot(source)

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
