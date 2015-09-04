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

boys = table.where(lambda r: r['gender'] == 'male')
table.line('month', 'median', filename='boys.png')

genders = table.group_by('gender')
genders.line('month', 'median')
