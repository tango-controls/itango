"""Main module for itango"""

import sys
from itango import run, run_qt

if 'qtconsole' in sys.argv:
    run_qt()
else:
    run()
