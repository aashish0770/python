marks = {"Aashish": 90, "Aman": 80, "Amit": 70, "Aayush": 60}

print(marks, type(marks))
print(marks["Aashish"])  # display by key value pairs, return error if key is not found

# Dictionary is mutable data type

# methods in dictionary
print(marks.keys())  # returns the keys of the dictionary
print(marks.values())  # returns the values of the dictionary
print(marks.items())  # returns the key-value pairs of the dictionary
marks.update({"Aman": 85, "user": 100})  # update the value of a key
print("After update: ", marks)

print(
    marks.get("Aashish")
)  # prints the value of the key and return none if the key is not found

marks.pop("Aayush")  # removes the key-value pair
print("After pop: ", marks)

marks.popitem()  # removes the last key-value pair
print("After popitem: ", marks)

marks.clear()  # removes all the key-value pairs
print("After clear: ", marks)
