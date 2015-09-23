#!/usr/bin/env python

from agatecharts.charts import *
from agatecharts.table import TableCharts
from agatecharts.tableset import TableSetCharts

# Monkeypatch!
agate.Table.monkeypatch(TableCharts)
agate.TableSet.monkeypatch(TableSetCharts)
