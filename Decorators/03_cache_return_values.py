# Implement a decorator that caches the return values of a function, so that when it is called with the same arguments, the cached value is returned instead of re-executing the function

import time

def cache(func):
    cached_value = {}
    def wrapper(*args, **kwargs):
        if args in cached_value:
            return cached_value[args]
        result = func(*args, **kwargs)
        cached_value[args] = result
        return result
    return wrapper


@cache
def long_returning_function(a, b):
    time.sleep(4)
    return a+b

print(long_returning_function(2,3))
print(long_returning_function(2,3))
print(long_returning_function(10,3))
print(long_returning_function(5,2))
print(long_returning_function(10,3))