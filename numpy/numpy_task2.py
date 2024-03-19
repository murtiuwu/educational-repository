import numpy as np

def num_matrix(width, height):
    return np.transpose(np.array(list(range(width)) * height).reshape(height, width))

print(num_matrix(100, 3))
