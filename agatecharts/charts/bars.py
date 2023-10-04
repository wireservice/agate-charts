import agate

from agatecharts.charts.base import Chart
from agatecharts.colors import Qualitative


class Bars(Chart):
    def __init__(self, label_column_name, value_column_names):
        self._label_column_name = label_column_name

        if isinstance(value_column_names, str):
            value_column_names = [value_column_names]

        self._value_column_names = value_column_names

    def show_legend(self):
        return len(self._value_column_names) > 1

    def get_x_domain(self, table):
        x_min = min([min(table.columns[name].values_without_nulls()) for name in self._value_column_names])
        x_max = max([max(table.columns[name].values_without_nulls()) for name in self._value_column_names])

        return x_min, x_max

    def get_y_domain(self, table):
        return (None, None)

    def plot(self, table, axes):
        label_column = table.columns[self._label_column_name]

        if not isinstance(label_column.data_type, agate.Text) and \
                not isinstance(label_column.data_type, agate.Number) and \
                not isinstance(label_column.data_type, agate.Date):
            raise ValueError('Only Text, Number and Date data are supported for bar chart labels.')

        series_count = len(self._value_column_names)
        positions = list(range(len(label_column)))
        colors = Qualitative()
        legend_bars = []
        bar_area = 0.65
        bar_height = bar_area / len(self._value_column_names)

        # Display first value at the top of the chart.
        positions.reverse()

        for i, value_column_name in enumerate(self._value_column_names):
            value_column = table.columns[value_column_name]

            if not isinstance(value_column.data_type, agate.Number):
                raise ValueError('Only Number data is supported for bar chart values.')

            series_positions = []

            for j in positions:
                series_positions.append(j + (series_count - i) * bar_height)

            plot_bars = axes.barh(
                series_positions,
                value_column,
                bar_height,
                color=next(colors),
                linewidth=0,
                label=value_column_name
            )

            legend_bars.append(plot_bars[0])

        axes.set_ylabel(self._label_column_name)
        axes.set_yticks([p + (series_count - i) * bar_height + (bar_area / 2) for p in positions])
        axes.set_yticklabels(table.columns[self._label_column_name])

        if len(self._value_column_names) == 1:
            axes.set_xlabel(self._value_column_names[0])

        return (legend_bars, self._value_column_names)
