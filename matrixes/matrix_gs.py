import numpy as np


def multiply_n_matrix(matrices):
    for matrix in range(matrices):
        output = matrix ** matrix

    return output


# r = [[1, 2], [3, 4]]
def create_array_matrix(r):
    array = np.array(r)
    matrix = np.asmatrix(array)
    return matrix
