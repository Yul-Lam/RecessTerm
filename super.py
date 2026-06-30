class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

    def description(self):
        return f"This is {self.name}."


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Use super() to call the parent method and extend its behavior
        parent_sound = super().speak()
        return f"{parent_sound} The dog barks."

    def description(self):
        return f"{super().description()} It is a {self.breed}."


if __name__ == "__main__":
    animal = Animal("Generic Animal")
    dog = Dog("Buddy", "Labrador")

    print(animal.speak())
    print(animal.description())
    print(dog.speak())
    print(dog.description())
