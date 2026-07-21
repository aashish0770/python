# problem1.py
# Que: to create a dictionary of Neplai words with values as their English translation. Prrovide user with an option to look it up!

nepali_words = {
    "अ": "a",
    "आ": "aa",
    "इ": "i",
    "ई": "ii",
    "उ": "u",
    "ऊ": "uu",
    "ए": "e",
    "ऐ": "ai",
    "ओ": "o",
    "औ": "oo",
}

word = input("Enter a Nepali word: ")
print("The English translation is:", nepali_words.get(word, "Word not found"))
