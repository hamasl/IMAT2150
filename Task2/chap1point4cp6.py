import math


def f(r):
    return (2 * math.pi * r ** 3)/3 + (math.pi * r ** 2 * 10)/3 - 60


def f_differentiated(r):
    return 2 * math.pi * r ** 2 + (2 * math.pi * 10 * r) / 3


def newtons_method(x, function, function_differentiated, tol):
    x_i0 = x

    while abs(function(x_i0)) >= tol:
        x_i0 = x_i0 - function(x_i0) / function_differentiated(x_i0)
        print(x_i0)
    return x_i0


if __name__ == "__main__":
    print(newtons_method(5.0, f, f_differentiated, 1e-4))
