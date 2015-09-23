#!/usr/bin/env python

import agate

from agatecharts.charts import Bars, Columns, Lines, Scatter
from agatecharts.table import TableCharts
from agatecharts.tableset import TableSetCharts

# Monkeypatch!
agate.Table.monkeypatch(TableCharts)
agate.TableSet.monkeypatch(TableSetCharts)
