# Example of implementing the Factory Design Pattern in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)

animal_factory = AnimalFactory()
dog = animal_factory.create_animal("dog", "Rex")
cat = animal_factory.create_animal("cat", "Tom")

print(dog.name) # Output: Rex
print(dog.speak()) # Output: Woof!
print(cat.name) # Output: Tom
print(cat.speak()) # Output: Meow!
