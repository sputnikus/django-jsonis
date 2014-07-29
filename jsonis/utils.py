import calendar
import datetime
import decimal
import sys
from json import JSONEncoder, JSONDecoder

PY3 = True if sys.version_info[0] == 3 else False


class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return calendar.timegm(o.timetuple())
        return super(MyJSONEncoder, self).default(o)


class MyJSONDecoder(JSONDecoder):
    def decode(self, s):
        if PY3:
            s = s.decode()
        return super(MyJSONDecoder, self).decode(s)


# Lazy evaluation utils
def lazyprop(fn, prefix='_lazy_'):
    """Lazy property decorator

    Property is evaluated only on first use and then cached in _lazy_*propname* attribute"""
    attr_name = prefix + fn.__name__

    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazyprop
