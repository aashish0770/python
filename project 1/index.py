# Cleaner version of same as main.py

import random

comp = random.choice([1, 0, -1])

wining_case = {(1, -1), (0, 1), (-1, 0)}

youstr = (
    input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()
)
if youstr not in ["s", "w", "g"]:
    print("Invalid input")
    exit()
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

print("The computer chose", reverseDict[comp])
print("You chose", reverseDict[you])

if you == comp:
    print("Draw")
elif (you, comp) in wining_case:
    print("You won")
else:
    print("You lost")
