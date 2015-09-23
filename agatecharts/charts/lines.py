#!/usr/bin/env python

import agate

from agatecharts.charts.base import Chart
from agatecharts.colors import Qualitative

class Lines(Chart):
    def __init__(self, x_column_name, y_column_names):
        self._x_column_name = x_column_name

        if isinstance(y_column_names, basestring):
            y_column_names = [y_column_names]

        self._y_column_names = y_column_names

    def show_legend(self):
        return len(self._y_column_names) > 1

    def plot(self, table, axes):
        colors = Qualitative()
        lines = []

        x_column = table.columns[self._x_column_name]

        if not isinstance(x_column.data_type, agate.Number) and \
            not isinstance(x_column.data_type, agate.Date) and \
            not isinstance(x_column.data_type, agate.DateTime):
            raise ValueError('Only Number, Date and DateTime data are supported for line chart X-axis.')

        for y_column_name in self._y_column_names:
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
