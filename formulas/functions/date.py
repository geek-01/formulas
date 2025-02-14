import dateutil.parser as dparser
from datetime import datetime
from dateutil.parser import parse
import datetime
from . import (
    wrap_func
)

# noinspection PyDictCreation
FUNCTIONS = {}

def parse_date_fromat(date_str):
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')

def find_day(date_str):
    parse_date_fromat(date_str)
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).day


FUNCTIONS['DAY'] = wrap_func(find_day)


def find_month(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).month


FUNCTIONS['MONTH'] = wrap_func(find_month)


def find_year(date_str):
    return dparser.parse(date_str, fuzzy=True, dayfirst=True).year


FUNCTIONS['YEAR'] = wrap_func(find_year)


def xnow():
    return datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")


FUNCTIONS['NOW'] = wrap_func(xnow)


def xtoday():
    return datetime.now().strftime("%Y-%m-%d")


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


def xdateadd(date_part, interval, date):
    try:
        date = dparser.parse(date)
        if date_part.lower() == 'day':
            date += datetime.timedelta(days=int(interval))
            return date.strftime("%Y-%m-%d")
        elif date_part.lower() == 'month':
            return datetime.date(date.year, date.month + int(interval), date.day).strftime("%Y-%m-%d")
        elif date_part.lower() == 'year':
            return datetime.date(date.year + int(interval), date.month, date.day).strftime("%Y-%m-%d")
        return "Require value for argument interval"
    except ValueError:
        raise Exception("Invalid date string!")


FUNCTIONS['DATEADD'] = wrap_func(xdateadd)


def xmakedate(year, month, day):
    try:
        return datetime.date(year=int(year), month=int(month), day=int(day)).strftime("%B %d, %Y")
    except ValueError:
        raise Exception("Invalid date string!")


FUNCTIONS['MAKEDATE'] = wrap_func(xmakedate)


def xmakedatetime(date, time):
    try:
        return dparser.parse(date + ' ' + time).strftime("%Y-%m-%d %I:%M:%S %p")
    except ValueError as err:
        raise Exception("Invalid date string! {}".format(str(err)))


FUNCTIONS['MAKEDATETIME'] = wrap_func(xmakedatetime)


def xmaketime(hour, minute, second):
    try:
        return datetime.time(hour=int(hour), minute=int(minute), second=int(second)).strftime("%I:%M:%S %p")
    except ValueError as err:
        raise Exception("Invalid date string! {}".format(str(err)))


FUNCTIONS['MAKETIME'] = wrap_func(xmaketime)