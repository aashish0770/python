# problem4.py
# Que: to find whether a given usename contains less then 10 characters or not.

import re

username = input("Enter your username: ")

if not username:
    print("the username is empty.")

elif not username[0].isalpha():
    print("the username should start with a letter.")

elif not username.isalnum():
    print("the username should only contain letters and numbers.")

elif len(username) < 10:
    print("the username is less then 10 characters.", username)

else:
    print("the username is valid.", username)


# using regex

if re.fullmatch(r"[A-Za-z][A-Za-z0-9]{0,8}", username):
    print("Valid username")
else:
    print("Invalid username")
