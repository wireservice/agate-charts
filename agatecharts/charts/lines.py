#!/usr/bin/env python

import agate
from matplotlib import pyplot

from agatecharts.charts.base import Chart
from agatecharts.colors import Qualitative

class Lines(Chart):
    """
    Plots a line chart.

    :param x_column_name: The name of a column in the source to be used for
        the horizontal axis. May refer to a column containing
        :class:`.Number`, :class:`.Date` or :class:`.DateTime`
        data.
    :param y_column_names: A sequence of column names in the source, each of
        which will be used for the vertical axis. Must refer to a column with
        :class:`.Number` data.
    """
    def __init__(self, x_column_name, y_column_names):
        self._x_column_name = x_column_name

        if isinstance(y_column_names, basestring):
            y_column_names = [y_column_names]

        self._y_column_names = y_column_names

    def _show_legend(self):
        return len(self._y_column_names) > 1

    def _plot(self, table, axes):
        colors = Qualitative()
        lines = []

        x_column = table.columns[self._x_column_name]

        if not isinstance(x_column.data_type, agate.Number) and \
            not isinstance(x_column.data_type, agate.Date) and \
            not isinstance(x_column.data_type, agate.DateTime):
            raise ValueError('Only Number, Date and DateTime data are supported for line chart X-axis.')

        for i, y_column_name in enumerate(self._y_column_names):
            y_column = table.columns[y_column_name]

            if not isinstance(y_column.data_type, agate.Number):
                raise ValueError('Only Number data is supported for line chart Y-axis.')

            plot_lines = axes.plot(
                x_column,
                y_column,
                linewidth=2,
                color=colors.next(),
                label=y_column_name
            )

            lines.extend(plot_lines)

        axes.set_xlabel(self._x_column_name)

        if len(self._y_column_names) == 1:
            axes.set_ylabel(self._y_column_names[0])

        return (lines, self._y_column_names)
