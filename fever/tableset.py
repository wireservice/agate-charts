#!/usr/bin/env python

import math

import agate
from matplotlib import pyplot

from fever.table import DEFAULT_DPI

#: Default small multiple chart size in inches
DEFAULT_MULTIPLE_SIZE = (4, 4)

class TableSetFever(object):
    def plot(self, chart, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        Execute a plot of this :class:`.TableSet`.

        :param chart: An instance of :class:`.Chart` to render.
        :param filename: A filename to render to. If not specified will render
            to screen in "interactive mode".
        :param size: A (width, height) tuple in inches defining the size of the
            canvas to render to.
        :param dpi: A number defining the pixels-per-inch to render.
        """
        if isinstance(self.values()[0], agate.TableSet):
            raise ValueError('fever does not currently support nested TableSets.')

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
