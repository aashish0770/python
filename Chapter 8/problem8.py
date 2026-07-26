# problem8.py
# Que: function to print multiplication table of given number


def table(n):
    for i in range(1, 11):
        a = n * i
        print(f"{n} * {i} = {a}")


n = int(input("Enter a number: "))
table(n)
