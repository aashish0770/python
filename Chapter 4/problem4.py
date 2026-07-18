# problem4.py
# Que: to sum a list with 4 numbers

numbers = []

for i in range(4):
    number = int(input(f"Enter a number {i + 1}: "))
    numbers.append(number)

sum = 0
for number in numbers:
    sum += number

print("The sum of the numbers is:", sum)
