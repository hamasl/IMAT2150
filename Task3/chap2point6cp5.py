import numpy as np

import chap2point5cp1 as gen
import chap2point6cp1 as sol


def task(n):
    A = gen.gen_a(n)
    b = gen.gen_b(n)
    x, r, steps = sol.conjugate_gradiant_method(np.ones(n), A, b)
    if x.all() == 1:
        print(f"Found correct solution:\n{x}\nAfter {steps + 1} steps.\nWith residual: {r}")


if __name__ == "__main__":
    print("Task a:")
    task(100)
    print("\nTask b:")
    task(1000)
    print("\nTask c:")
    task(10000)
