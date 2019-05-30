import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args,**kwarges):
            if level == 'warn':
                logging.warn("%s is running" %func.__name__)
            return func(*args)
        return wrapper
    return decorator

@use_logging(level = "warn")
def foo(name = 'foo'):
    print(' i am %s' % name)

foo()

"""
output
WARNING:root:foo is running
 i am foo
"""