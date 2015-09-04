#!/usr/bin/env python

import csv

from agate import Table, DateType, NumberType, TextType, Sum, StDev
import way

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

with open('heights.csv') as f:
    # Create a csv reader
    reader = csv.reader(f)

    # Skip header
    next(f)

    # Create the table
    table = Table(reader, COLUMNS)

line = way.Line('month', ['median', 'stdev'])

boys = table.where(lambda r: r['gender'] == 'male')
# boys.plot(line)
#
# boys.plot(way.Scatter('median', 'stdev'))

# first_year = boys.where(lambda r: r['month'] < 73)
# first_year.plot(way.Column('month', ['median', 'stdev', '25th']))

genders = table.group_by('gender')
genders.plot(line, filename='genders.png')
