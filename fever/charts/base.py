#!/usr/bin/env python

import math

import agate
from matplotlib import pyplot

#: Default rendered chart size in inches
DEFAULT_SIZE = (8, 8)

#: Default small multiple chart size in inches
DEFAULT_MULTIPLE_SIZE = (4, 4)

#: Default rendered chart dpi
DEFAULT_DPI = 72

class Chart(object):
    """
    Base class for a chart type.
    """
    def _plot(self):
        """
        Subclasses implement this method to draw a single chart, regardless of
        whether or not it is part of small multiples.
        """
        raise NotImplementedError

    def run(self, source, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        Execute a plot of the source which can be either a :class:`agate.Table`
        or a :class:`agate.TableSet`. In the latter case the output will be in
        small multiples format.

        :param source: A :class:`agate.Table` or :class:`agate.TableSet` to
            chart.
        :param filename: A filename to render to. If not specified will render
            to screen in "interactive mode".
        :param size: A (width, height) tuple in inches defining the size of the
            canvas to render to.
        :param dpi: A number defining the pixels-per-inch to render.
        """
        if isinstance(source, agate.TableSet):
            if isinstance(source.values()[0], agate.TableSet):
                raise ValueError('fever does not currently support nested TableSets.')

            count = len(source)

            if self._show_legend():
                count += 1

            rows = int(math.sqrt(count))
            columns = math.ceil(float(count) / rows)

            if not size:
                size = (
                    DEFAULT_MULTIPLE_SIZE[0] * columns,
                    DEFAULT_MULTIPLE_SIZE[1] * rows
                )

            pyplot.figure(figsize=size, dpi=dpi)

            for i, (key, table) in enumerate(source.items()):
                axes = pyplot.subplot(rows, columns, i + 1)

                legend = self._plot(table)

                pyplot.title(key)

                pyplot.grid(b=True, which='major', color='0.85', linestyle='-')
                axes.set_axisbelow(True)

            if self._show_legend():
                axes = pyplot.subplot(rows, columns, i + 2)
                pyplot.axis('off')
                axes.legend(*legend, loc='center left', bbox_to_anchor=(0, 0.5))

            pyplot.tight_layout(pad=1, w_pad=1, h_pad=1)
        else:
            if not size:
                size = DEFAULT_SIZE

            if self._show_legend():
                size = (
                    size[0] * 1.2,
                    size[1]
                )

            pyplot.figure(figsize=size, dpi=dpi)
            axes = pyplot.subplot(1, 1, 1)

            legend = self._plot(source)

            pyplot.grid(b=True, which='major', color='0.85', linestyle='-')
            axes.set_axisbelow(True)

            if self._show_legend():
                bbox = axes.get_position()
                axes.set_position([bbox.x0, bbox.y0, bbox.width / 1.2, bbox.height])

                axes.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
