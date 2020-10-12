#! /usr/bin/env python

import math


class Complex:

    # Constructor
    def __init__(self, realpart=0.0, imagpart=0.0):
        self.r = realpart
        self.i = imagpart

    # Conjugate of complex number (imaginary part negation)
    def conjugate(self):
        self.i = -self.i

    # Method that returns complete form of complex number
    def val(self):
        return '{} + ({})j'.format(self.r, self.i)

    # Method adding two complex numbers
    def add(self, other):
        return Complex(self.r + other.r,
                       self.i + other.i)

    # Method subtracting two complex numbers
    def sub(self, other):
        return Complex(self.r - other.r,
                       self.i - other.i)

    # Method multiply two complex numbers
    def mul(self, other):
        return Complex(self.r*other.r - self.i*other.i,
                       self.i*other.r + self.r*other.i)

    # Method returns absolute value of complex number
    def abs(self):
        return math.sqrt(self.r**2 + self.i**2)


# Create object of Complex class
x = Complex(2.0, -1.0)
y = Complex(2.0, -2.0)
a = Complex()
# Test val method (get full form of complex number)
print("Complex number: ", x.val())

# Test add method
z = x.add(y)
print("Complex number adding: (", x.val(), ") + (", y.val(), ") =", z.val())

# Test subtracting method
z = x.sub(y)
print("Complex number adding: (", x.val(), ") - (", y.val(), ") =", z.val())

# Test multiplication method
z = x.mul(y)
print("Complex number multiplication: (", x.val(), ") * (", y.val(), ") =", z.val())

# Test abs method
z = x.abs()
print("Absolute value of ", x.val(), " is: ", z)
