import math


def bisection(TOL, a, b, f):
    c = None
    while (b - a) / 2 > TOL:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


def a_func(x):
    return x ** 3 - 9


def b_func(x):
    return 3 * x ** 3 + x ** 2 - x - 5


def c_func(x):
    return math.cos(x) ** 2 - x + 6


if __name__ == "__main__":
    tol = 1e-6
    print(f"Task a:\nroot is equal {bisection(tol, 0, 5, a_func)}")
    print(f"Task b:\nroot is equal {bisection(tol, 0, 2, b_func)}")
    print(f"Task c:\nroot is equal {bisection(tol, 0, 10, c_func)}")
