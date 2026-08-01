# problem04.py
# Que: Write a class "Complex" to represent complex number, along with overloaded operators "+" and "*" which adds and multiplies them.


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# objects
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print("c1 + c2 = ", c1 + c2)
print("c1 * c2 = ", c1 * c2)
