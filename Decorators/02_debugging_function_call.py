# Create a decorator to print the fuction name and the values of the arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    
    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Rishi", greeting="Hii")

@debug
def hello():
    print("Hello")

hello()
