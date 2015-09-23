#!/usr/bin/env python

from agatecharts.charts import *
from agatecharts.table import TableFever
from agatecharts.tableset import TableSetFever

# Monkeypatch!
agate.Table.monkeypatch(TableFever)
agate.TableSet.monkeypatch(TableSetFever)
