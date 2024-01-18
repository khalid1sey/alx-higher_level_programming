0x02. Python - import & modules

Python programming is awesome for several reasons:

    Readability: Python has a clean and easy-to-read syntax, making it simple to write and understand code.

    Versatility: Python can be used for a wide range of applications, including web development, data analysis, artificial intelligence, scientific computing, and more.

    Large Standard Library: Python comes with a comprehensive standard library that provides ready-to-use modules and functions for various tasks, saving development time and effort.

    Third-Party Libraries: Python has a vast ecosystem of third-party libraries and frameworks, allowing developers to leverage existing tools and solutions to accelerate development.

    Cross-Platform Compatibility: Python is available on multiple platforms, including Windows, macOS, and Linux, making it highly portable.

To import functions from another file in Python, you can use the import statement. Here's an example:
python

# File: mymodule.py
def greeting(name):
    print("Hello, " + name + "!")

# File: main.py
import mymodule

mymodule.greeting("Alice")

In the above example, the greeting() function is defined in the mymodule.py file. To use this function in another file (main.py), you import the mymodule module using the import statement. You can then access the greeting() function using the module name and the function name.

To create a module in Python, you simply define functions, classes, or variables in a .py file. This file can then be imported as a module in other Python scripts.

The dir() function in Python returns a list of names in the current namespace or the names of an object's attributes. It can be used to explore the contents of a module, class, or object. Here's an example:
python

import math

print(dir(math))  # List attributes of the math module

When executing a Python script, the code is executed line by line. However, sometimes you may want to prevent certain code from being executed when the script is imported as a module. To achieve this, you can use the if __name__ == "__main__": condition. Code within this block will only execute if the script is run directly, but not if it is imported. Here's an example:
python

# File: mymodule.py
def greeting(name):
    print("Hello, " + name + "!")

if __name__ == "__main__":
    # Code here will only execute when the script is run directly
    greeting("Alice")

To use command-line arguments with your Python programs, you can access them through the sys.argv list provided by the sys module. Here's an example:
python

import sys

# Access command-line arguments
script_name = sys.argv[0]
argument1 = sys.argv[1]
argument2 = sys.argv[2]

print("Script Name:", script_name)
print("Argument 1:", argument1)
print("Argument 2:", argument2)

In the above example, sys.argv[0] corresponds to the script name itself, and subsequent elements represent the command-line arguments passed to the script.

These are some of the fundamental concepts related to Python programming. Python's simplicity, versatility, and extensive ecosystem make it a popular choice among developers for a wide range of applications.


0. Import a simple function from a simple file
mandatory

Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

    You have to use print function with string format to display integers
    You have to assign:
        the value 1 to a variable called a
        the value 2 to a variable called b
        and use those two variables as arguments when calling the functions add and print
    a and b must be defined in 2 different lines: a = 1 and another b = 2
    Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
    You can only use the word add_0 once in your code
    You are not allowed to use * for importing or __import__
    Your code should not be executed when imported - by using __import__, like the example below


1. My first toolbox!
mandatory

Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

    Do not use the function print (with string format to display integers) more than 4 times
    You have to define:
        the value 10 to a variable a
        the value 5 to a variable b
        and use those two variables only, as arguments when calling functions (including print)
    a and b must be defined in 2 different lines: a = 10 and another b = 5
    Your program should call each of the imported functions. See example below for format
    the word calculator_1 should be used only once in your file
    You are not allowed to use * for importing or __import__
    Your code should not be executed when imported
