#!/usr/bin/env python

import agate

from agatecharts.charts.base import Chart

class Scatter(Chart):
    def __init__(self, x_column_name, y_column_name):
        self._x_column_name = x_column_name
        self._y_column_name = y_column_name

    def show_legend(self):
        return False

    def plot(self, table, axes):
        x_column = table.columns[self._x_column_name]
        y_column = table.columns[self._y_column_name]

        if not isinstance(x_column.data_type, agate.Number):
            raise ValueError('Only Number data is supported for scatter chart X axis values.')

        if not isinstance(y_column.data_type, agate.Number):
            raise ValueError('Only Number data is supported for scatter chart Y axis values.')

        axes.scatter(
            x_column,
            y_column
        )

        axes.set_xlabel(self._x_column_name)
        axes.set_ylabel(self._y_column_name)
