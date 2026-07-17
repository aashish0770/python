# problem4.py
# Que: Write a python program to print the contents of a directory using the os module.
import os

directory_path = "."
# List all files and directories
# to print the contents of the directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)

print("\nFull paths of the items in the directory:")
# to print the full path of each item in the directory
for item in os.listdir(directory_path):
    full_path = os.path.join(directory_path, item)
    print(full_path)
