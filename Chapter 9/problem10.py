# problem10.py
# Que: WAP to wipe out the content of a file

with open("Chapter 9/this.txt", "w") as f:
    f.write("")
    print("File content wiped out.")

# or

with open("Chapter 9/this.txt", "w") as f:
    f.truncate()
    print("File content wiped out.")
