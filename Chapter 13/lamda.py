# with out lambda function
def square(x):
    return x * x


print(square(5))  # 25

# with lambda function
square = lambda x: x * x
print(square(4))

# join method
l = ["a", "b", "c", "d"]
print("".join(l))

a = "hello"
print(a.join(l))  # ahellobhellochellod

# format method
name = "John"
age = 30
# format method with string not used less but have in python 3.6 and above
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# map function
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, numbers))
print(square)  # [1, 4, 9, 16, 25


# filter function
def is_even(x):
    if x % 2 == 0:
        return True
    return False


only_even = list(filter(is_even, numbers))
print(only_even)  # [2, 4]

# reduce function
from functools import reduce


def sum(x, y):
    return x + y


total = reduce(sum, numbers)
print(total)

# reduce get the output one by one or step by step from the list
# from the list of numbers and apply the sum function to them
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
