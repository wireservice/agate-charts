============
Installation
============

Users
=====

If you only want to use agate-charts, install it this way::

    pip install agate-charts

Developers
==========

If you are a developer that also wants to hack on agate-charts, install it this way::

    git clone git://github.com/wireservice/agate-charts.git
    cd agate-charts
    mkvirtualenv agate-charts
    pip install -r requirements.txt
    python setup.py develop
    tox

Supported platforms
===================

agate-charts supports the following versions of Python:

* Python 2.6 (tests pass, but some dependencies claim not to support it)
* Python 2.7
* Python 3.2
* Python 3.3
* Latest `PyPy <http://pypy.org/>`_

It works anywhere `matplotlib <http://matplotlib.org/>`_ works.
