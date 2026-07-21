s = {}  # enpty dictionary
print(type(s))

s1 = {1, 2, 3, 4, 5, "char"}  # sets with values
print(type(s1))

s3 = set()  # empty set, () used to create empty set not {}
print(type(s3))

s4 = {1, 2, 3, 4, 5, 5, 5}  # set takes only unique values
print(s4)

s5 = {1, 2, 100, 200}
s6 = {100, 200, 300, 400}

# set methodes:
s1.add(6)  # add an element to the set
print(f"Set s1: {s1}")  # print the set (s1)

s1.remove("char")  # remove an element from the set
print(s1)

# Set are unordered and cannot be accessed by index
# items in sets cant be changed and they are unique

print("Length of set s1:", len(s1))

s1.pop()  # remove a random element from the set
print(f"Set s1 after pop: {s1}")

print(f"Union of s6 and s5: {s6.union(s5)}")  # union of two sets
print(f"Intersection of s6 and s5: {s6.intersection(s5)}")  # intersection of two sets
