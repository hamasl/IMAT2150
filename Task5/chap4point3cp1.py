import numpy as np


def gram_schmidt(A):
    n = len(A)
    r = np.zeros((n, n))
    q = np.zeros((n, n))
    for j in range(n):
        y = A[:, j]
        for i in range(j):
            r[i, j] = np.transpose(q[:, i]) @ A[:, j]
            y = y - r[i, j] * q[:, i]
        r[j, j] = np.linalg.norm(y)
        q[:, j] = 1 / r[j, j] * y
    return q, r


if __name__ == '__main__':
    # a
    print("Task a:")
    A = np.array([4, 0, 3, 1]).reshape(2, 2)
    print(f"A:\n {A}")
    q, r = gram_schmidt(A)
    print(f"q:\n {q}")
    print(f"r:\n {r}")

    # b
    print("\n\nTask b:")
    A = np.array([1, 2, 1, 1]).reshape(2, 2)
    print(f"A:\n {A}")
    q, r = gram_schmidt(A)
    print(f"q:\n {q}")
    print(f"r:\n {r}")

    # c
    print("\n\nTask c:")
    A = np.array([2, 1, 1, -1, 2, 1]).reshape(3, 2)
    print(f"A:\n {A}")
    # Need to append linearly independent column [0 0 1]^T to make gram schimdt algo work. When method returns just, remove last column of r
    A = np.append(A, [[0], [0], [1]], axis=1)
    q, r = gram_schmidt(A)
    # Removing last column of r
    r = np.delete(r, -1, axis=1)
    print(f"q:\n {q}")
    print(f"r:\n {r}")

    # d
    print("\n\nTask d:")
    A = np.array([4, 8, 1, 0, 2, -2, 3, 6, 7]).reshape(3, 3)
    print(f"A:\n {A}")
    q, r = gram_schmidt(A)
    print(f"q:\n {q}")
    print(f"r:\n {r}")
