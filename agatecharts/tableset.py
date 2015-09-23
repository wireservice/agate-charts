#!/usr/bin/env python

import math

import agate
from matplotlib import pyplot

from agatecharts.charts import *
from agatecharts.table import DEFAULT_DPI

#: Default small multiple chart size in inches
DEFAULT_MULTIPLE_SIZE = (4, 4)

class TableSetCharts(object):
    def bar_chart(self, label_column_name, value_column_names, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        See :meth:`.TableCharts.bar_chart`.
        """
        chart = Bars(label_column_name, value_column_names)

        self._plot(chart, filename, size, dpi)

    def column_chart(self, label_column_name, value_column_names, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        See :meth:`.TableCharts.column_chart`.
        """
        chart = Columns(label_column_name, value_column_names)

        self._plot(chart, filename, size, dpi)

    def line_chart(self, x_column_name, y_column_names, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        See :meth:`.TableCharts.line_chart`.
        """
        chart = Lines(x_column_name, y_column_names)

        self._plot(chart, filename, size, dpi)

    def scatter_chart(self, x_column_name, y_column_name, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        See :meth:`.TableCharts.scatter_chart`.
        """
        chart = Scatter(x_column_name, y_column_name)

        self._plot(chart, filename, size, dpi)

    def _plot(self, chart, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        See :meth:`.TableCharts._plot`.
        """
        if isinstance(self.values()[0], agate.TableSet):
            raise ValueError('agate-charts does not currently support nested TableSets.')

        count = len(self)

        if chart._show_legend():
            count += 1

        rows = int(math.sqrt(count))
        columns = math.ceil(float(count) / rows)

        if not size:
            size = (
                DEFAULT_MULTIPLE_SIZE[0] * columns,
                DEFAULT_MULTIPLE_SIZE[1] * rows
            )

        pyplot.figure(figsize=size, dpi=dpi)

        for i, (key, table) in enumerate(self.items()):
            axes = pyplot.subplot(rows, columns, i + 1)

            legend = chart._plot(table, axes)

            pyplot.title(key)

            pyplot.grid(b=True, which='major', color='0.85', linestyle='-')
            axes.set_axisbelow(True)

        if chart._show_legend():
            axes = pyplot.subplot(rows, columns, i + 2)
            pyplot.axis('off')
            axes.legend(*legend, loc='center left', bbox_to_anchor=(0, 0.5))

        pyplot.tight_layout(pad=1, w_pad=1, h_pad=1)

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
