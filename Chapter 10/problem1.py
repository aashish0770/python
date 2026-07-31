# problem1.py
# Que: creae a class "Programmer" or storig info of few programmers working in python


class Programmer:
    def __init__(self, name, salary, depertment, language):
        self.name = name
        self.salary = salary
        self.depertment = depertment
        self.language = language

    def getInfo(self):
        print(
            f"The name is {self.name}, salary is {self.salary}, depertment is {self.depertment}, language is {self.language}"
        )


count = int(input("Enter number of programmers: "))
programmers = []

try:
    for i in range(count):
        print(f"Enter details of {i + 1} programmer")
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        depertment = input("Enter depertment: ")
        language = input("Enter language: ")

        p = Programmer(name, salary, depertment, language)
        programmers.append(p)  # store the object in a list

        print("\n --- All programmers info ---")
        for p in programmers:
            p.getInfo()
except:
    print("Invalid input")
