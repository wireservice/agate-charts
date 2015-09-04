#!/usr/bin/env python

import agate

def _plot(self, plot, *args, **kwargs):
    plot.run(self, *args, **kwargs)

agate.Table.plot = _plot
agate.TableSet.plot = _plot
