# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1

print("------------------------------------------------------------------------------------ Line 10")

# Note: remember to increment i, or else the loop will continue forever.
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("------------------------------------------------------------------------------------ Line 26")

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("------------------------------------------------------------------------------------ Line 38")

# For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("------------------------------------------------------------------------------------ Line 49")

# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)

print("------------------------------------------------------------------------------------ Line 60")

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("------------------------------------------------------------------------------------ Line 72")

# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("------------------------------------------------------------------------------------ Line 82")

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)

print("------------------------------------------------------------------------------------ Line 90")

# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

print("------------------------------------------------------------------------------------ Line 98")

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

print("------------------------------------------------------------------------------------ Line 107")

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("------------------------------------------------------------------------------------ Line 118")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("------------------------------------------------------------------------------------ Line 132")

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

print("------------------------------------------------------------------------------------ Line 148")

# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

print("------------------------------------------------------------------------------------ Line 155")

# Loop through both keys and values, by using the items() function:

for x, y in thisdict.items():
  print(x, y)

print("------------------------------------------------------------------------------------ Line 162")

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Access Items
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


