# problem7.py
# Que: to find out whether a given post is taking about "Aashish" or not.

post = input("Enter a post: ")
if "aashish" in post.lower():
    print("The post is about Aashish.")
else:
    print("The post is not about Aashish.")
