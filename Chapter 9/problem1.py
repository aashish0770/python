# problem1.py
# Que: WAP to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle.

with open("Chapter 9/newfile.txt", "r") as f:
    data = f.read()
    if "twinkle" in data.lower():
        count = data.lower().count("twinkle")

        print(f"The word 'twinkle' is present {count}'s time in the file.")
    else:
        print("The word 'twinkle' is not present in the file.")
