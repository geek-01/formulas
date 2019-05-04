import math
import functools
import numpy as np
import datetime
import dateutil.parser as dparser
from . import (
    get_error, raise_errors, is_number, flatten, wrap_ufunc, wrap_func,
    replace_empty, Error
)

# noinspection PyDictCreation
FUNCTIONS = {}
_kw0 = dict(
    input_parser=lambda *a: a,
    args_parser=lambda *a: map(functools.partial(replace_empty, empty=''), a)
)


def find_day(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).day


FUNCTIONS['DAY'] = wrap_ufunc(find_day, **_kw0)


def find_month(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).month


FUNCTIONS['DAY'] = wrap_func(find_month, **_kw0)


def find_year(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).year


FUNCTIONS['DAY'] = wrap_func(find_year, **_kw0)
