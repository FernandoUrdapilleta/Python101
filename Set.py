# Set
# Set is a collection which is unordered and unindexed. No duplicate members.

thisset = {"apple", "banana", "cherry"}
print(thisset)
print("-------------------------------------------------------------------------------- Line 6")

# Check if "banana" is present in the set:

print("banana" in thisset)
print("-------------------------------------------------------------------------------- Line 11")

# Note: Once a set is created, you cannot change its items, but you can add new items.
#
# Add Items
# Add an item to a set, using the add() method:

thisset.add("orange")
print(thisset)
print("-------------------------------------------------------------------------------- Line 20")

# Add multiple items to a set, using the update() method:

thisset.update(["orange", "mango", "grapes"])
print(thisset)
print("-------------------------------------------------------------------------------- Line 26")

# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print("-------------------------------------------------------------------------------- Line 32")

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

thisset.remove("banana")
print(thisset)
