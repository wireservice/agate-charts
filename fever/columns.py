#!/usr/bin/env python

import collections

import agate
from matplotlib import pyplot

from fever.base import Chart
from fever.colors import Qualitative

class Columns(Chart):
    """
    Plots a column chart.

    :param label_column_name: The name of a column in the source to be used for
        the horizontal axis labels.
    :param value_column_names: One or more column names in the source, each of
        which will used to define the vertical height of a bar.
    """
    def __init__(self, label_column_name, value_column_names):
        self._label_column_name = label_column_name

        if isinstance(value_column_names, basestring):
            value_column_names = [value_column_names]

        self._value_column_names = value_column_names

    def _plot(self, table):
        positions = range(len(table.columns[self._label_column_name]))
        colors = Qualitative()
        bar_width = 0.35

        for i, value_column_name in enumerate(self._value_column_names):
            series_positions = []

            for j in positions:
                series_positions.append(positions[j] + (i + 1) * bar_width)

            pyplot.bar(
                series_positions,
                table.columns[value_column_name],
                bar_width,
                color=colors.next(),
                label=value_column_name
            )

        pyplot.xlabel(self._label_column_name)
        pyplot.xticks(series_positions, table.columns[self._label_column_name])

        if len(self._value_column_names) == 1:
            pyplot.ylabel(self._value_column_names[0])
        else:
            pyplot.legend()
