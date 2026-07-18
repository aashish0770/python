# problem4.py
# Que: Use comparison operators to find out whether a given variable a is greater than b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if a > b:
    print(a, "is greater than", b)
elif a == b:
    print(a, "is equal to", b)
else:
    print(b, "is greater than", a)
