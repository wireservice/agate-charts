#!/usr/bin/env python

import csv
import os

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import agate
import way

TEST_FILENAME = '.test.png'

class TestLineChart(unittest.TestCase):
    def setUp(self):
        text_type = agate.TextType()
        number_type = agate.NumberType()

        columns = (
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
            self.table = agate.Table(reader, columns)

        if os.path.exists(TEST_FILENAME):
            os.remove(TEST_FILENAME)

    def test_single(self):
        line_chart = way.Lines('month', 'median')
        self.table.plot(line_chart, filename=TEST_FILENAME)

        self.assertTrue(os.path.exists(TEST_FILENAME))

    def test_many(self):
        line_chart = way.Lines('month', ['median', 'stdev'])
        self.table.plot(line_chart, filename=TEST_FILENAME)

        self.assertTrue(os.path.exists(TEST_FILENAME))

    def test_multiples(self):
        genders = self.table.group_by('gender')

        line_chart = way.Lines('month', 'median')
        genders.plot(line_chart, filename=TEST_FILENAME)

        self.assertTrue(os.path.exists(TEST_FILENAME))
