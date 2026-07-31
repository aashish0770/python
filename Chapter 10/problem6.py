# problem6.py
# Que: Can you chnage the self-parameter inside a class to someting else?


class MyClass:
    def __init__(abc, name="Aashish"):
        # self.name = name
        print (f"Hello {name}")


MyClass("Aman")
MyClass()

# Yes, we can change the name of self to anything, but it is strongly recommended to use self by convention for better readability.
