# Exercise: Define Object-Level Attributes and Methods

class Student:
    """A class to represent a student"""
    
    # Constructor to initialize object-level attributes
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    # Method 1: Display student information
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
    
    # Method 2: Check if student is an adult
    def is_adult(self):
        if self.age >= 18:
            return f"{self.name} is an adult"
        else:
            return f"{self.name} is a minor"


# Create student objects
student1 = Student("Lahm", 20, "A")
student2 = Student("Lana", 17, "B")

# Print student1 age
print(student1.age)

# Test methods
print("\n--- Student 1 Info ---")
student1.display_info()
print(student1.is_adult())

print("\n--- Student 2 Info ---")
student2.display_info()
print(student2.is_adult())
