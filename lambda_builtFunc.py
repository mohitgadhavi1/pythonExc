'''
A lambda function is a small, anonymous function in Python
that can be defined inline and assigned to a variable.
In contrast, a built-in function is a function that is
already defined in Python and can be called directly
without the need for defining it. Here are some key
differences between the two:

Syntax: A lambda function is defined using the lambda
keyword, followed by a comma-separated list of input 
arguments, a colon, and the expression to be evaluated.
A built-in function is called using its name, followed 
by any required input arguments within parentheses.

Scope: A lambda function is defined within the scope of 
the expression in which it is defined and can only access
 variables in its local scope and its enclosing scope. 
 A built-in function is defined in the global scope and 
 can access any variables that are in scope at the time 
 it is called.

Return value: A lambda function automatically returns the 
value of the expression it evaluates, while a built-in 
function returns a value specified in its definition.

Complexity: Lambda functions are typically used for simple,
 one-line expressions, while built-in functions can be much 
 more complex and may have a large number of input arguments.

Here is an example of a lambda function and a built-in 
function that accomplish the same task of doubling a given
 number:
'''
# Using a lambda function
double = lambda x: x * 2
result = double(5)
print(result)  # Output: 10

# Using a built-in function
result = pow(5, 2)
print(result)  # Output: 10
