# problem2.py
# Que: greet all the person names stored in a list "l" and which starts with S.
l = ["Hello", "Sam", "Sachin", "World", "sunny"]
for name in l:
    if name.lower().startswith("s"):
        print(f"Welcome: {name}")
