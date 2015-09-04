#!/usr/bin/env python

import agate

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

def _line_table(table, x_column_name, y_column_name, title=None):
    plt.plot(table.columns[x_column_name], table.columns[y_column_name])

    plt.xlabel(x_column_name)
    plt.ylabel(y_column_name)

    if title:
        plt.title(title)

def _line_tableset(tableset, x_column_name, y_column_name):
    for i, (key, table) in enumerate(tableset.items()):
        plt.subplot(1, 2, i)
        # plt.tight_layout(pad=0, w_pad=3)

        _line_table(table, x_column_name, y_column_name, title=key)

def line(source, x_column_name, y_column_name, filename=None):
    args = (source, x_column_name, y_column_name)

    if isinstance(source, agate.TableSet):
        _line_tableset(*args)
    else:
        _line_table(*args)

    plt.legend()

    if filename:
        plt.savefig(filename)
    else:
        plt.show()
