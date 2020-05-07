# Creating Variables
# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5
y = "Hello World"
print(x)
print(y)
print("-------------------------------------------------------------------------------- Line 10")

# Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
print("-------------------------------------------------------------------------------- Line 17")

# String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Remember that variable names are case-sensitive

# Assign Value to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("-------------------------------------------------------------------------------- Line 54")

# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)
print("-------------------------------------------------------------------------------- Line 62")

# Output Variables
# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character:

x = "awesome"
print("Python is " + x)
print("-------------------------------------------------------------------------------- Line 70")

# You can also use the + character to add a variable to another variable:

x = "Python is "
y = "awesome"
z =  x + y
print(z)
print("-------------------------------------------------------------------------------- Line 78")

# For numbers, the + character works as a mathematical operator:

x = 7
y = 5
print(x + y)
print("-------------------------------------------------------------------------------- Line 85")

# Arithmetic Operations
# +	Addition
z = x + y
# -	Subtraction
z = x - y
# *	Multiplication
z = x * y
# /	Division
z = x / y
# %	Modulus
z = x % y
print(z)
# ** Exponentiation
z = x ** y
# // Floor division
z = x // y

print("-------------------------------------------------------------------------------- Line 104")

# Printing string and integer (or float) in the same line

print ("i am" ,  x)
print ("i am " + str(x))
print ("i am %s " % x)

# If you try to combine a string and a number, Python will give you an error:

x = 5
y = "John"
# print(x + y)
print("-------------------------------------------------------------------------------- Line 117")



# types of variables

x = "Hello World"	#str
x = 20	#int
x = 20.5	#float
print(type(x))
x = True	#bool
print("-------------------------------------------------------------------------------- Line 128")

# Type Conversion

x = 1    # int
y = 2.8  # float

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)


print(a)
print(b)


print(type(a))
print(type(b))

