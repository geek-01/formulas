import dateutil.parser as dparser
import datetime
from . import (
    wrap_func
)

# noinspection PyDictCreation
FUNCTIONS = {}


def find_day(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).day


FUNCTIONS['DAY'] = wrap_func(find_day)


def find_month(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).month


FUNCTIONS['MONTH'] = wrap_func(find_month)


def find_year(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).year


FUNCTIONS['YEAR'] = wrap_func(find_year)
FUNCTIONS['NOW'] = wrap_func(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))
FUNCTIONS['TODAY'] = wrap_func(datetime.datetime.now().strftime("%Y-%m-%d"))
