import agate

from agatecharts.charts.base import Chart
from agatecharts.colors import Qualitative


class Lines(Chart):
    def __init__(self, x_column_name, y_column_names):
        self._x_column_name = x_column_name

        if isinstance(y_column_names, str):
            y_column_names = [y_column_names]

        self._y_column_names = y_column_names

    def show_legend(self):
        return len(self._y_column_names) > 1

    def get_x_domain(self, table):
        if not isinstance(table.columns[self._x_column_name].data_type, agate.Number):
            return (None, None)

        x_min = min(table.columns[self._x_column_name])
        x_max = max(table.columns[self._x_column_name])

        return (x_min, x_max)

    def get_y_domain(self, table):
        y_min = min([min(table.columns[name]) for name in self._y_column_names])
        y_max = max([max(table.columns[name]) for name in self._y_column_names])

        return (y_min, y_max)

    def plot(self, table, axes):
        colors = Qualitative()
        legend_lines = []

        x_column = table.columns[self._x_column_name]

        if not isinstance(x_column.data_type, agate.Number) and \
                not isinstance(x_column.data_type, agate.Date) and \
                not isinstance(x_column.data_type, agate.DateTime):
            raise ValueError('Only Number, Date and DateTime data are supported for line chart X-axis.')

        for y_column_name in self._y_column_names:
            y_column = table.columns[y_column_name]

            if not isinstance(y_column.data_type, agate.Number):
                raise ValueError('Only Number data is supported for line chart Y-axis.')

            plot_lines = axes.plot(
                x_column,
                y_column,
                linewidth=2,
                color=next(colors),
                label=y_column_name
            )

            legend_lines.append(plot_lines[0])

        axes.set_xlabel(self._x_column_name)

        if len(self._y_column_names) == 1:
            axes.set_ylabel(self._y_column_names[0])

        return (legend_lines, self._y_column_names)
