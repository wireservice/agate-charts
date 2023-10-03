#!/usr/bin/env python

def patch():
    """
    Patch the features of this library onto agate's core :class:`.Table` and :class:`.TableSet`.
    """
    import agate

    from agatecharts.table import TableCharts
    from agatecharts.tableset import TableSetCharts

    agate.Table.monkeypatch(TableCharts)
    agate.TableSet.monkeypatch(TableSetCharts)
