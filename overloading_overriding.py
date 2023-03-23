'''
In Python, both overloading and overriding are
supported, but they work slightly differently 
than in some other object-oriented programming 
languages.

Overloading in Python refers to the ability to 
define multiple methods or functions with the 
same name but different parameters. This allows
 you to call the same function name with different
arguments and get different results. Here's an
 example:
'''
class MyClass:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

obj = MyClass()
print(obj.add(1, 2))    # This will raise an error
print(obj.add(1, 2, 3)) # This will output 6


'''
In this example, we have defined two versions
 of the add method, one that takes two arguments
and another that takes three arguments. However,
 if we try to call the add method with two
 arguments, we will get an error, because
 Python does not support overloading based
 on the number of arguments alone.
'''

'''
Overriding in Python refers to the ability to
define a method in a subclass with the same name
as a method in the superclass, and have it
replace the implementation of the superclass
method. Here's an example:
'''
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

obj = Dog()
obj.speak() # This will output "The dog barks"

'''
In this example, we have defined a superclass
Animal with a speak method, and a subclass Dog
that overrides the speak method to provide a 
different implementation. When we create an
object of the Dog class and call the speak 
method, it will use the implementation
'''