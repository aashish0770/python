# problem2.py
# Que: to accept marks of 6 students and display them in a sorted manner.
names = []
marks = []

for i in range(6):
    name = input("Enter name of student: ")
    names.append(name)
    mark = int(input("Enter marks of student: "))
    marks.append(mark)

marks.sort()
for i in range(6):
    print(names[i], ":", marks[i])

# using zip function
names = []
marks = []

for i in range(6):
    name = input("Enter name of student: ")
    names.append(name)
    mark = int(input("Enter marks of student: "))
    marks.append(mark)

for name, mark in zip(names, marks):
    print(name, ":", mark)
