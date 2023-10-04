import agate

from agatecharts.charts.base import Chart
from agatecharts.colors import Qualitative


class Columns(Chart):
    def __init__(self, label_column_name, value_column_names):
        self._label_column_name = label_column_name

        if isinstance(value_column_names, str):
            value_column_names = [value_column_names]

        self._value_column_names = value_column_names

    def show_legend(self):
        return len(self._value_column_names) > 1

    def get_x_domain(self, table):
        return (None, None)

    def get_y_domain(self, table):
        y_min = min([min(table.columns[name].values_without_nulls()) for name in self._value_column_names])
        y_max = max([max(table.columns[name].values_without_nulls()) for name in self._value_column_names])

        return y_min, y_max

    def plot(self, table, axes):
        label_column = table.columns[self._label_column_name]

        if not isinstance(label_column.data_type, agate.Text) and \
                not isinstance(label_column.data_type, agate.Number) and \
                not isinstance(label_column.data_type, agate.Date):
            raise ValueError('Only Text, Number and Date data are supported for bar chart labels.')

        positions = range(len(label_column))
        colors = Qualitative()
        legend_bars = []
        bar_area = 0.65
        bar_width = bar_area / len(self._value_column_names)

        for i, value_column_name in enumerate(self._value_column_names):
            value_column = table.columns[value_column_name]

            if not isinstance(value_column.data_type, agate.Number):
                raise ValueError('Only Number data is supported for column chart values.')

            series_positions = []

            for j in positions:
                series_positions.append(positions[j] + (i * bar_width))

            plot_bars = axes.bar(
                series_positions,
                value_column,
                bar_width,
                color=next(colors),
                linewidth=0,
                label=value_column_name
            )

            legend_bars.append(plot_bars[0])

        axes.set_xlabel(self._label_column_name)
        axes.set_xticks([p + (bar_area / 2) for p in positions])
        axes.set_xticklabels(table.columns[self._label_column_name])

        if len(self._value_column_names) == 1:
            axes.set_ylabel(self._value_column_names[0])

        return (legend_bars, self._value_column_names)
