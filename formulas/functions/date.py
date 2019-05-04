import dateutil.parser as dparser
from dateutil.parser import parse
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


def xnow():
    return datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")


FUNCTIONS['NOW'] = wrap_func(xnow)


def xtoday():
    return datetime.datetime.now().strftime("%Y-%m-%d")


FUNCTIONS['TODAY'] = wrap_func(xtoday)


def xisdate(date_str):
    try:
        parse(date_str, fuzzy=False)
        return "True"
    except ValueError:
        return "False"


FUNCTIONS['ISDATE'] = wrap_func(xisdate)


def xgetdate(date_str):
    try:
        date = dparser.parse(date_str, fuzzy=True)
        return date.date().strftime("%Y-%m-%d")
    except ValueError:
        raise Exception("Incorrect Date format!")


FUNCTIONS['DATE'] = wrap_func(xgetdate)
