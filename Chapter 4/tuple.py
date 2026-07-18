# tuple.py
# Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.
a = ("apple", "banana", False, 1, 2, 3, 1)
print(a)

b = (1,)
print(type(b))  # to check the type of the variable

#  methods in tuple
no = a.count(1)
print(no)

i = a.index(1)
print(i)  # returns the index of the first occurrence of the specified value

print(len(a))