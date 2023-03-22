'''
Decorators:
Decorators are functions that modify the
 behavior of other functions without changing
their source code. They take a function 
 as input and return a new function that 
adds some additional functionality to 
 the original function.
'''

def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

# Calling the decorated function
say_hello()
