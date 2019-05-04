import dateutil.parser as dparser
import functools
from . import wrap_ufunc, Error, replace_empty, XlError, value_return
from . import (
    wrap_ufunc, wrap_func
)

# noinspection PyDictCreation
FUNCTIONS = {}


def _str(text):
    if isinstance(text, bool):
        return str(text).upper()
    return str(text)


def find_day(date_str):
    return _str(dparser.parse(_str(date_str), fuzzy=True, dayfirst=True).day)


_kw1 = dict(
    input_parser=lambda text: [_str(text)], return_func=value_return,
    args_parser=lambda *a: map(functools.partial(replace_empty, empty=''), a),
)

FUNCTIONS['DAY'] = wrap_ufunc(find_day, **_kw1)


def find_month(date_str):
    return _str(dparser.parse(date_str, fuzzy=True, dayfirst=True).month)


FUNCTIONS['MONTH'] = wrap_func(find_month, **_kw1)


def find_year(date_str):
    return _str(dparser.parse(_str(date_str), fuzzy=True, dayfirst=True).year)


FUNCTIONS['YEAR'] = wrap_func(find_year, **_kw1)
