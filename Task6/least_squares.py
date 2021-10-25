import numpy as np

def least_squares(A, b):
    A_t = np.transpose(A)
    return np.linalg.solve(A_t @ A, A_t @ b)


def rsme(A, b, x):
    return e_norm2(A, b, x) / (len(b) ** (1 / 2))

def e_norm2(A, b, x):
    return np.linalg.norm(b - A @ x)