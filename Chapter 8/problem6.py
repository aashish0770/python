# problem6.py
# Que: function to converts inches to centimeters


def convert(inches):
    cm = inches * 2.54
    return cm


inches = float(input("Enter the length in inches: "))
cm = convert(inches)
print("The length in centimeters is:", cm)
