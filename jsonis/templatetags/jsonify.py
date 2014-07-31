from django.conf import settings
from django.template import Library

from ..utils import MyJSONEncoder, PY3

register = Library()

if PY3:
    encoder = MyJSONEncoder(ensure_ascii=False)
else:
    encoder = MyJSONEncoder(ensure_ascii=False,
                            encoding=settings.DEFAULT_CHARSET)


@register.filter
def jsonify(obj):
    return encoder.encode(obj)
