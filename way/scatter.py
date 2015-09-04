#!/usr/bin/env python

from matplotlib import pyplot
import agate

from way.base import Chart

class Scatter(Chart):
    """
    Plots a scatter plot.

    :param x_column_name: The name of a column in the source to be used for
        the horizontal axis.
    :param y_column_name: The name of a column in the source to be used for
        the vertical axis.
    """
    def __init__(self, x_column_name, y_column_name):
        self._x_column_name = x_column_name
        self._y_column_name = y_column_name

    def _plot(self, table):
        """
        Plot a single scatter chart, regardless of whether it is part of a small
        multiples series.
        """
        pyplot.scatter(
            table.columns[self._x_column_name],
            table.columns[self._y_column_name]
        )

        pyplot.xlabel(self._x_column_name)
        pyplot.ylabel(self._y_column_name)

    def run(self, source, filename=None):
        """
        Execute a scatter plot of source which can be either a :class:`Table`
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
