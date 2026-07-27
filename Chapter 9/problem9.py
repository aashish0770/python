# problem9.py
# Que: WAP to find out whether  file is identical & matches the content of another file

file1 = "Chapter 9/this.txt"
file2 = "Chapter 9/file.txt"

with open(file1, "r") as f1, open(file2, "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

    if data1 == data2:
        print("The files are identical\nMatches the content of another file.")
    else:
        print("The files are not identical.")
