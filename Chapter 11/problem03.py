# problem03.py
# Que: Create a class "Employee" and add salary and increment propertiees to it.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def increment(self):
        return self.salary * 1.10  # 10% increment

    @increment.setter
    def increment(self, value):
        self.salary = value / 1.10  # set salary based on increment value


a = Employee("John", 50000)
print(f"Employee name: {a.name}, salary: {a.salary}")
print(f"After increment (getter): {a.increment}")
a.increment = 10000
print(f"Employee name: {a.name}, salary: {a.salary}")