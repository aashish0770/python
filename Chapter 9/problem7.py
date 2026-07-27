# problem7.py
# Que: WAP to find out the line number where python is present in the file.

count = 0

with open("Chapter 9/newfile.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        if "python" in line.lower():
            print(f"Line {i}: {line.strip()}")
            count += 1

if count == 0:
    print("The word 'python' is not present in the file.")

print(f"\nTotal occurrences: {count}")
