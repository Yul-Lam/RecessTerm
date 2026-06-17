# Exercise 1 (Lists)

# Create a list with 5 items (names of people)
people = ["Allot", "Beny", "Miin", "Diana", "Liam"]
print("People:", people)

# Output the 2nd item
print("2nd item:", people[1])

# Change the value of the first item to a new value
people[0] = "Amira"
print("After changing first item:", people)

# Add a sixth item to the list
people.append("Fiona")
print("After adding sixth item:", people)

# Add "Bathel" as the 3rd item in the list
people.insert(2, "Bathel")
print("After inserting Bathel as 3rd item:", people)

# Remove the 4th item from the list
removed_item = people.pop(3)
print(f"Removed 4th item ({removed_item}):", people)

# Use negative indexing to print the last item in the list
print("Last item using negative indexing:", people[-1])

# Create a new list with 7 items and print the 3rd, 4th and 5th items
more_people = ["George", "Hannah", "Ibrahim", "Jasmine", "Kevin", "Laura", "Mona"]
print("New list:", more_people)
print("3rd, 4th, and 5th items:", more_people[2:5])

# Write a list of countries and make a copy of it
countries = ["Canada", "Brazil", "Japan", "Kenya", "Norway"]
countries_copy = countries.copy()
print("Countries:", countries)
print("Countries copy:", countries_copy)

# Loop through the list of countries
print("Looping through countries:")
for country in countries:
    print(country)

# Write a list of animal names and sort them in both descending and ascending order
animals = ["zebra", "elephant", "giraffe", "panda", "cheetah", "antelope"]
print("Animals ascending:", sorted(animals))
print("Animals descending:", sorted(animals, reverse=True))

# Output only animal names with the letter 'a' in them
animals_with_a = [animal for animal in animals if "a" in animal]
print("Animals containing 'a':", animals_with_a)

# Write two lists and join them
first_names = ["Amira", "Charlie", "George"]
second_names = ["Smith", "Brown", "White"]
full_names = first_names + second_names
print("First names:", first_names)
print("Second names:", second_names)
print("Joined lists:", full_names)
