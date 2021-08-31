import numpy as np


def naive_gaussian(matrix, answer_matrix):
    """""
    print(matrix)
    print(matrix[0])
    print(matrix[0][0])
    print(np.finfo(float).eps)
    """
    """""
    for j in range(0, len(matrix-1):
        eliminate column j
    
    for j in range(0, len(matrix-1):
        for i in range(j + 1, len(matrix)):
            eliminate entry a[j][i]
    
    Matlab matrix goaes from 1 to n where n is len(matrix), python goes from 0 to n-1
    
    """""

    for j in range(0, len(matrix) - 1):
        if abs(matrix[j][j]) < np.finfo(float).eps:
            raise Exception("zero pivot encountered")
        for i in range(j + 1, len(matrix)):
            mult = matrix[i][j] / matrix[j][j]
            for k in range(j + 1, len(matrix)):
                matrix[i][k] -= mult * matrix[j][k]
            answer_matrix[i] -= mult * answer_matrix[j]
    x = [None]*len(matrix[0])
    for i in range(len(matrix)-1, -1, -1):
        for j in range(i+1, len(matrix)):
            answer_matrix[i] -= matrix[i][j] * x[j]
        x[i] = answer_matrix[i] / matrix[i][i]
    return x


if __name__ == "__main__":
    a = [
        [2, -2, -1],
        [4, 1, -2],
        [-2, 1, -1]
    ]
    ab = [-2, 1, -3]
    print(naive_gaussian(a, ab))
    print(a)
    print(ab)

    b = [
        [1, 2, -1],
        [0, 3, 1],
        [2, -1, 1]
    ]
    bb = [2, 4, 2]
    print(naive_gaussian(b, bb))
    print(b)
    print(bb)

    c = [
        [2, 1, -4],
        [1, -1, 1],
        [-1, 3, -2]
    ]
    cb = [-7, -2, 6]
    print(naive_gaussian(c, cb))
    print(c)
    print(cb)
