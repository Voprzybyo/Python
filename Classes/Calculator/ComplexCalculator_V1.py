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


print("Starting calculator mode!")

# Enter first complex number
complex_num = input("Enter first complex number(f.e. 1.0 -3.5j) : ")
complex_num = complex_num.split()
complex_num[1] = complex_num[1].replace('j', '')            # No matter if user put "j" at imaginary part or not
p = Complex(float(complex_num[0]), float(complex_num[1]))
print(p.val())

# Enter second complex number
complex_num = input("Enter second complex number(f.e. 2.0 -4.25j) : ")
complex_num = complex_num.split()
complex_num[1] = complex_num[1].replace('j', '')            # No matter if user put "j" at imaginary part or not
q = Complex(float(complex_num[0]), float(complex_num[1]))
print(q.val())

# Choose operation on given complex numbers
complex_oper = input("Enter operation( \"+\" \"-\" \"*\" ) : ")

if complex_oper == '+':
    z = p.add(q)
    print("Complex number adding: (", p.val(), ") + (", q.val(), ") =", z.val())

if complex_oper == '-':
    z = p.sub(q)
    print("Complex number subtracting: (", p.val(), ") - (", q.val(), ") =", z.val())

if complex_oper == '*':
    z = p.mul(q)
    print("Complex number multiplication: (", p.val(), ") * (", q.val(), ") =", z.val())


