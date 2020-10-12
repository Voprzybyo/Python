#! /usr/bin/env python

import random


# Function generating matrix with random content
def generate_random_matrix(rows, cols):

    matrix = [[random.randint(1, 5) for i in range(cols)] for j in range(rows)]

    return matrix


# Calculate determinant of given matrix using recursion
def calculate_determinant(X, n):

    if len(X[0]) != len(X):   # Checking if number of column X is equal to number of rows Y (necessary condition)
        print("Cannot calculate determinant due to wrong matrix dimension")

    det = 0
    matrix_temp = [[0 for i in range(n)] for j in range(n)]
    if n == 2:                                              # If matrix is 2x2...
        return (X[0][0] * X[1][1]) - (X[1][0] * X[0][1])
    else:
        for x in range(n):
            temp_i = 0
            for i in range(n):
                temp_j = 0
                for j in range(n):
                    if j == x:
                        continue
                    matrix_temp[temp_i][temp_j] = X[i][j]
                    temp_j += 1
                temp_i += 1
            det = det + ((-1 ** x) * X[0][x] * calculate_determinant(matrix_temp, n - 1))
    return det


rows, cols = (8, 8)

matrix = generate_random_matrix(rows, cols)

for row in matrix:
    print(row)
print("\n")

res_matrix = calculate_determinant(matrix, rows)
print(res_matrix)
