class Chart:
    """
    Base class for a chart type.
    """

    def show_legend(self):
        """
        Returns true if this chart should render a legend. (Usually if there
        is more than one series of data.)
        """
        raise NotImplementedError

    def get_x_domain(self, table):
        """
        Compute the x domain for this chart type for a given table.
        """
        raise NotImplementedError

    def get_y_domain(self, table):
        """
        Compute the y domain for this chart type for a given table.
        """
        raise NotImplementedError

    def plot(self, table, axes):
        """
        Subclasses implement this method to draw a single chart, regardless of
        whether or not it is part of small multiples.
        """
        raise NotImplementedError
