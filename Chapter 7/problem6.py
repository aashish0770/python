# peoblem6.py
# Que: to calcuate the factorial of a given number using for loop.

n = int(input("Enter a number: "))
fac = 1
for i in range(1, n + 1):
    fac = fac * i
print("The factorial of", n, "is:", fac)
