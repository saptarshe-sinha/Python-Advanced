'''
    Decorators allows us to modify or extend the behavior of functions or methods 
    without changing their actual code
'''

# Write a decorator that measures the time a function takes to execute

import time

# toll booth 
def timer(func):
    def wrapper(*args, **kwargs):  # arguments & keyword arguments
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

# wrapper fucntion is the function that replaces the original function when the decorator is applied

@timer
def example_function(n):
    time.sleep(n)

example_function(2)