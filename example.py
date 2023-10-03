#!/usr/bin/env python

import os

import agate

import agatecharts

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
state_totals = states.aggregate([
    ('so2', agate.Sum('so2')),
    ('co2', agate.Sum('co2')),
    ('noX', agate.Sum('noX'))
])

new_york = states['NY']

# NB: key_type shouldn't be necessary--agate bug #234
days = emissions.group_by('day', key_type=agate.Number())
day_totals = days.aggregate([
    ('so2', agate.Sum('so2')),
    ('co2', agate.Sum('co2')),
    ('noX', agate.Sum('noX'))
])

dates = emissions.group_by(' Date', key_type=agate.Date('%Y-%m-%d'))
date_totals = dates.aggregate([
    ('so2', agate.Sum('so2')),
    ('co2', agate.Sum('co2')),
    ('noX', agate.Sum('noX'))
])

print('Simple charts')

day_totals.line_chart('day', 'co2', filename=os.path.join(OUTPUT_DIR, 'line_chart_simple.png'))
state_totals.column_chart('State', 'co2', filename=os.path.join(OUTPUT_DIR, 'column_chart_simple.png'))
state_totals.bar_chart('State', 'co2', filename=os.path.join(OUTPUT_DIR, 'bar_chart_simple.png'))
day_totals.scatter_chart('so2', 'noX', filename=os.path.join(OUTPUT_DIR, 'scatter_chart.png'))

print('Time series')

date_totals.line_chart(' Date', 'co2', filename=os.path.join(OUTPUT_DIR, 'line_chart_dates.png'))
date_totals.column_chart(' Date', 'co2', filename=os.path.join(OUTPUT_DIR, 'column_chart_dates.png'))
date_totals.bar_chart(' Date', 'co2', filename=os.path.join(OUTPUT_DIR, 'bar_chart_dates.png'))

print('Multiple series')

day_totals.line_chart('day', ['so2', 'noX'], filename=os.path.join(OUTPUT_DIR, 'line_chart_complex.png'))
state_totals.column_chart('State', ['so2', 'noX'], filename=os.path.join(OUTPUT_DIR, 'column_chart_complex.png'))
state_totals.bar_chart('State', ['so2', 'noX'], filename=os.path.join(OUTPUT_DIR, 'bar_chart_complex.png'))

print('Small multiples')

states.line_chart('day', 'co2', filename=os.path.join(OUTPUT_DIR, 'line_chart_simple_multiples.png'))
states.column_chart('day', 'co2', filename=os.path.join(OUTPUT_DIR, 'column_chart_simple_multiples.png'))
states.bar_chart('day', 'co2', filename=os.path.join(OUTPUT_DIR, 'bar_chart_simple_multiples.png'))
states.scatter_chart('so2', 'noX', filename=os.path.join(OUTPUT_DIR, 'scatter_chart_multiples.png'))

print('Small multiples with multiple series')

states.line_chart('day', ['so2', 'noX'], filename=os.path.join(OUTPUT_DIR, 'line_chart_complex_multiples.png'))
states.column_chart('day', ['so2', 'noX'], filename=os.path.join(OUTPUT_DIR, 'column_chart_complex_multiples.png'))
states.bar_chart('day', ['so2', 'noX'], filename=os.path.join(OUTPUT_DIR, 'bar_chart_complex_multiples.png'))
