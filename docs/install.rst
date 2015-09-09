============
Installation
============

Users
=====

If you only want to use fever, install it this way::

    pip install fever

Developers
==========

If you are a developer that also wants to hack on fever, install it this way::

    git clone git://github.com/onyxfish/fever.git
    cd fever
    mkvirtualenv fever
    pip install -r requirements.txt
    python setup.py develop
    tox

Supported platforms
===================

fever supports the following versions of Python:

* Python 2.6 (tests pass, but some dependencies claim not to support it)
* Python 2.7
* Python 3.2
* Python 3.3
* Latest `PyPy <http://pypy.org/>`_

It works anywhere `matplotlib <http://matplotlib.org/>`_ works.
