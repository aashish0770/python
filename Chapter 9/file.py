"""
file.py
file are used to store the data in order to persist the data after the program is closed


a = "a very long strings with email"
emails = [] --> it will be lost after the program is closed
3 seconds
"""

"""There are 2 types of file
1. text file (.txt, .c, etc..)
2. binary file (.png, .mp3, etc..)
"""

f = open("Chapter 9/file.txt")  # open the file
# data = f.read()  # read the file
# print(data)

# lines = f.readlines()  # read the file line by line
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 == "")
# f.close()  # close the file
# # close the file once you are done with it

# functions of file
# st = "Write function to the file"
# f = open("Chapter 9/newfile.txt", "w")  # open the file in write mode
# f.write(st)  # write to the file
# f.close()

# in loop
f = open("Chapter 9/file.txt")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()

# append
st = "\nAppend function to the file."
f = open("Chapter 9/newfile.txt", "a")
f.write(st)
f.close()

# with
# you dont have to close the file with with statement
with open("Chapter 9/newfile.txt") as f:
    print(f.read( ))
