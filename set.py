# Exercise 3 (Sets)

# Use the set() constructor to create a set of 3 favorite beverages
beverages = set(["coffee", "tea", "juice"])
print("Beverages:", beverages)

# Add 2 more items to the beverages set
beverages.add("water")
beverages.add("soda")
print("After adding beverages:", beverages)

# Given the set below, check if microwave is present
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("Is microwave present?", "microwave" in mySet)

# Remove kettle from the set
mySet.discard("kettle")
print("After removing kettle:", mySet)

# Loop through the set
print("Looping through mySet:")
for item in mySet:
    print(item)

# Add elements from a list to a set
my_items = {"pen", "notebook", "eraser", "ruler"}
new_items = ["marker", "stapler"]
my_items.update(new_items)
print("Set after adding list items:", my_items)

# Join two sets, one with ages and the other with first names
ages = {21, 25, 30}
first_names = {"Lahm", "Yul", "Dhol"}
joined_sets = ages.union(first_names)
print("Joined sets:", joined_sets)
