# Loops are used to repeat a block of code multiple times.
# There are 2 types of loops in Python:
# 1. for loop
# 2. while loop

# while loop
i = 1
while i <= 5:
    print(f"While loop: {i}")
    i += 1

# while loop will keep executing as long as the condition is true

# while loop with list
l = [1, "Aashish", False, "Hello", 3.14]

a = 0
while a < len(l):
    print(f"List: {l[a]}")
    a += 1

# for loop
for i in range(1, 6):
    print(f"For loop: {i}")

# for loop with step (start, end, step_size)
for i in range(1, 100, 5):
    print(f"For loop with step_size: {i}")

#  iterate over a list
for i in l:
    print(f"List: {i}")

#  for loop with else
for i in range(1, 6):
    print(f"For loop with else: {i}")
else:
    print("The loop is over")

#  Break Statement
#  break is used to break out of a loop, exit the loop abruptly
for i in range(100):
    print(f"Break Statement: {i}")
    if i == 7:
        break

# Continue Statement
#  continue is used to skip the current iteration of a loop
for i in range(10):
    if i == 7:
        continue
    print(f"Continue Statement: {i}")
    
#  Pass Statement
# pass is a null statement.
#  pass is used to do nothing. It is a placeholder for a statement that is not yet implemented
for i in range(10):
    pass
