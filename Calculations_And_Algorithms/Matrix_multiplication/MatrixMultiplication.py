#! /usr/bin/env python

import random


# Function generating matrix with random content
def generate_random_matrix(rows, cols):

    matrix = [[random.randint(1, 5) for i in range(cols)] for j in range(rows)]

    return matrix


# Multiplication of two given matrix
def matrix_multiply(X, Y):

    if len(X[0]) != len(Y) or len(Y[0]) != len(X):      # Checking if number of column X is equal to number of rows Y (necessary condition)
        print("Matrix dimensions incorrect! Cannot multiply given matrix")
        return -1
    else:
        RES = [[0 for i in range(len(X[0]))] for j in range(len(X))]    # Creating result matrix (filled with zeros)
        # Iterate rows
        for i in range(len(X)):
            # Iterate columns
            for j in range(len(X[0])):
                # iterate through rows of Y
                for k in range(len(Y)):
                    RES[i][j] += X[i][k] * Y[k][j]

    return RES


rows, cols = (8, 8)

matrix1 = generate_random_matrix(rows, cols)
matrix2 = generate_random_matrix(rows, cols)

for row in matrix1:
    print(row)
print("\n\n\n")

for row in matrix2:
    print(row)
print("\n\n\n")

res_matrix = matrix_multiply(matrix1, matrix2)
if res_matrix == -1:
    print("ERROR")
else:
    for row in res_matrix:
        print(row)

