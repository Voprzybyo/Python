#! /usr/bin/env python

import random


# Function generating matrix with random content
def generate_random_matrix(rows, cols):

    matrix = [[random.randint(1, 100) for i in range(cols)] for j in range(rows)]

    return matrix


# Sum of two given matrix
def matrix_sum(X, Y):

    if len(X) != len(Y) or len(X[0]) != len(Y[0]):      # Checking if matrix dimensions are correct
        print("Matrix dimensions incorrect!")
        return -1
    else:
        RES = [[0 for i in range(len(X[0]))] for j in range(len(X))]    # Creating result matrix (filled with zeros)
        # Iterate rows
        for i in range(len(X)):
            # Iterate columns
            for j in range(len(X[0])):
                RES[i][j] = X[i][j] + Y[i][j]

    return RES


rows, cols = (5, 5)

matrix1 = generate_random_matrix(rows, cols)
matrix2 = generate_random_matrix(rows, cols)

for row in matrix1:
    print(row)
print("\n\n\n")

for row in matrix2:
    print(row)
print("\n\n\n")

res_matrix = matrix_sum(matrix1, matrix2)
if res_matrix == -1:
    print("ERROR")
else:
    for row in res_matrix:
        print(row)
