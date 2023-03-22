#In Python, a module is a file containing Python definitions and statements that can be imported and used in another Python program. A script, on the other hand, is a standalone program that can be executed from the command line or by double-clicking the file.

#Here's an example of a Python module:

# mymodule.py
def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y
#===========================================

#This module contains two functions that can be imported and used in another Python program:

# main.py
import mymodule

result1 = mymodule.add_numbers(5, 3)
print(result1)

result2 = mymodule.subtract_numbers(10, 4)
print(result2)

#=============================================

#Here's an example of a Python script:

# myscript.py
def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()

#This script defines a main function that prints "Hello, world!" to the console. The if __name__ == "__main__": block ensures that the main() function is only executed when the script is run directly, and not when it is imported as a module. To run the script, you can simply execute it from the command line