#!/usr/bin/env python

from fever.charts.base import DEFAULT_DPI

class TableFever(object):
    def plot(self, chart, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        Plot a given chart using data from this table and the specified arguments.

        :param filename: A filename to render to. If not specified will render
            to screen in "interactive mode".
        :param size: A (width, height) tuple in inches defining the size of the
            canvas to render to.
        :param dpi: A number defining the pixels-per-inch to render.
        """
        chart.run(self, filename=filename, size=size, dpi=dpi)
