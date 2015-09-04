#!/usr/bin/env python

import agate
from matplotlib import pyplot

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

    def run(self, source, filename=None):
        """
        Execute a plot of the source which can be either a :class:`Table`
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
