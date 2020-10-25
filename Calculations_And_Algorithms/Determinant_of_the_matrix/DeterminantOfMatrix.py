#! /usr/bin/env python

import random
import numpy as np
import math


# Checking if algorithm works correctly
def check_correctness(detA, detB):
    detB=math.floor(detB+0.49999999)

    if detA == detB:
        print("Algorithm is working fine. Determinant of given matrix is: ", detB)
    else:
        print("Determinant of given matrix is: ", detB)


# Function generating matrix with random content
def generate_random_matrix(rows, cols):

    matrix = [[random.randint(1, 5) for i in range(cols)] for j in range(rows)]

    return matrix


# Calculate determinant of given matrix using recursion
def calculate_determinant(X, n):

    det = 0
    matrix_temp = [[0 for i in range(n)] for j in range(n)]

    if n == 2:                                              # If matrix is 2x2...
        det = (X[0][0] * X[1][1]) - (X[1][0] * X[0][1])
        return det
    else:
        for c in range(n):
            subi = 0
            for i in range(1, n):
                subj = 0
                for j in range(n):
                    if j == c:
                        continue
                    matrix_temp[subi][subj] = X[i][j]
                    subj += 1
                subi += 1
            det = det + ((-1 ** c) * X[0][c] * calculate_determinant(matrix_temp, n - 1))
    return det


# rows, cols = (8, 8)
rows, cols = (3, 3)
matrix = generate_random_matrix(rows, cols)

for row in matrix:
    print(row)
print("\n")

# Calculate determinant (algorithm)
res_matrix = calculate_determinant(matrix, rows)

# Calculate determinant (numpy function)
res_matrix_check = np.linalg.det(matrix)

check_correctness(res_matrix, res_matrix_check)