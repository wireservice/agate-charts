#!/usr/bin/env python

import agate

def _plot(self, chart, *args, **kwargs):
    chart.run(self, *args, **kwargs)

agate.Table.plot = _plot
agate.TableSet.plot = _plot
