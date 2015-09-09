===============
fever |release|
===============

About
=====

.. include:: ../README

Why fever?
==========

* A clean, readable API.
* Automatically infers good defaults from your data.
* An order of magnitude simpler than the alternatives.
* Fast, fast, fast.

Installation
============

Users
-----

If you only want to use fever, install it this way::

    pip install fever

Developers
----------

If you are a developer that also wants to hack on fever, install it this way::

    git clone git://github.com/onyxfish/fever.git
    cd fever
    mkvirtualenv fever
    pip install -r requirements.txt
    python setup.py develop
    tox

Supported platforms
-------------------

fever supports the following versions of Python:

* Python 2.6+
* Python 3.2+
* Latest `PyPy <http://pypy.org/>`_

It works wherever `matplotlib <http://matplotlib.org/>`_ works.

Table of contents
=================

.. toctree::
    :maxdepth: 2

    tutorial
    api

Authors
=======

.. include:: ../AUTHORS

License
=======

.. include:: ../COPYING

Changelog
=========

.. include:: ../CHANGELOG

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
