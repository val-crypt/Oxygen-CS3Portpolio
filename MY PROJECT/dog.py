class Dog:
    def __init__(self, name, age):
        self.name = name
        self.breed = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")