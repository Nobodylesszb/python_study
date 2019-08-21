from functools import wraps
import inspect


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values)
    parms.append(inspect.Parameter('debug',
                                   inspect.Parameter.KEYWORD_ONLY,
                                   default=False))

    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


"""
在于强制关键字参数很容易被添加到接受 *args 和 **kwargs 参数的函数中。 
通过使用强制关键字参数，它被作为一个特殊情况被挑选出来， 
并且接下来仅仅使用剩余的位置和关键字参数去调用这个函数时，这个特殊参数会被排除在外。 
也就是说，它并不会被纳入到 **kwargs 中去。
"""
