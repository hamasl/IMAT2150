import numpy as np
import copy


def lu(matrix):
    u = np.array(copy.deepcopy(matrix))
    l = np.zeros(np.shape(matrix))

    for x in range(len(matrix)):
        l[x, x] = 1.0

    for j in range(0, len(matrix) - 1):
        if abs(matrix[j][j]) < np.finfo(float).eps:
            raise Exception("zero pivot encountered")
        for i in range(j + 1, len(matrix)):
            mult = u[i,j] / u[j,j]
            for k in range(j, len(matrix)):
                u[i, k] -= mult * u[j,k]
            l[i, j] = mult
    return l, u


if __name__ == "__main__":
    print("\nTask a")
    a = [
        [3, 1, 2],
        [6, 3, 4],
        [3, 1, 5]
    ]
    l, u = lu(a)
    print(f"L {l}")
    print(f"U {u}")

    print("\nTask b")
    b = [
        [4, 2, 0],
        [4, 4, 2],
        [2, 2, 3]
    ]
    l, u = lu(b)
    print(f"L {l}")
    print(f"U {u}")

    print("\nTask c")
    c = [
        [1, -1, 1, 2],
        [0, 2, 1, 0],
        [1, 3, 4, 4],
        [0, 2, 1, -1]
    ]
    l, u = lu(c)
    print(f"L {l}")
    print(f"U {u}")
