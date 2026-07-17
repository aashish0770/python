# problem2.py
# que: print the multiplication table of 5
n = 5
for i in range(1, 11):
    a = n * i
    print(a, end=" ")

# que: print the multiplication table of a number entered by user
a = int(input("Enter a number: "))
for i in range(1, 11):
    b = a * i
    print(b, end=" ")
