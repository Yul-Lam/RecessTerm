# ============================================================================
# EXERCISE 9-1: Restaurant
# ============================================================================

class Restaurant:
    """A class to represent a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print restaurant information"""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")


# Exercise 9-1: Create an instance and test it
print("=" * 50)
print("EXERCISE 9-1: Restaurant")
print("=" * 50)

restaurant = Restaurant("Pizza Palace", "Italian")

# Print the two attributes individually
print(f"\nRestaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call both methods
print()
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()


# ============================================================================
# EXERCISE 9-2: Three Restaurants
# ============================================================================

print("\n" + "=" * 50)
print("EXERCISE 9-2: Three Restaurants")
print("=" * 50)

# Create three different instances
restaurant1 = Restaurant("Sakura Sushi", "Japanese")
restaurant2 = Restaurant("Le Français", "French")
restaurant3 = Restaurant("Tandoori Express", "Indian")

# Call describe_restaurant() for each instance
print("\nRestaurant 1:")
restaurant1.describe_restaurant()

print("\nRestaurant 2:")
restaurant2.describe_restaurant()

print("\nRestaurant 3:")
restaurant3.describe_restaurant()


# ============================================================================
# EXERCISE 9-3: Users
# ============================================================================

class User:
    """A class to represent a user"""
    
    def __init__(self, first_name, last_name, email, age, country):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country
    
    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"User Profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Age: {self.age}")
        print(f"  Country: {self.country}")
    
    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Welcome, {self.first_name}! Nice to meet you.")


print("\n" + "=" * 50)
print("EXERCISE 9-3: Users")
print("=" * 50)

# Create several instances representing different users
user1 = User("Ali", "Ahmed", "ali.ahmed@email.com", 25, "United Arab Emirates")
user2 = User("Fatima", "Khan", "fatima.khan@email.com", 28, "Pakistan")
user3 = User("Hassan", "Mohammad", "hassan.mohammad@email.com", 22, "Saudi Arabia")

# Call both methods for each user
print("\n" + "-" * 50)
print("User 1:")
print("-" * 50)
user1.describe_user()
user1.greet_user()

print("\n" + "-" * 50)
print("User 2:")
print("-" * 50)
user2.describe_user()
user2.greet_user()

print("\n" + "-" * 50)
print("User 3:")
print("-" * 50)
user3.describe_user()
user3.greet_user()
