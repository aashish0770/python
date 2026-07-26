# problem4.py
# Que: A file contents a word "Donkey" multiple times. You need to write a program which replaces this word with ##### by updating the same file.

with open("Chapter 9/file.txt", "r") as f:
    data = f.read().lower()
    data = data.replace("donkey", "#####")
    print(data)

with open("Chapter 9/file.txt", "w") as f:
    f.write(data)


print(data)
