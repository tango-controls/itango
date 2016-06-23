"""Sphinx configuration for itango documentation."""

import sys
import os


# Extensions

sys.path.append(os.path.abspath('sphinxext'))
extensions = ['ipython_console_highlighting',
              'tango_console_highlighting']

# Configuration

master_doc = 'itango'
rst_epilog = """\
.. _Tango: http://www.tango-controls.org/
.. _IPython: http://ipython.org/
.. _ITango: https://pypi.python.org/pypi/itango/
"""

# Data

project = u'itango'
copyright = u'2016, Tango Controls'
