# problem9.py
# Que: to print the following pattern:
# ***
# * *
# ***

for i in range(3):
    if i == 1:
        print("* *")
        continue
    print("*" * 3)

# whit logic pattern
for i in range(3):
    for j in range(3):
        if i == 0 or i == 2 or j == 0 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# with user input range
a = int(input("Enter a range: "))

for i in range(a):
    if i % 2 == 0:
        print("*" * 3)
    else:
        print("* *")
