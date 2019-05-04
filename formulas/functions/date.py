import dateutil.parser as dparser
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
    return dparser.parse(_str(date_str), fuzzy=True, dayfirst=True).day


FUNCTIONS['DAY'] = wrap_ufunc(find_day)


def find_month(date_str):
    return dparser.parse(_str(date_str), fuzzy=True, dayfirst=True).month


FUNCTIONS['MONTH'] = wrap_func(find_month)


def find_year(date_str):
    return dparser.parse(_str(date_str), fuzzy=True, dayfirst=True).year


FUNCTIONS['YEAR'] = wrap_func(find_year)
