#!/usr/bin/env python

from fever.charts import *
from fever.table import TableFever
from fever.tableset import TableSetFever

# Monkeypatch!
agate.Table.monkeypatch(TableFever)
agate.TableSet.monkeypatch(TableSetFever)
