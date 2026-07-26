# problem3.py
# Que: How do you prevent a python print() function to print a new line at the end


def print_without_newline(text):
    print(text, end=" ")


text = input("Enter a Text: ")
print_without_newline(text)
print ("Hello")
