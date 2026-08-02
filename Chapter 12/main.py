from module import myFun, myFun2

a = 10  # global variable


def fun():
    global a  # to access the global variable
    a = 30  # local variable for a function
    print(a)


fun()
print(a)

# emeraute function
# with out emulate function
l = [1, 2, 3, 4, 5]
index = 0
print("\n>---- without enumerate function ---->")
for item in l:
    print(f"index: {index}, item: {item}")
    index += 1

print("\n>---- with enumerate function ----> ")

# with enumerate  function
for index, item in enumerate(l):
    print(f"index: {index}, item: {item}")

# list comprehension
print("\n>---- list comprehension ----> ")
l1 = [1, 2, 3, 4, 5]

# without list comprehension
l2 = []
for item in l1:
    l2.append(item**2)
print(f"\n>---- without list comprehension ----> {l2}")

# with list comprehension
squaredList = [x**2 for x in l1]
print(f"\n>---- with list comprehension ----> {squaredList}")
