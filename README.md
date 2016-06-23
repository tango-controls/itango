itango
======

An interactive Tango client.


Description
-----------

[ITango] is a [PyTango][PyTango] CLI based on [IPython][IPython].
It is designed to be used as an IPython profile.

It is available since PyTango 7.1.2 and has been moved to a separate
project since PyTango 9.2.0.


Requirements
------------

ITango is compatible with python 2 and 3. It requires:

- [IPython][IPython] >= 0.10
- [PyTango][PyTango] >= 9.2


Install
-------

ITango is available on [PyPI][ITango]:

    $ pip install itango


Usage
-----

ITango can be started using the `itango` script:

    $ itango  # Or itango3 if using python 3

or the `tango` profile:

    $ ipython --profile=tango


Features
--------

ITango works like a normal python console, but it provides a nice set of features from IPython:

- proper (bash-like) command completion
- automatic expansion of python variables, functions, types
- command history (with up/down arrow keys, %hist command)
- help system ( object? syntax, help(object))
- persistently store your favorite variables
- color modes

For a complete list checkout the [IPython web page][IPython].

It also adds set of [PyTango][PyTango] specific features:

- automatic import of Tango objects
- device and attribute name completion
- list tango devices, classes, servers
- customized tango error message
- database utilities

Check out the [documentation][Documentation] for more informations.


[ITango]: http://pypi.python.org/pypi/itango/
[PyTango]: https://github.com/tango-cs/PyTango
[IPython]: http://ipython.org/
[Documentation]: http://pythonhosted.org/itango
