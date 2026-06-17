# Exercise 5 (Dictionaries)

Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# Print the value of the shoe size
print("Shoe size:", Shoes["size"])

# Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("After brand change:", Shoes)

# Add a key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("After adding type:", Shoes)

# Return a list of all keys in the dictionary
print("Keys:", list(Shoes.keys()))

# Return a list of all values in the dictionary
print("Values:", list(Shoes.values()))

# Check if the key "size" exists in the dictionary
print("Does 'size' exist?", "size" in Shoes)

# Loop through the dictionary
print("Looping through Shoes:")
for key, value in Shoes.items():
    print(key, "=", value)

# Remove "color" from the dictionary
Shoes.pop("color", None)
print("After removing color:", Shoes)

# Empty the dictionary
Shoes.clear()
print("After emptying:", Shoes)

# Write a dictionary of your choice and make a copy of it
person = {
    "name": "Messi",
    "age": 24,
    "city": "Kampala"
}
person_copy = person.copy()
print("Person:", person)
print("Person copy:", person_copy)

# Show nested dictionaries
school = {
    "student1": {"name": "Enzo", "grade": "A"},
    "student2": {"name": "Lahm", "grade": "B"}
}
print("Nested dictionary:", school)
