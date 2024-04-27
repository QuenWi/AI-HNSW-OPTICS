import random
import numpy as np

def dataset():
    matrix = [[0 for x in range(2)] for y in range(200)]
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            matrix[row][column] = random.randrange(-100, 100)
    return np.array(matrix, dtype=None, copy=False)

