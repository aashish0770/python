# problem8.py
# Que: WAP to make a copy of a text file 'this.txt"
import os

file_path = "Chapter 9/this.txt"
with open("Chapter 9/file.txt", "r") as f:
    data = f.read()
    print(data)

with open(file_path, "w") as f:
    f.write(data)

print(f"File copied to {file_path}")
