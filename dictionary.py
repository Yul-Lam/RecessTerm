#These store information in keyvalue pairs
#Properties-
#1 - Immutable and mutable

#Without dict function
data = {
    "x": 1,
    "y": 30,
}
print(data)

#Using Dict function
b=dict(name="Miin", age=20)
print(b)

#Accessing Dictionary Items
print(b["name"])

#Using get method
print(b.get("age"))