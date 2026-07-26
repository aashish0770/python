# function.py
# Functions are blocks of code that perform specific tasks and can be reused in your code.
# They can accept parameters and return values.
# A function is defined using the def keyword, followed by the function name, parentheses, and a colon.
# Inside the function, you can define the code that the function will execute.


# simple example
# defining a function
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    avg = (a + b + c) / 3
    print("The average of", a, "and", b, "and", c, "is:", avg)


# calling the function
# avg()


#
def greeting(name):
    print("Hello", name)


name = input("Enter your name: ")
greeting(name)

# types of functions
# 1. built-in functions
# 2. user-defined functions

# Built-in functions
# len() function returns the length of a string
name1 = input("Enter your name: ")
length = len(name1)
print("The length of your name is:", length)


# functions with arg
def add(a, b):
    c = a + b
    print("The sum of", a, "and", b, "is:", c)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add(a, b)


# functions with return
def avg(a, b, c):
    avg = (a + b + c) / 3
    return avg


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
avg = avg(a, b, c)
print("The average of", a, "and", b, "and", c, "is:", avg)


# default arguments
def goodDay(name, ending="Good Day!"):
    print("Hello", name, ending)


name = input("Enter your name: ")
goodDay(name)

# recursion function
# a function that calls itself


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)  # here fact() is calling itself


n = int(input("Enter a number: "))
print("The factorial of", n, "is:", fact(n))
