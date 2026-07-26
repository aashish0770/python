# problem2.py
"""The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score."""

import os


def game():
    return int(input("Enter your score: "))


score = game()
file_path = "Chapter 9/Hi-score.txt"

# check if the file exists
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("")

# read old file
with open("Chapter 9/Hi-score.txt", "r") as f:
    data = f.read()

# handle the expty file
if data == "":
    highScore = 0
else:
    highScore = int(data)

# compare and update
if score > highScore:
    with open("Chapter 9/Hi-score.txt", "w") as f:
        f.write(str(score))
    print(f"New High Score: {score}")
else:
    print("High Score is not updated")
