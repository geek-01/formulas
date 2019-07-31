from . import wrap_func

FUNCTIONS = {}

FUNCTIONS['STR'] = wrap_func(lambda input: str(input))


def xfloat(input):
    try:
        return float(input)
    except ValueError:
        raise Exception("Invalid value passed to function!")


FUNCTIONS['FLOAT'] = wrap_func(xfloat)
