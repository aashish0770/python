#  __ inti __ method is a constructor of a class
#  it is a special method that is called when an object is created


class Employee:
    # __init__ method will be called when an object is created
    def __init__(self, name, salary, lan):  # constructor
        self.name = name
        self.salary = salary
        self.lan = lan
        print("This is a constructor")

    def info(self):
        print("This is a instance method")


emp1 = Employee("Aashish", 10000, "Python")
print(emp1.name, emp1.salary, emp1.lan)
