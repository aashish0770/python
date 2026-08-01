class Employee:
    company = "ICT"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"[Employee] name: {self.name}, salary: {self.salary}")


class Coder:
    language = "Python"

    def __init__(self, Os, experience):
        self.Os = Os
        self.experience = experience

    def show(self):
        print(f"[Coder] OS: {self.Os}, experience: {self.experience}")


# Multiple Inheritance
class Programmer(Employee, Coder):
    def __init__(self, name, salary, Os, experience):
        Employee.__init__(self, name, salary)
        Coder.__init__(self, Os, experience)

    def show(self):
        print(
            f"[Programmer] name: {self.name}, salary: {self.salary}, OS: {self.Os}, experience: {self.experience}, company: {self.company}, language: {self.language}"
        )


# objects
a = Employee("Aashish", 60000)
a.show()

b = Coder("Linux", 10)
b.show()

c = Programmer("John", 50000, "Windows", 5)
c.show()