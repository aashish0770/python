# problem1.py
# Que: WAP using function to find the greatest number among three numbers.


def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The greatest number is:", greatest(a, b, c))
