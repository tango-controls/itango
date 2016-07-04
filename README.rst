ITango
======

An interactive Tango client.


Description
-----------

ITango_ is a PyTango_ CLI based on IPython_.
It is designed to be used as an IPython profile.

It is available since PyTango 7.1.2 and has been moved to a separate
project since PyTango 9.2.0.


Requirements
------------

ITango is compatible with python 2 and 3. It requires:

-  IPython_ >= 1.0
-  PyTango_ >= 9.2

.. note:: For IPython_ < 1.0 compatibilty, use `ITango 0.1.1`_.


Install
-------

ITango is available on `PyPI <ITango_>`__::

    $ pip install itango


Usage
-----

ITango can be started using the ``itango`` script::

    $ itango  # Or itango3 if using python 3

or the ``tango`` profile::

    $ ipython --profile=tango


Features
--------

ITango works like a normal python console, but it provides a nice set of
features from IPython:

-  proper (bash-like) command completion
-  automatic expansion of python variables, functions, types
-  command history (with up/down arrow keys, %hist command)
-  help system ( object? syntax, help(object))
-  persistently store your favorite variables
-  color modes

For a complete list checkout the `IPython web page <IPython_>`__.

It also adds set of PyTango_ specific features:

-  automatic import of Tango objects
-  device and attribute name completion
-  list tango devices, classes, servers
-  customized tango error message
-  database utilities

Check out the `documentation <Documentation_>`__ for more informations.

.. _IPython: http://ipython.org/
.. _ITango: http://pypi.python.org/pypi/itango/
.. _ITango 0.1.1: https://pypi.python.org/pypi/itango/0.1.1
.. _PyTango: https://github.com/tango-cs/PyTango
.. _Documentation: http://pythonhosted.org/itango
