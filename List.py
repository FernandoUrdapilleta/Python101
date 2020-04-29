# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Lists
thislist = ["apple", "banana", "cherry"]

# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print("-------------------------------------------------------------------------------- Line 15")

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print("-------------------------------------------------------------------------------- Line 22")

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print("-------------------------------------------------------------------------------- Line 31")

# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to "orange":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print("-------------------------------------------------------------------------------- Line 42")

# By leaving out the end value, the range will go on to the end of the list:
# This example returns the items from "cherry" and to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
print("-------------------------------------------------------------------------------- Line 49")

# Add Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("-------------------------------------------------------------------------------- Line 57")

# To add an item at the specified index, use the insert() method:
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print("-------------------------------------------------------------------------------- Line 65")

# Remove Item
# The remove() method removes the specified item:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("-------------------------------------------------------------------------------- Line 73")

# The pop() method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("-------------------------------------------------------------------------------- Line 80")

# The del keyword removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print("-------------------------------------------------------------------------------- Line 87")

# The clear() method empties the list:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("-------------------------------------------------------------------------------- Line 94")

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print("-------------------------------------------------------------------------------- Line 104")

# Join two list:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

