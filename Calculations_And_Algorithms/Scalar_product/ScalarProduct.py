#! /usr/bin/env python


def scalar_product(vector1, vector2):

    result = 0

    # Checking if length of given vectors is correct
    if len(vector1) != len(vector2):
        print("Cannot calculate scalar product of given vectors (size difference)")
        return -1

    # Calculating scalar product
    for i in range(len(vector1)):
        result += (vector1[i] * vector2[i])

    return result


v1 = [1, 2, 12, 4]
v2 = [2, 4, 2, 8]

res = scalar_product(v1, v2)

print(res)
