# problem5.py
# Que: to format the following letter using escape sequence characters.
Letter = "Hello, My name is Aashish Timasina. I am from Nepal. I am a student of BSc.CSIT. I am learning Python programming language. Thank you!"

formated = Letter.replace(". ", ".\n")  # replacing the full stop with a new line
print(formated)

# for user input
paragraph = input("Enter a paragraph: ")
formated_paragraph = paragraph.replace(". ", ".\n")  # replacing the full stop
print("The formated paragraph is: \n" + formated_paragraph)
