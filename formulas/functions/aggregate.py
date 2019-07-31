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


def mean(x):
    return sum(x) / len(x)


def xcovar(exp1, exp2):
    covar = [(exp1[i] - mean(exp1)) * (exp2[i] - mean(exp2))
             for i in range(len(exp1))]
    return sum(covar) / (len(covar) - 1) or [0]


FUNCTIONS['COVAR'] = wrap_func(xcovar)
