# problem10.py
# Que: to print multiplication of n using for loops in reversed order.

n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    a = n * i
    print(f"{n} * {i} = {a}")
