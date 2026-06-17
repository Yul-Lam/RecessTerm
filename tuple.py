# Exercise 2 (Tuples)

x = ("samsung", "iphone", "tecno", "redmi")

# Output your favorite phone brand
favorite_brand = x[0]
print("Favorite phone brand:", favorite_brand)

# Use negative indexing to print the 2nd last item
print("2nd last item:", x[-2])

# Update "iphone" to "itel" by converting to a list and back to a tuple
phones_list = list(x)
phones_list[1] = "itel"
x = tuple(phones_list)
print("After updating iphone to itel:", x)

# Add "Huawei" to the tuple
x = x + ("Huawei",)
print("After adding Huawei:", x)

# Loop through the tuple
print("Looping through phones:")
for phone in x:
    print(phone)

# Remove/delete the first item in the tuple
x = x[1:]
print("After removing first item:", x)

# Create a tuple of cities in Uganda using the tuple() constructor
cities = tuple(["Kampala", "Jinja", "Fort Portal", "Gulu", "Mbale"])
print("Cities tuple:", cities)

# Unpack the tuple
city1, city2, city3, city4, city5 = cities
print("Unpacked cities:", city1, city2, city3, city4, city5)

# Print the 2nd, 3rd and 4th cities using a range of indexes
print("2nd, 3rd and 4th cities:", cities[1:4])

# Join two tuples containing first names and second names
first_names = ("Amirah", "John Blaq", "Windy")
second_names = ("Eden", "Brown", "White")
joined_names = first_names + second_names
print("Joined tuples:", joined_names)

# Create a tuple of colors and multiply it by 3
colors = ("red", "green", "blue")
colors_repeated = colors * 3
print("Colors repeated 3 times:", colors_repeated)

# Count how many times 8 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_eight = thistuple.count(8)
print("Number of times 8 appears:", count_of_eight)
