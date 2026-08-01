# decorator, it is a class method, with we get the class value not the instance
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    # property decorator
    @property
    def name(self):
        return f"{self.lname} {self.fname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 2
e.name = "Aashish Timalsina"
print(e.name)
e.show()
