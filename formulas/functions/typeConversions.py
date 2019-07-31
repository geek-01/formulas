from . import raise_errors, flatten, wrap_func, Error

FUNCTIONS = {}

FUNCTIONS['STR'] = wrap_func(lambda input: str(input))


def xint(input):
    try:
        return int(input)
    except ValueError:
        raise Exception("Invalid value passed to function!")


FUNCTIONS['INT'] = wrap_func(xint)


def xfloat(input):
    try:
        return float(input)
    except ValueError:
        raise Exception("Invalid value passed to function!")


FUNCTIONS['FLOAT'] = wrap_func(xfloat)
