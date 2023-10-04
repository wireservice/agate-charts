import math

import agate
from matplotlib import pyplot

from agatecharts.charts import Bars, Columns, Lines, Scatter
from agatecharts.table import DEFAULT_DPI
from agatecharts.utils import round_limits

#: Default small multiple chart size in inches
DEFAULT_MULTIPLE_SIZE = (4, 4)


def bar_chart(self, label_column_name, value_column_names, filename=None, size=None, dpi=DEFAULT_DPI):
    """
    See :meth:`agatecharts.table.bar_chart`.
    """
    chart = Bars(label_column_name, value_column_names)

    plot(self, chart, filename, size, dpi)


def column_chart(self, label_column_name, value_column_names, filename=None, size=None, dpi=DEFAULT_DPI):
    """
    See :meth:`agatecharts.table.column_chart`.
    """
    chart = Columns(label_column_name, value_column_names)

    plot(self, chart, filename, size, dpi)


def line_chart(self, x_column_name, y_column_names, filename=None, size=None, dpi=DEFAULT_DPI):
    """
    See :meth:`agatecharts.table.line_chart`.
    """
    chart = Lines(x_column_name, y_column_names)

    plot(self, chart, filename, size, dpi)


def scatter_chart(self, x_column_name, y_column_name, filename=None, size=None, dpi=DEFAULT_DPI):
    """
    See :meth:`agatecharts.table.scatter_chart`.
    """
    chart = Scatter(x_column_name, y_column_name)

    plot(self, chart, filename, size, dpi)


def plot(tableset, chart, filename=None, size=None, dpi=DEFAULT_DPI):
    """
    See :meth:`agatecharts.table.plot`.
    """
    if isinstance(tableset.values()[0], agate.TableSet):
        raise ValueError('agate-charts does not currently support nested TableSets.')

    count = len(tableset)

    if chart.show_legend():
        count += 1

    grid_rows = int(math.sqrt(count))
    grid_columns = math.ceil(float(count) / grid_rows)

    if not size:
        size = (
            DEFAULT_MULTIPLE_SIZE[0] * grid_columns,
            DEFAULT_MULTIPLE_SIZE[1] * grid_rows
        )

    pyplot.figure(figsize=size, dpi=dpi)

    # Compute max domain of all tables so they can be placed on the same axes
    x_min = float('inf')
    x_max = float('-inf')
    y_min = float('inf')
    y_max = float('-inf')

    for table in tableset.values():
        table_x_min, table_x_max = chart.get_x_domain(table)
        table_y_min, table_y_max = chart.get_y_domain(table)

        x_min = min(filter(None, [x_min, table_x_min]))
        x_max = max(filter(None, [x_max, table_x_max]))
        y_min = min(filter(None, [y_min, table_y_min]))
        y_max = max(filter(None, [y_max, table_y_max]))

    x_min, x_max, y_min, y_max = round_limits(x_min, x_max, y_min, y_max)

    i = 0

    for i, (key, table) in enumerate(tableset.items()):
        axes = pyplot.subplot(grid_rows, grid_columns, i + 1)

        legend = chart.plot(table, axes)

        pyplot.title(key)

        pyplot.grid(visible=True, which='major', color='0.85', linestyle='-')
        axes.set_axisbelow(True)

        # matplotlib won't accept Decimal for limit values
        if x_min is not None and x_max is not None:
            axes.set_xlim(float(x_min), float(x_max))

        if y_min is not None and y_max is not None:
            axes.set_ylim(float(y_min), float(y_max))

    if chart.show_legend():
        axes = pyplot.subplot(grid_rows, grid_columns, i + 2)
        pyplot.axis('off')
        axes.legend(*legend, loc='center left', bbox_to_anchor=(0, 0.5))

    pyplot.tight_layout(pad=1, w_pad=1, h_pad=1)

    if filename:
        pyplot.savefig(filename)
    else:
        pyplot.show()


agate.TableSet.bar_chart = bar_chart
agate.TableSet.column_chart = column_chart
agate.TableSet.line_chart = line_chart
agate.TableSet.scatter_chart = scatter_chart
