# problem3.py
# Que: check the type of variable assigned using input() function.
a = input("Enter a value: ")

try:
    int(a)
    print("The value is an integer.")
except ValueError:
    try:
        float(a)
        print("The value is a float.")
    except ValueError:
        if a.lower() == "true" or a.lower() == "false":
            print("The value is a boolean.")
        else:
            print("The value is a string.")
