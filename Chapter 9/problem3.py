# problem3.py
# Que: WAP to generate nultiplication tables from 2 to 20 and write it to the different files.
# place files in a folder for a 13 year old student

import os

file_path = "Chapter 9/tables/"
os.makedirs(file_path, exist_ok=True)

for i in range(2, 21):
    with open(file_path + f"table{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}\n")

    print(f"Table {i} generated and saved to {file_path}table{i}.txt")
