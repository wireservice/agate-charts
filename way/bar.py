#!/usr/bin/env python

from matplotlib import pyplot
import agate

from way.base import Chart
from way.colors import ColorGenerator

class Bar(Chart):
    """
    Plots a bar chart.

    :param label_column_name: The name of a column in the source to be used for
        the horizontal axis labels.
    :param value_column_names: A sequence of column names in the source, each of
        which will used to define the vertical height of a bar.
    """
    def __init__(self, label_column_name, value_column_names):
        self._label_column_name = label_column_name
        self._value_column_names = value_column_names

    def _plot(self, table):
        """
        Plot a single bar chart, regardless of whether it is part of a small
        multiples series.
        """
        positions = range(len(table.columns[self._label_column_name]))
        colors = ColorGenerator()
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

    def run(self, source, filename=None):
        """
        Execute a bar plot of source which can be either a :class:`Table`
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
