# problem6.py
# Que: Create an empty dictionary. Allow 4 friends to enter their facorite langauage as value and use key as theri names. Assume that names are unique.

d = {}
for i in range(1, 5):
    name = input(f"Enter name of friend {i}: ")

    if name in d:
        print("Name already exists. Please enter a different name.")
        continue
    lang = input(f"Enter favorite language of {i}: ")
    d[name] = lang

print(d)

# using dictionary comprehension
d = {
    input(f"Enter name of friend {i}: "): input(f"Enter favorite language of {i}: ")
    for i in range(1, 5)
}
print(d)
