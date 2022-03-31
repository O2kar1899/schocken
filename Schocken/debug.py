from functools import wraps


def debug(fn):
    print("Entering debug")

    @wraps(fn)
    def debugger(*args, **kwargs):
        print("Entering debugger!")
        args_value_types = [(a, type(a)) for a in args]
        kwargs_values_types = [(k, v, type(v)) for k, v in kwargs.items()]
        print("Args: {args_value_types} ")
        print("Kwargs: {kwargs_values_types}")
        print("Fuction {fn.__name__} called ")
        fn_result = fn(*args, **kwargs)
        print("Funciton {fn.__name__} returns {fn__result__} ")
        return fn_result
    return debugger
