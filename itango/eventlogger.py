# -----------------------------------------------------------------------------
# This file is part of ITango (http://pypi.python.org/pypi/itango)
#
# Copyright 2006-2012 CELLS / ALBA Synchrotron, Bellaterra, Spain
# Copyright 2013-2014 European Synchrotron Radiation Facility, Grenoble, France
#
# Distributed under the terms of the GNU Lesser General Public License,
# either version 3 of the License, or (at your option) any later version.
# See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from __future__ import print_function

import re
import io

LENGTHS = 4, 30, 18, 20, 12, 16
COLUMNS = 'ID', 'Device', 'Attribute', 'Value', 'Quality', 'Time'

TEMPLATE = ' '.join('{%d:%d}' % x for x in enumerate(LENGTHS))
TITLE = TEMPLATE.format(*COLUMNS) + '\n' + ' '.join('-' * l for l in LENGTHS)


class EventLogger(object):

    def __init__(self, capacity=100000, pager=None):
        self._capacity = capacity
        self._pager = pager
        self._records = []

    def push_event(self, evt):
        attr_name = evt.attr_name
        dev, sep, attr = attr_name.rpartition('/')
        if dev.startswith("tango://"):
            dev = dev[8:]
        if dev.count(":"):
            # if it has tango host
            host, sep, dev = dev.partition('/')
        else:
            host = "-----"
        evt.host = host
        evt.dev_name = dev
        evt.s_attr_name = attr
        self._records.append(evt)
        over = len(self._records) - self._capacity
        if over > 0:
            self._records = self._records[over:]

    def model(self):
        return self

    def getEvents(self):
        return self._records

    def show(self, dexpr=None, aexpr=None):
        if dexpr is not None:
            dexpr = re.compile(dexpr, re.IGNORECASE)
        if aexpr is not None:
            aexpr = re.compile(aexpr, re.IGNORECASE)

        class StringIO(io.StringIO):
            def write(self, value):
                if isinstance(value, bytes):
                    value = value.decode()
                io.StringIO.write(self, value)

        s = StringIO()

        print(TITLE, file=s)

        for i, r in enumerate(self._records):
            if dexpr is not None and not dexpr.match(r.dev_name):
                continue
            if aexpr is not None and not aexpr.match(r.s_attr_name):
                continue
            if r.err:
                v = r.errors[0].reason
                q = 'ERROR'
                ts = r.reception_date.strftime("%H:%M:%S.%f")
            else:
                v = str(r.attr_value.value)
                q = str(r.attr_value.quality)
                ts = r.attr_value.time.strftime("%H:%M:%S.%f")
            args = i, r.dev_name, r.s_attr_name, v, q, ts
            print(TEMPLATE.format(*args), file=s)
        s.seek(0)
        if self._pager is None:
            print(s.read())
        else:
            self._pager(s.read())
