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


def find_day(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).day


FUNCTIONS['Day'] = wrap_ufunc(find_day)


def find_month(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).month


FUNCTIONS['Month'] = wrap_func(find_month)


def find_year(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).year


FUNCTIONS['Year'] = wrap_func(find_year)
