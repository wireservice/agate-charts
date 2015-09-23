#!/usr/bin/env python

import collections

import agate
from matplotlib import pyplot

from fever.charts.base import Chart
from fever.colors import Qualitative

class Bars(Chart):
    """
    Plots a bar chart.

    :param label_column_name: The name of a column in the source to be used for
        the vertical axis labels. Must refer to a column containing
        :class:`.Text`, :class:`.Number` or :class:`.Date` data.
    :param value_column_names: One or more column names in the source, each of
        which will used to define the horizontal width of a bar. Must refer to a
        column containing :class:`.Number` data.
    """
    def __init__(self, label_column_name, value_column_names):
        self._label_column_name = label_column_name

        if isinstance(value_column_names, basestring):
            value_column_names = [value_column_names]

        self._value_column_names = value_column_names

    def _show_legend(self):
        return len(self._value_column_names) > 1

    def _plot(self, table, axes):
        label_column = table.columns[self._label_column_name]

        if not isinstance(label_column.data_type, agate.Text) and \
            not isinstance(label_column.data_type, agate.Number) and \
            not isinstance(label_column.data_type, agate.Date):
            raise ValueError('Only Text, Number and Date data are supported for bar chart labels.')

        positions = range(len(label_column))
        colors = Qualitative()
        bars = []
        bar_height = 0.35

        for i, value_column_name in enumerate(self._value_column_names):
            value_column = table.columns[value_column_name]

            if not isinstance(value_column.data_type, agate.Number):
                raise ValueError('Only Number data is supported for bar chart values.')

            series_positions = []

            for j in positions:
                series_positions.append(positions[j] + (i + 1) * bar_height)

            plot_bars = axes.barh(
                series_positions,
                value_column,
                bar_height,
                color=colors.next(),
                label=value_column_name
            )

            bars.extend(plot_bars)

        axes.set_ylabel(self._label_column_name)
        axes.set_yticks(series_positions)
        axes.set_yticklabels(table.columns[self._label_column_name])

        if len(self._value_column_names) == 1:
            axes.set_xlabel(self._value_column_names[0])

        return (bars, self._value_column_names)
