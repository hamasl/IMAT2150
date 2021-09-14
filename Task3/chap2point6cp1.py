import numpy as np


def conjugate_gradiant_method(x_0, A, b):
    x = x_0.copy()
    d = r = old_r = b - A @ x

    for i in range(len(b)):
        if r.all() == 0:
            break
        alpha = (np.transpose(r).dot(r)) / (np.transpose(d).dot(A.dot(d)))
        x += alpha * d
        # Cannot use -= because d = r = old_r at second line of function
        r = r - alpha * A.dot(d)
        beta = (np.transpose(r).dot(r)) / (np.transpose(old_r).dot(old_r))
        old_r = r
        d = r + beta * d
    return x, r, i


def print_res(x, r, i):
    print(f"Solution: {x}\nWith residual:{r}\nIn {i + 1} steps.")


if __name__ == "__main__":
    A = np.array([[1, 0], [0, 2]], dtype=float)
    b = np.array([[2], [4]], dtype=float)
    x_0 = np.array([[0], [0]], dtype=float)
    x, r, j = conjugate_gradiant_method(x_0, A, b)
    print("Task a:")
    print_res(x, r, j)

    A2 = np.array([[1, 2], [2, 5]], dtype=float)
    b2 = np.array([[1], [1]], dtype=float)
    x, r, j = conjugate_gradiant_method(x_0, A2, b2)
    print("\nTask b:")
    print_res(x, r, j)
