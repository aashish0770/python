# problem6.py
# Que: WAP to mine a log file and find out whether it contains the word pthon.

with open("Chapter 9/newfile.txt", "r") as f:
    data = f.read()
    lower = data.lower()
    if "python" in lower:
        count = lower.count("python")
        print(f"The word 'python' is present {count}'s time in the file.")
    else:
        print("The word 'python' is not present in the file.")
