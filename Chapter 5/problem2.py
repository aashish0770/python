# problem2.py
# Que: to input eight numbers from the user and display all the unique numbers.

num = {}
for i in range(8):
    n = int(input(f"Enter number {i + 1}: "))
    num[n] = n
print(num)

# using set
num = set()
for i in range(8):
    n = int(input(f"Enter number {i + 1}: "))
    num.add(n)
print(num)
