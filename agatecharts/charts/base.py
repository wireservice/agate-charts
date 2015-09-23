#!/usr/bin/env python

class Chart(object):
    """
    Base class for a chart type.
    """
    def show_legend(self):
        """
        Returns true if this chart should render a legend. (Usually if there
        is more than one series of data.)
        """
        raise NotImplementedError

    def plot(self, table, axes):
        """
        Subclasses implement this method to draw a single chart, regardless of
        whether or not it is part of small multiples.
        """
        raise NotImplementedError
