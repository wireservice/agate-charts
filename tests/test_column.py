import csv
import os
import unittest

import agate

import agatecharts  # noqa: F401

TEST_FILENAME = '.test.png'


class TestColumnsChart(unittest.TestCase):
    def setUp(self):
        text_type = agate.Text()
        number_type = agate.Number()

        column_names = [
            'gender',
            'month',
            'median',
            'stdev',
            '1st',
            '3rd',
            '5th',
            '15th',
            '25th',
            '50th',
            '75th',
            '85th',
            '95th',
            '97th',
            '99th',
        ]
        column_types = [
            text_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
            number_type,
        ]

        with open('examples/heights.csv') as f:
            # Create a csv reader
            reader = csv.reader(f)

            # Skip header
            next(f)

            # Create the table
            self.table = agate.Table(reader, column_names, column_types)

        if os.path.exists(TEST_FILENAME):
            os.remove(TEST_FILENAME)

    def test_single(self):
        boys = self.table.where(lambda r: r['gender'] == 'male')
        boys.where(lambda r: r['month'] < 73)

        self.table.column_chart('month', 'median', filename=TEST_FILENAME)

        self.assertTrue(os.path.exists(TEST_FILENAME))

    def test_many(self):
        boys = self.table.where(lambda r: r['gender'] == 'male')
        boys.where(lambda r: r['month'] < 73)

        self.table.column_chart('month', ['median', 'stdev'], filename=TEST_FILENAME)

        self.assertTrue(os.path.exists(TEST_FILENAME))

    def test_multiples(self):
        genders = self.table.group_by('gender')

        genders.column_chart('month', 'median', filename=TEST_FILENAME)

        self.assertTrue(os.path.exists(TEST_FILENAME))
