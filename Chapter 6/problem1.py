# problem1.py
# Que: to find the greatest of four number entered by user

for i in range(4):
    number = int(input(f"Enter a number {i + 1}: "))
    if i == 0:
        max = number
    else:
        if number > max:
            max = number
print("The largest number is:", max)
