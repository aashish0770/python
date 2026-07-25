# problem3.py
# Que: to print the multiplication table of a number entered by user in while loop

a = int(input("Enter a number: "))
i = 1
while i <= 10:
    b = a * i
    print(b, end=" ")
    i += 1
