"""Main module for itango"""

import sys
from .itango import run, run_qt

run_qt() if 'qtconsole' in sys.argv else run()
