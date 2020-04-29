# Dictionary
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print("-------------------------------------------------------------------------------- Line 11")

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

x = thisdict["model"]
print(x)
print("-------------------------------------------------------------------------------- Line 18")

# There is also a method called get() that will give you the same result:

x = thisdict.get("model")
print(x)
print("-------------------------------------------------------------------------------- Line 24")

# Change the "year" to 2018:

thisdict["year"] = 2018
x = thisdict["year"]
print(x)
print("-------------------------------------------------------------------------------- Line 31")

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() method.

print(len(thisdict))
print("-------------------------------------------------------------------------------- Line 43")

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict["color"] = "red"
print(thisdict)
print("-------------------------------------------------------------------------------- Line 49")

# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:

thisdict.pop("model")
print(thisdict)
print("-------------------------------------------------------------------------------- Line 56")

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.popitem()
print(thisdict)
print("-------------------------------------------------------------------------------- Line 62")

# The clear() method empties the dictionary:

thisdict.clear()
print(thisdict)
print("-------------------------------------------------------------------------------- Line 68")

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

mydict = thisdict.copy()
print(mydict)
print("-------------------------------------------------------------------------------- Line 76")

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Or, if you want to nest three dictionaries that already exists as dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}