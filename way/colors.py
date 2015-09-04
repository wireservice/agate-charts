#!/usr/bin/env python

def ColorGenerator():
    colors = ['r', 'g', 'b']
    i = 0

    while i < len(colors):
        yield colors[i]

        i += 1
