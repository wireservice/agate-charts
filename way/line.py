#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot
import agate

from way.base import Plot

class Line(Plot):
    def __init__(self, x_column_name, y_column_name, filename=None):
        self._x_column_name = x_column_name
        self._y_column_name = y_column_name

    def _plot(self, table):
        pyplot.plot(
            table.columns[self._x_column_name],
            table.columns[self._y_column_name]
        )

        pyplot.xlabel(self._x_column_name)
        pyplot.ylabel(self._y_column_name)

    def run(self, source, filename=None):
        if isinstance(source, agate.TableSet):
            for i, (key, table) in enumerate(source.items()):
                pyplot.subplot(1, len(source), i + 1)
                # pyplot.tight_layout(pad=0, w_pad=3)

                self._plot(table)

                pyplot.title(key)
        else:
            self._plot(source)

        pyplot.legend()

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
