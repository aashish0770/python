# problem5.py
# Que: WAP to print firt n lines of the following pattern:
# ***
# **
# *


def pattern(n):
    for i in range(n):
        if n <= 0:
            return 0
        else:
            print("*" * (n - i))


n = int(input("Enter a number: "))
pattern(n)
