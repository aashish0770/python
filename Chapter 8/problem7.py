# problem7.py
# Que: function to remove a given word from a list and strip it at the same time


def remove_word(list, word):
    word = word.strip()  # clean input first

    if word in list:
        list.remove(word)
    return list


list = ["hello", "world", "this", "is", "a", "list"]
word = input("Enter a word to remove: ")
print(remove_word(list, word))
