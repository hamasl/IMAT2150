import math
from Task4 import chap6point1cp1 as cp1


def correct_sol(t):
    return math.e ** (t ** 3 / 3)


def fun(t, y):
    return t ** 2 * y


def midpoint_method(w0, t0, h, steps, fun, correct_sol):
    w = [w0]
    t = [t0]
    error = [0]
    for i in range(steps):
        t.append(t[i] + h)
        w.append(w[i] + h * fun(t[i] + h / 2, w[i] + h / 2 * fun(t[i], w[i])))
        error.append(abs(w[i + 1] - correct_sol(t[i + 1])))
    return w, t, error


if __name__ == "__main__":
    cp1.print_eulers_res(midpoint_method(1, 0, 0.1, 10, fun, correct_sol))
