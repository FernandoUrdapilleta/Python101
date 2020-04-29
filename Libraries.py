# coding=utf-8
import string
from datetime import datetime  # Info about library https://docs.python.org/3/library/datetime.html
#from datetime import *        #would have a similar effect as above line but imports all the datetime module
import calendar as c
'''
A function is a block of organized, reusable code that is used to perform a single, related action.
Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc.
but you can also create your own functions. These functions are called user-defined functions.

Syntax
def functionName(parameter1, parameter2, parameterN):
   "function description"
   statements
   return [expression]
'''

def absolute_value(num):
    """
    This function returns the absolute
    value of the entered number
    """

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))
# print(absolute_value.__doc__)     #__doc__ atribute returns the descroption of the function

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("\nHello, " + name + ". Good morning!")

greet('Paul')
print(greet('Mary'))                #Prints "None" as there's no value being returned, this is by default


'''
Depending on where the variable is being defined, then variable could be local or global
If defined within the function, it's a local variable and will only exist while the function is being executed/
Local variables cannot be used outside of the function
'''

def my_func():
	x = 10
	print("\nValue inside function: " + str(x))

#x += 1
x = 20
my_func()
print("Value outside function: " + str(x))

"""
Libraries
A (software) library is a collection of files (called modules) that contains functions for use by other programs

Use 'import' to load a library module into a program’s memory (look at the top of the code)
Then refer to things from the module as module_name.thing_name.
    - Python uses . to mean “part of”.
    
Library of Python libraries: https://docs.python.org/3/library/
"""

#help(string)
print("\n")
print('The lower ascii letters are', string.ascii_lowercase)
print(string.capwords('capitalise this sentence please.'))

#help(datetime)
"""
To import specific items from a library module, to shorten programs:
Use from ... import ... to load only specific items from a library module.

Then refer to them directly without library name as prefix. Below, we would need to use datetime.datetime()
to create object datetime otherwise
"""
print("\n")
x = datetime(2020, 2, 1)
print(x)
print(x.strftime("%A" + " " + "%d" +', '+ "%B" + ", " + "%Y"))     #strftime() method has many other directives to print in different formats

date_object = datetime.strptime('2018-04-29T17:45:25Z', '%Y-%m-%dT%H:%M:%SZ')
same_object = datetime(2018, 4, 29, 17, 45, 25)

print(date_object)
print(same_object)

"""
Create an alias for a library module when importing it to shorten programs.
Use import ... as ... to give a library a short alias while importing it.
Then refer to items in the library using that shortened name:

import string as s

print(s.capwords('capitalise this sentence again please.'))
"""
print("\n")
def leapYear(year):
    if c.isleap(year) :
        print("This is a leap year")
    else:
        print("This is not a leap year")

print("2019: ")
leapYear(2019)
print("\n")
print("2020: ")
leapYear(2020)