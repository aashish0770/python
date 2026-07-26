"""

1 for snake
-1 for water
0 for gun
"""

import random

comp = random.choice([-1, 0, 1])

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

if comp == -1 and you == 1:
    print("You won")

elif comp == -1 and you == 0:
    print("You lost")

elif comp == 1 and you == 0:
    print("You won")

elif comp == 1 and you == -1:
    print("You lost")

elif comp == 0 and you == 1:
    print("You lost")

elif comp == 0 and you == -1:
    print("You won")

else:
    print("Draw")
    
    

