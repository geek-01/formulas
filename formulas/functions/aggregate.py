from . import raise_errors, flatten, wrap_func, Error
from statistics import median, variance

FUNCTIONS = {}


def xcount(*args):
    raise_errors(args)
    return len(list(flatten(args))) or [0]


FUNCTIONS['COUNT'] = wrap_func(xcount)


def xmedian(*args):
    raise_errors(args)
    data = tuple(list(flatten(args)))
    return median(data) or [0]


FUNCTIONS['MEDIAN'] = wrap_func(xmedian)


def xvar(*args):
    raise_errors(args)
    return variance(list(flatten(args))) or [0]


FUNCTIONS['VAR'] = wrap_func(xvar)
