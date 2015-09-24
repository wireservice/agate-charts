#!/usr/bin/env python

import math

import agate
from matplotlib import pyplot

from agatecharts.charts import Bars, Columns, Lines, Scatter
from agatecharts.table import DEFAULT_DPI
from agatecharts.utils import roundoff

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

        if chart.show_legend():
            count += 1

        grid_rows = int(math.sqrt(count))
        grid_columns = math.ceil(float(count) / grid_rows)

        if not size:
            size = (
                DEFAULT_MULTIPLE_SIZE[0] * grid_columns,
                DEFAULT_MULTIPLE_SIZE[1] * grid_rows
            )

        pyplot.figure(figsize=size, dpi=dpi)

        # Compute max domain of all tables so they can be placed on the same axes
        x_min = float('inf')
        x_max = float('-inf')
        y_min = float('inf')
        y_max = float('-inf')

        for table in self.values():
            table_x_min, table_x_max = chart.get_x_domain(table)
            table_y_min, table_y_max = chart.get_y_domain(table)

            x_min = min(x_min, table_x_min)
            x_max = max(x_max, table_x_max)
            y_min = min(y_min, table_y_min)
            y_max = max(y_max, table_y_max)

        if x_min is not None:
            if x_min < 0:
                x_min = roundoff(x_max)
            else:
                x_min = 0

        if x_max is not None and x_max != 0:
            if x_max > 0:
                x_max = roundoff(x_max)
            else:
                x_max = 0

        if y_min is not None:
            if y_min < 0:
                y_min = roundoff(x_max)
            else:
                y_min = 0

        if y_max is not None:
            if y_max > 0:
                y_max = roundoff(y_max)
            else:
                y_max = 0

        i = 0

        for i, (key, table) in enumerate(self.items()):
            axes = pyplot.subplot(grid_rows, grid_columns, i + 1)

            legend = chart.plot(table, axes)

            pyplot.title(key)

            pyplot.grid(b=True, which='major', color='0.85', linestyle='-')
            axes.set_axisbelow(True)

            # matplotlib won't accept Decimal for limit values
            if x_min is not None and x_max is not None:
                axes.set_xlim(float(x_min), float(x_max))

            if y_min is not None and y_max is not None:
                axes.set_ylim(float(y_min), float(y_max))

        if chart.show_legend():
            axes = pyplot.subplot(grid_rows, grid_columns, i + 2)
            pyplot.axis('off')
            axes.legend(*legend, loc='center left', bbox_to_anchor=(0, 0.5))

        pyplot.tight_layout(pad=1, w_pad=1, h_pad=1)

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
