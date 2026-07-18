# problem4.py
# Que: to replace double space with single space in a string
string = input("Enter a string: ")
if "  " in string:
    string = string.replace("  ", " ")
    print("The string after replacing double space with single space: " + string)
else:
    print("The string does not contain double space: " + string)
