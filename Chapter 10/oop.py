# class
# class person: # class name
# methods & variables


class Person:
    age = 26  # class attribute
    language = "Python"


aashish = Person()
aashish.name = "Aashish Timalsina"  # instance attribute
print(aashish.name, aashish.age, aashish.language)

person2 = Person()
person2.name = "Aman Timalsina"
print(person2.name, person2.age, person2.language)

person3 = Person()
person3.name = "Sachin Timalsina"
person3.age = 25
print(person3.name, person3.age, person3.language)


# self parameter
class Employee:
    lan = "Python"
    salary = 10000

    def getInfo(self):
        print(f"The language is {self.lan} and salary is {self.salary}")

    @staticmethod # decorator, no need to pass self
    def info():
        print("This is a static method")


emp1 = Employee()
emp1.getInfo()

# __init__ method constructor

