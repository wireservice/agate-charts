#!/usr/bin/env python

from matplotlib import pyplot

#: Default rendered chart size in inches
DEFAULT_SIZE = (8, 8)

#: Default rendered chart dpi
DEFAULT_DPI = 72

class TableFever(object):
    def plot(self, chart, filename=None, size=None, dpi=DEFAULT_DPI):
        """
        Execute a plot of this :class:`.Table`.

        :param chart: An instance of :class:`.Chart` to render.
        :param filename: A filename to render to. If not specified will render
            to screen in "interactive mode".
        :param size: A (width, height) tuple in inches defining the size of the
            canvas to render to.
        :param dpi: A number defining the pixels-per-inch to render.
        """
        if not size:
            size = DEFAULT_SIZE

        if chart._show_legend():
            size = (
                size[0] * 1.2,
                size[1]
            )

        pyplot.figure(figsize=size, dpi=dpi)
        axes = pyplot.subplot(1, 1, 1)

        legend = chart._plot(self, axes)

        pyplot.grid(b=True, which='major', color='0.85', linestyle='-')
        axes.set_axisbelow(True)

        if chart._show_legend():
            bbox = axes.get_position()
            axes.set_position([bbox.x0, bbox.y0, bbox.width / 1.2, bbox.height])

            axes.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        if filename:
            pyplot.savefig(filename)
        else:
            pyplot.show()
