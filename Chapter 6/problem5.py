# problem5.py
# Que: which find a given name is present in a list or not.

names = ["hello", "world", "This", "is", "a", "list"]
name = input("Enter a name: ")

# if name in names: # case sensitive
if name.lower() in names:
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")
