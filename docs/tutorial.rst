========
Tutorial
========

About agate-charts
==================

agate-charts is an extension for the  `agate <http://agate.readthedocs.org/>`_ data analysis library that adds support for quickly exploring data using charts. It does not create polished or publication-ready graphics. If you haven't used agate before, please read the `agate tutorial <http://agate.readthedocs.org/>`_ before reading this.

In this tutorial we will use agate-charts to explore a `time-series dataset from the EPA <http://ampd.epa.gov/ampd/>`_ documenting US greenhouse gas emissions for the month of June 2015.

Installing agate-charts
=======================

.. code-block:: bash

    pip install agate-charts

Getting setup
=============

Let's start by creating a clean workspace::

    mkdir agate_charts_tutorial
    cd agate_charts_tutorial

Now let's download the data::

    curl -L -O https://raw.githubusercontent.com/onyxfish/agate-charts/master/examples/epa-emissions-20150910.csv

You will now have a file named ``epa-emissions-20150910.csv`` in your ``agate_charts_tutorial`` directory.

.. note::

    agate-charts plays nicely with ipython and ipython notebook. If you prefer to go through this tutorial in that environment all the examples will work the same.

Loading the data
================

Now let's load the dataset into an :class:`.Table`. We'll use an :class:`.TypeTester` so that we don't have to specify every column, but we'll force the :code:` Date` column to be a date since it is in a known format.

.. code-block:: python

    import agate
    import agatecharts

    tester = agate.TypeTester(force={
        ' Date': agate.Date('%Y-%m-%d')
    })

    emissions = agate.Table.from_csv('examples/epa-emissions-20150910.csv', tester)

Now let's compute a few derived columns in order to make our charting easier. The first column will be the numerical day of the month. The latter three correct for an issue where the EPA has included empty columns instead of numerical zeroes.

.. code-block:: python

    emissions = emissions.compute([
        (agate.Formula(agate.Number(), lambda r: r[' Date'].day), 'day'),
        (agate.Formula(agate.Number(), lambda r: r[' SO2 (tons)'] or 0), 'so2'),
        (agate.Formula(agate.Number(), lambda r: r[' NOx (tons)'] or 0), 'nox'),
        (agate.Formula(agate.Number(), lambda r: r[' CO2 (short tons)'] or 0), 'co2')
    ])

Of course, for analysis purposes you should always be extremely cautious in assuming that blank fields are equivalent to zero. For the purposes of this tutorial, we will assume this is a valid transformation.

Your first chart
================

The emissions dataset includes data for several states. We'll look at the states individually later on, but to start out let's aggregate some totals:

.. code-block:: python

    days = emissions.group_by('day', key_type=agate.Number())
    day_totals = days.aggregate([
        ('so2', agate.Sum(), 'so2'),
        ('co2', agate.Sum(), 'co2'),
        ('nox', agate.Sum(), 'nox')
    ])

The :code:`day_totals` table now contains total counts of each type of emission. Note that we don't know if this data is comprehensive so we shouldn't assume these are national totals. (In fact, I know that they aren't for reasons that will become obvious shortly.)

Now let's render a line chart of the total :code:`co2`:

.. code-block: python

    day_totals.line_chart('day', 'co2')

Notice that :code:`line_chart` is a method on the :class:`.Table`. When agate-charts is imported, it automatically adds :class:`.TableCharts` methods to :class:`.Table` and the :class:`.TableSetCharts` methods to :class:`.TableSet`.

If all goes well, you should see a window popup containing this image:

.. image:: samples/line_chart_simple.png

You can also choose to render the image directly to disk, by passing the :code:`filename` argument:

.. code-block: python

    day_totals.line_chart('day', 'co2', filename='totals.png')

.. warning::

    agate-charts uses `matplotlib <http://matplotlib.org/>`_ to render charts. Matplotlib is a notoriously complicated and finicky piece of software. agate-charts attempts to abstract away all the messiest bits, but you may still have issues with charts not rendering on your particular platform. If the script hangs, or you don't see any output, try `specifying a rendering backend <http://matplotlib.org/faq/usage_faq.html#what-is-a-backend>`_ *before* importing agate-charts. This shouldn't normally be an issue if you're rendering to files.

Rendering multiple series
=========================

You may also want to render charts that compare to series of data. For instance, in this dataset the sulfur dioxide (:code:`so2`) and nitrogen oxide (:code:`nox`) amounts are on similar scales. Let's compare them with a bar chart:

.. code-block: python

    day_totals.bar_chart('day', ['so2', 'nox'])

.. image:: samples/bar_chart_complex.png

Small multiples
===============

TKTK

Saving charts
=============

TKTK

Where to go next
================

TKTK

Link to proof