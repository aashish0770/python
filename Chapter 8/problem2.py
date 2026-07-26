# problem2.py
# Que: WAP using function to convert Clesius to Fahrenheit.


def temp(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = temp(celsius)
print("Temperature in Fahrenheit:", fahrenheit)
