import numpy as np
import scipy.sparse as sp


def jacobi(A, b, k, exact_sol):
    x = np.zeros(len(b))
    d = A.diagonal()
    r = A - sp.diags(d)
    for j in range(k):
        x = (b - r @ x) / d
        if forwards_error(exact_sol, x) < 1e-6:
            break

    return x, j, backwards_error(A, b, x)


def backwards_error(A, b, numeric_sol):
    return np.linalg.norm(b - A @ numeric_sol, np.inf)


def forwards_error(exact_sol, numeric_sol):
    return np.linalg.norm(exact_sol - numeric_sol)


def gen_a(n):
    return -1 * sp.eye(n, k=-1) + 3 * sp.eye(n) + -1 * sp.eye(n, k=1)


def gen_b(n):
    b = np.ones(n)
    b[0] = b[n - 1] = 2
    return b


def gen_b_v2(n):
    b = np.ones(n)
    b[0] = b[n - 1] = 2
    return b

def task(n):
    A = gen_a(n)
    b = gen_b(n)
    exact = np.ones(n)
    x, i, be = jacobi(A, b, 100, exact)
    if x.all() == 1:
        print(f"Found correct solution in {i + 1} steps, with backwards error of:\n{be}\nSolution is:\n{x}")

if __name__ == "__main__":
    print("Task a:")
    task(100)

    print("\nTask b:")
    task(100000)