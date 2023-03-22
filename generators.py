'''
Generators:
Generators are functions that can be used to 
create iterators. They use the yield keyword 
to return a value from the function,
 but instead of returning the result and 
 terminating the function, it saves its 
 state and waits for the next call to
continue execution from where it left off.
This allows for a more memory-efficient
 and lazy evaluation of results.
'''
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator to print the first 10 numbers of the Fibonacci sequence
for i in fibonacci_generator(10):
    print(i)
