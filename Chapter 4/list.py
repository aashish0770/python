# list.py

hello = [
    "apple",
    "banana",
    "cherry",
    5,
    10,
    15,
    20,
    False,
    True,
    3.14,
    2.71,
]
print(hello[0])  # printing the whole list
hello[0] = "orange"  # changing the first element of the list
print(hello[0])

#  indexing
print(hello[2:6])  # printing the elements from index 2 to 5

# list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Unlike strings, which are immutable, lists are mutable. This means that we can modify the contents of a list without creating a new list.
hello.append("appended")  # adding an element to the end of the list
print(hello)

hello.insert(1, "inserted")  # inserting an element at a specific index
print(hello)

hello.remove("banana")  # removing an element from the list
print(hello)

hello.pop()  # removing the last element from the list
print(hello)

hello.pop(1)  # removing the element at a specific index
print(hello)

hello.clear()  # clearing the list
print(hello)

l1 = [1, 25, 33, 4, 50, 77, 3, 0, 100]
l1.sort()  # sorting the list
print(l1)
l1.sort(reverse=True)  # sorting the list in descending order
print(l1)

l2 = [1, 25, 33, 4, 50, 77, 3, 0, 100]
l2.reverse()  # reversing the list
print(l2)
