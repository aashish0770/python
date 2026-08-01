# problem01.py
# Que: Create a class 'pets' from the class Animal and further create a class 'Dog' from pets. add a method bark to class "dog"


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Animal name: {self.name}, age: {self.age}")


class Pets(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def show(self):
        print(f"Pet name: {self.name}, age: {self.age}, type: {self.type}")


class Dog(Pets):
    def __init__(self, name, age, type):
        super().__init__(name, age, type)

    def bark(self):
        print(f"{self.name} barks")

    def show(self):
        print(f"Dog name: {self.name}, age: {self.age}, type: {self.type}")


# objects
a = Animal("Lion", 5)
b = Pets("Kitty", 2, "Cat")
c = Dog("Max", 3, "Dog")

a.show()
b.show()
c.show()
c.bark()
