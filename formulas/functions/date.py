import math
import functools
import numpy as np
import datetime
from . import wrap_ufunc, Error, replace_empty, XlError, value_return
import dateutil.parser as dparser
from . import (
    get_error, raise_errors, is_number, flatten, wrap_ufunc, wrap_func,
    replace_empty, Error
)

# noinspection PyDictCreation
FUNCTIONS = {}


def _str(text):
    if isinstance(text, bool):
        return str(text).upper()
    return str(text)


_kw1 = dict(
    input_parser=lambda text: [_str(text)], return_func=value_return,
    args_parser=lambda *a: map(functools.partial(replace_empty, empty=''), a),
)


def find_day(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).day


FUNCTIONS['DAY'] = wrap_ufunc(find_day, **_kw1)


def find_month(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).month


FUNCTIONS['DAY'] = wrap_func(find_month, **_kw1)


def find_year(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).year


FUNCTIONS['DAY'] = wrap_func(find_year, **_kw1)
