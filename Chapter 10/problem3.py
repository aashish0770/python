# problem3.py
# Que: Create a class with a class attribute a: create an object from it and set
# "a" directly using object a = 0. does this change the class attribute?


class MyClass:
    a = 0


b = MyClass()
b.a = 1
print(b.a)  # the arrtibute is same but the object is different

# --> No, it does not change the class attribute

