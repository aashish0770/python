# problem7.py
# Que: to print the following star pattern.
#   *
#  ***
# *****

for i in range(3):
    spaces = 2 - i
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)

# with nested loop
for i in range(3):
    for j in range(2 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
