# problem2.py
# Que: to find reminder of a number when divided by z
a = int(input("Enter the number: "))
z = int(input("Enter the divisor: "))
reminder = a % z
result = a // z
print("The reminder of", a, "when divided by", z, "is:", reminder)
print("The result of", a, "when divided by", z, "is:", result)
