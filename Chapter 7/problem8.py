# problem8.py
# Que: to print the following pattern:
# *
# **
# ***

for i in range(3):
    print("*" * (i + 1))

# with nested loop
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()
