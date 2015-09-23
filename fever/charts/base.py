#!/usr/bin/env python

class Chart(object):
    """
    Base class for a chart type.
    """
    def _plot(self, table, axes):
        """
        Subclasses implement this method to draw a single chart, regardless of
        whether or not it is part of small multiples.
        """
        raise NotImplementedError
