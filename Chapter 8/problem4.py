# problem4.py
# Que: write a recursive function to calaculate the sum of the first n natural number


def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)


n = int(input("Enter a number: "))

if n <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    result = sum_n(n)
    print("The sum of the first", n, "natural numbers is:", result)
