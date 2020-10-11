#! /usr/bin/env python

import math


def calc_roots(a, b, c):

    delta = b*b - 4 * a * c
    root1 = (-b - math.sqrt(delta)) / (2 * a)
    root2 = (-b + math.sqrt(delta)) / (2 * a)

    print("Root1: ", root1)
    print("Root2: ", root2)


print("Equation formula is: ax^2 +bx + c = 0.")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

calc_roots(a, b, c)
