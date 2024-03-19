import numpy as np


def matrix_table(width, height):
    matrix = np.zeros((width, height))
    matrix[0] = list(range(1, height+1))
    for y in range(1, width):
        matrix[y] = [y*x for x in range(1, height+1)]

    return matrix

print(matrix_table(10, 10))