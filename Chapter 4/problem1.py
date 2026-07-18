# problem1.py
# Que: to store seven fruits in a list entered by user
fruits = []
for i in range(7):
    fruit = input(f"Enter a {i + 1} fruit name: ")
    fruits.append(fruit)
print(fruits)
