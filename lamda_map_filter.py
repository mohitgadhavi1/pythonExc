'''
1. Lambda Function:
Lambda is a small, anonymous function in
 Python that is defined without a name.
It is a single expression that can be 
used wherever a function is required. 
Lambda functions are commonly used in
conjunction with higher-order functions
like map(), filter(), and reduce().
The syntax for creating a lambda 
function is:
lambda args: expression
'''
square = lambda x: x**2

'''
2. map() Function:
The map() function in Python is used to
apply a function to each item in an iterable
(e.g., list, tuple, etc.) and returns 
a new list with the modified items. 
The syntax for the map() function is:
map(function, iterable)
'''

numbers = [1, 2, 3, 4]
squares = map(lambda x:x**2,numbers)


'''
3. filter() Function:
The filter() function in Python is used to
filter out elements from an iterable based
on a given condition and returns a new 
list with the filtered items. The syntax 
for the filter() function is:
filter(function, iterable)
'''

numbers = [1, 2, 3, 4]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

