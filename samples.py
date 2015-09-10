#!/usr/bin/env python

import csv
import os
import shutil

import agate
import fever

OUTPUT_DIR = 'docs/samples'

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

for filename in os.listdir(OUTPUT_DIR):
    os.remove(os.path.join(OUTPUT_DIR, filename))

tester = agate.TypeTester(force={
    ' Date': agate.Date('%Y-%m-%d')
})

emissions = agate.Table.from_csv('examples/epa-emissions-20150910.csv', tester)

emissions = emissions.compute([
    ('day', agate.Formula(agate.Number(), lambda r: r[' Date'].day)),
    ('so2', agate.Formula(agate.Number(), lambda r: r[' SO2 (tons)'] or 0)),
    ('noX', agate.Formula(agate.Number(), lambda r: r[' NOx (tons)'] or 0)),
    ('co2', agate.Formula(agate.Number(), lambda r: r[' CO2 (short tons)'] or 0))
])

states = emissions.group_by('State')
new_york = states['NY']

# NB: key_type shouldn't be necessary--agate bug #234
days = emissions.group_by('day', key_type=agate.Number())
day_totals = days.aggregate([
    ('so2', agate.Sum(), 'so2'),
    ('co2', agate.Sum(), 'co2'),
    ('noX', agate.Sum(), 'noX')
])

dates = emissions.group_by(' Date', key_type=agate.Date('%Y-%m-%d'))
date_totals = dates.aggregate([
    ('so2', agate.Sum(), 'so2'),
    ('co2', agate.Sum(), 'co2'),
    ('noX', agate.Sum(), 'noX')
])

date_totals.pretty_print(5)

single_series = {
    'line_chart_simple': fever.Lines('day', 'co2'),
    'column_chart_simple': fever.Columns('day', 'co2'),
    'bar_chart_simple': fever.Bars('day', 'co2'),
    'scatter_chart': fever.Scatter('co2', 'so2')
}

time_series = {
    'line_chart_dates': fever.Lines(' Date', 'co2'),
    'column_chart_dates': fever.Columns(' Date', 'co2'),
    'bar_chart_dates': fever.Bars(' Date', 'co2')
}

multiple_series = {
    'line_chart_complex': fever.Lines('day', ['so2', 'noX']),
    'column_chart_complex': fever.Columns('day', ['so2', 'noX']),
    'bar_chart_complex': fever.Bars('day', ['so2', 'noX']),
}

with_dates = {
    'line_chart_dates': fever.Lines(' Date', 'so2'),
    'column_chart_dates': fever.Columns(' Date', 'so2'),
    'line_chart_dates': fever.Lines(' Date', 'so2'),
}

# Not small multiples
for name, chart in single_series.items():
    print(name)

    day_totals.plot(chart, filename=os.path.join(OUTPUT_DIR, '%s.png' % name))

for name, chart in time_series.items():
    print(name)

    date_totals.plot(chart, filename=os.path.join(OUTPUT_DIR, '%s.png' % name))

for name, chart in multiple_series.items():
    print(name)

    day_totals.plot(chart, filename=os.path.join(OUTPUT_DIR, '%s.png' % name))

# Small multiples
for name, chart in single_series.items():
    print(name)

    states.plot(chart, filename=os.path.join(OUTPUT_DIR, '%s_multiples.png' % name))

for name, chart in multiple_series.items():
    print(name)

    states.plot(chart, filename=os.path.join(OUTPUT_DIR, '%s_multiples.png' % name))
