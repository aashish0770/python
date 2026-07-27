# problemf.py
# Que: A file contents list of words multiple times. You need to write a program which replaces this word with ##### by updating the same file.

l = ["donkey", "monkey", "trash", "noob"]

with open("Chapter 9/file.txt", "r") as f:
    data = f.read().lower()
    for word in l:
        data = data.replace(word, "#####")
    print(data)

with open("Chapter 9/file.txt", "w") as f:
    f.write(data)

print(data)
