import agate
from matplotlib import pyplot

from agatecharts.charts import Bars, Columns, Lines, Scatter
from agatecharts.utils import round_limits

#: Default rendered chart size in inches
DEFAULT_SIZE = (8, 8)

#: Default rendered chart dpi
DEFAULT_DPI = 72


def bar_chart(self, label_column_name, value_column_names, filename=None, size=DEFAULT_SIZE, dpi=DEFAULT_DPI):
    """
    Plots a bar chart.

    See :meth:`agatecharts.table.plot` for an explanation of keyword arguments.

    :param label_column_name: The name of a column in the source to be used for
        the vertical axis labels. Must refer to a column containing
        :class:`.Text`, :class:`.Number` or :class:`.Date` data.
    :param value_column_names: One or more column names in the source, each of
        which will used to define the horizontal width of a bar. Must refer to a
        column containing :class:`.Number` data.
    """
    chart = Bars(label_column_name, value_column_names)

    plot(self, chart, filename, size, dpi)


def column_chart(self, label_column_name, value_column_names, filename=None, size=DEFAULT_SIZE, dpi=DEFAULT_DPI):
    """
    Plots a column chart.

    See :meth:`agatecharts.table.plot` for an explanation of keyword arguments.

    :param label_column_name: The name of a column in the source to be used for
        the horizontal axis labels. Must refer to a column containing
        :class:`.Text`, :class:`.Number` or :class:`.Date` data.
    :param value_column_names: One or more column names in the source, each of
        which will used to define the vertical height of a bar. Must refer to a
        column containing :class:`.Number` data.
    """
    chart = Columns(label_column_name, value_column_names)

    plot(self, chart, filename, size, dpi)


def line_chart(self, x_column_name, y_column_names, filename=None, size=DEFAULT_SIZE, dpi=DEFAULT_DPI):
    """
    Plots a line chart.

    See :meth:`agatecharts.table.plot` for an explanation of keyword arguments.

    :param x_column_name: The name of a column in the source to be used for
        the horizontal axis. May refer to a column containing
        :class:`.Number`, :class:`.Date` or :class:`.DateTime`
        data.
    :param y_column_names: A sequence of column names in the source, each of
        which will be used for the vertical axis. Must refer to a column with
        :class:`.Number` data.
    """
    chart = Lines(x_column_name, y_column_names)

    plot(self, chart, filename, size, dpi)


def scatter_chart(self, x_column_name, y_column_name, filename=None, size=DEFAULT_SIZE, dpi=DEFAULT_DPI):
    """
    Plots a scatter plot.

    See :meth:`agatecharts.table.plot` for an explanation of keyword arguments.

    :param x_column_name: Column containing X values for the points to plot.
        Must refer to a column containg :class:`.Number` data.
    :param y_column_name: Column containing Y values for the points to plot.
        Must refer to a column containg :class:`.Number` data.
    """
    chart = Scatter(x_column_name, y_column_name)

    plot(self, chart, filename, size, dpi)


def plot(table, chart, filename=None, size=DEFAULT_SIZE, dpi=DEFAULT_DPI):
    """
    Execute a plot of this :class:`.Table`.

    This method should not be called directly by the user.

    :param chart: An chart class to render.
    :param filename: A filename to render to. If not specified will render
        to screen in "interactive mode".
    :param size: A (width, height) tuple in inches defining the size of the
        canvas to render to.
    :param dpi: A number defining the pixels-per-inch to render.
    """
    if chart.show_legend():
        size = (
            size[0] * 1.2,
            size[1]
        )

    x_min, x_max = chart.get_x_domain(table)
    y_min, y_max = chart.get_y_domain(table)
    x_min, x_max, y_min, y_max = round_limits(x_min, x_max, y_min, y_max)

    pyplot.figure(figsize=size, dpi=dpi)
    axes = pyplot.subplot(1, 1, 1)

    chart.plot(table, axes)

    pyplot.grid(visible=True, which='major', color='0.85', linestyle='-')
    axes.set_axisbelow(True)

    # matplotlib won't accept Decimal for limit values
    if x_min is not None and x_max is not None:
        axes.set_xlim(float(x_min), float(x_max))

    if y_min is not None and y_max is not None:
        axes.set_ylim(float(y_min), float(y_max))

    if chart.show_legend():
        bbox = axes.get_position()
        axes.set_position([bbox.x0, bbox.y0, bbox.width / 1.2, bbox.height])

        axes.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    if filename:
        pyplot.savefig(filename)
    else:
        pyplot.show()


agate.Table.bar_chart = bar_chart
agate.Table.column_chart = column_chart
agate.Table.line_chart = line_chart
agate.Table.scatter_chart = scatter_chart
