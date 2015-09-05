#!/usr/bin/env python

import agate
from matplotlib import pyplot

from fever.base import Chart, Legend
from fever.colors import Qualitative

class Lines(Chart):
    """
    Plots a line chart.

    :param x_column_name: The name of a column in the source to be used for
        the horizontal axis.
    :param y_column_names: A sequence of column names in the source, each of
        which will be used for the vertical axis.
    """
    def __init__(self, x_column_name, y_column_names):
        self._x_column_name = x_column_name

        if isinstance(y_column_names, basestring):
            y_column_names = [y_column_names]

        self._y_column_names = y_column_names

    def _show_legend(self):
        return len(self._y_column_names) > 1

    def _plot(self, table):
        colors = Qualitative()
        lines = []

        for i, y_column_name in enumerate(self._y_column_names):
            plot_lines = pyplot.plot(
                table.columns[self._x_column_name],
                table.columns[y_column_name],
                linewidth=2,
                color=colors.next(),
                label=y_column_name
            )

            lines.extend(plot_lines)

        pyplot.xlabel(self._x_column_name)

        if len(self._y_column_names) == 1:
            pyplot.ylabel(self._y_column_names[0])

        return Legend(lines, self._y_column_names)
