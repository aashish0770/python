# Conditional Ecpression define a value that is a expression that is evaluated to True or False
# Conditional Ecpression can be used to control the flow of a program
a = int(input("Enter a age: "))

if a % 2 == 0:
    print("The number is even")

# if elif else
if a >= 18:
    print("You are eligible to vote")
elif a < 0:
    print("Not a valid age")
elif a == 0:
    print("O is not a valid age")
else:
    print("You are not eligible to vote")
