# problem3.py
# Que: A spam comment is defined as a tet containing following keywords:
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.


def is_spam(comment):
    spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
    for keyword in spam_keywords:
        if keyword in comment.lower():
            return True
    return False


comment = input("Enter a comment: ")
if is_spam(comment):
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
