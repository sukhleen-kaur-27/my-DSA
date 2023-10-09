from typing import *

def rotateMatrix(matrix : List[List[int]]):
    # Write your code here.
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = reversed(matrix[i])    