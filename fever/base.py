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
        Execute a plot of the source which can be either a :class:`Table`
        or a :class:`TableSet`. In the latter case the output will be in small
        multiples format.

        :param source: A :class:`Table` or :class:`TableSet` to chart.
        :param filename: A filename to render to. If not specified will render
            to screen in "interactive mode".
        :param size: A (width, height) tuple in inches defining the size of the
            canvas to render to.
        :param dpi: A number defining the pixels-per-inch to render.
        """
        if isinstance(source, agate.TableSet):
            # Plus one for legend spot
            count = len(source) + 1

            rows = int(math.sqrt(count))
            columns = math.ceil(float(count) / rows)

            if not size:
                size = (
                    DEFAULT_MULTIPLE_SIZE[0] * columns,
                    DEFAULT_MULTIPLE_SIZE[1] * rows
                )

            figure = pyplot.figure(figsize=size, dpi=dpi)

            for i, (key, table) in enumerate(source.items()):
                pyplot.subplot(rows, columns, i + 1)

                self._plot(table)

                pyplot.title(key)

            axes = pyplot.subplot(rows, columns, i + 2)
            pyplot.axis('off')
            pos = axes.get_position()

            self._legend(figure, pos)

            pyplot.tight_layout(pad=1, w_pad=1, h_pad=1)
        else:
            if not size:
                size = DEFAULT_SIZE

            pyplot.figure(figsize=size, dpi=dpi)

            self._plot(source)

            pyplot.legend()

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
