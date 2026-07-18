# problem3.py
# Que: to detect double  space in a string
string = input("Enter a string: ")
if "  " in string:
    print("The string contains double space.")
else:
    print("The string does not contain double space: " + string)

# print("The string does not double contain space: " + string) 