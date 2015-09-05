#!/usr/bin/env python

import csv
import os
import shutil

from agate import Table, DateType, NumberType, TextType, Sum, StDev
import fever

OUTPUT_DIR = 'samples'

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

for filename in os.listdir(OUTPUT_DIR):
    os.remove(os.path.join(OUTPUT_DIR, filename))

text_type = TextType()
number_type = NumberType()

COLUMNS = (
    ('gender', text_type),
    ('month', number_type),
    ('median', number_type),
    ('stdev', number_type),
    ('1st', number_type),
    ('3rd', number_type),
    ('5th', number_type),
    ('15th', number_type),
    ('25th', number_type),
    ('50th', number_type),
    ('75th', number_type),
    ('85th', number_type),
    ('95th', number_type),
    ('97th', number_type),
    ('99th', number_type)
)

with open('examples/heights.csv') as f:
    # Create a csv reader
    reader = csv.reader(f)

    # Skip header
    next(f)

    # Create the table
    table = Table(reader, COLUMNS)

i = 1

samples = {
    'line_chart_simple': fever.Lines('month', 'median'),
    'line_chart_complex': fever.Lines('month', ['median', 'stdev']),
    'column_chart_simple': fever.Columns('month', 'median'),
    'column_chart_complex': fever.Columns('month', ['median', 'stdev']),
    'bar_chart_simple': fever.Bars('month', 'median'),
    'bar_chart_complex': fever.Bars('month', ['median', 'stdev']),
    'scatter_chart': fever.Scatter('median', 'stdev')
}

boys = table.where(lambda r: r['gender'] == 'male')

for name in ['line_chart_simple', 'line_chart_complex']:
    chart = samples[name]
    boys.plot(chart, filename=os.path.join(OUTPUT_DIR, '%i_%s.png' % (i, name)))

    i += 1

first_year = boys.where(lambda r: r['month'] < 73)

for name in ['column_chart_simple', 'column_chart_complex', 'bar_chart_simple', 'bar_chart_complex', 'scatter_chart']:
    chart = samples[name]
    first_year.plot(chart, filename=os.path.join(OUTPUT_DIR, '%i_%s.png' % (i, name)))

    i += 1

genders = table.group_by('gender')

for name in ['line_chart_simple', 'line_chart_complex']:
    chart = samples[name]
    genders.plot(chart, filename=os.path.join(OUTPUT_DIR, '%i_%s_multiples.png' % (i, name)))

    i += 1

genders_first_year = genders.where(lambda r: r['month'] < 73)

for name in ['column_chart_simple', 'column_chart_complex', 'bar_chart_simple', 'bar_chart_complex', 'scatter_chart']:
    chart = samples[name]
    genders_first_year.plot(chart, filename=os.path.join(OUTPUT_DIR, '%i_%s_multiples.png' % (i, name)))

    i += 1
