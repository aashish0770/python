a = "string"  # double quotes
b = 'string'  # single quotes
c = """string"""  # triple quotes for multi-line strings

name = "Aashish"
nameshort = name[0:5]  # slicing the string to get first 5 characters
print(nameshort)  # Output: Aashi
char = name[3]  # getting the character at index 3, index starts from 0
print(char)  # Output: h

# negative slicing
# use of negative slicing is low
negslice = name[-5:-1]  # slicing from the end of the string
print(negslice)  # Output: shis
print(name[:4])  # is same as name[0:4]
print(name[4:])  # is same as name[4:len(name)]

# slicing with skip values
word = "Python"
print(word[1:5:2])  # Output: yh

# string functions
# len function returns the length of the string
print (len(name))  # Output: 7

# A and a are different characters in python, so the output will be False
print(name.endswith("sh"))  # Output: True
print(name.startswith("Aas"))  # Output: True

index = name.find("s")  # returns the index of the first occurrence of the substring
print(index)  # Output: 2

# escape sequences characters
print("Hello\nWorld")  # \n starts a new line
print("Hello\tWorld")  # \t adds a tab space
print("Hello\\World")  # \\ adds a backslash
print ("Hello\'World")  # \' adds a single quote
