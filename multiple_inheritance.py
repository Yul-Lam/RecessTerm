class Flyable:
    def fly(self):
        return "Flying through the sky..."


class Swimmable:
    def swim(self):
        return "Swimming in the water..."


class Walkable:
    def walk(self):
        return "Walking on the ground..."


class Duck(Flyable, Swimmable, Walkable):
    """Duck inherits from three classes"""
    def __init__(self, name):
        self.name = name


class Penguin(Swimmable, Walkable):
    """Penguin inherits from two classes (cannot fly)"""
    def __init__(self, name):
        self.name = name


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        return f"Brand: {self.brand}"


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_power(self):
        return f"Horsepower: {self.horsepower}"


class Car(Vehicle, Engine):
    """Car inherits from both Vehicle and Engine"""
    def __init__(self, brand, horsepower, color):
        Vehicle.__init__(self, brand)
        Engine.__init__(self, horsepower)
        self.color = color

    def full_info(self):
        return f"{self.describe()} | {self.get_power()} | Color: {self.color}"


if __name__ == "__main__":
    # Test Duck - can fly, swim, and walk
    duck = Duck("Donald")
    print(f"{duck.name}: {duck.fly()}")
    print(f"{duck.name}: {duck.swim()}")
    print(f"{duck.name}: {duck.walk()}")

    print("\n" + "="*50 + "\n")

    # Test Penguin - can only swim and walk
    penguin = Penguin("Tux")
    print(f"{penguin.name}: {penguin.swim()}")
    print(f"{penguin.name}: {penguin.walk()}")

    print("\n" + "="*50 + "\n")

    # Test Car - inherits from Vehicle and Engine
    car = Car("Toyota", 150, "Red")
    print(car.full_info())
