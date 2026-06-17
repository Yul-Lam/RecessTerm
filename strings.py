# Exercise 4 (Strings)

# Declare an integer and a string and concatenate them correctly
number = 7
text = "days"
concatenated = str(number) + " " + text
print("Concatenated:", concatenated)

# Trim spaces at the beginning, in the middle, and at the end
txt = "      Hello,       Uganda!       "
trimmed = " ".join(txt.split())
print("Trimmed:", trimmed)

# Convert txt to uppercase
uppercase_txt = trimmed.upper()
print("Uppercase:", uppercase_txt)

# Replace 'U' with 'V' in the string
replaced_txt = uppercase_txt.replace("U", "V")
print("Replace U with V:", replaced_txt)

# Return a range of characters in the 2nd, 3rd and 4th position
y = "I am proudly Ugandan"
print("2nd, 3rd, and 4th chars:", y[1:4])

# Correct the string quoting error
x = 'All "Data Scientists" are cool!'
print(x)
