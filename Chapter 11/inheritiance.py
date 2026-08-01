class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"[Employee] name: {self.name}, salary: {self.salary}")


# With out inheritance from the "Employee" parent class
class Programmer:
    company = "YouTube"

    def __init__(self, name, slary, language):
        self.name = name
        self.salary = slary
        self.language = language

    def show(self):
        print(
            f"[Programmer] name: {self.name}, salary: {self.salary}, language: {self.language}"
        )

    def showLanguage(self):
        print(f"[Programmer] language: {self.language}")


# With inheritance
#  from the "Employee" parent class
# its show the clean code struture and reusability
# this is the example of single level inheritance
class Coder(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show(self):
        print(
            f"[Coder] name: {self.name}, salary: {self.salary}, language: {self.language}"
        )


# objects
a = Employee("Py", 10000)
b = Programmer("AS", 20000, "Python")
c = Coder("Aashish", 30000, "Java")

print(a.company)  # Google
print(b.company)  # YouTube
print(c.company)  # Google (from Employee due to MRO)

a.show()
b.show()
c.show()  # comes from Employee (MRO)
