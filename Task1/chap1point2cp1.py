import math

# TODO add max iterations
def fpi(tol, start_x, func):
    x_i0 = start_x

    # Simulating do while in python
    while True:
        x_i1 = func(x_i0)
        if x_i1 == x_i0 or abs(x_i1 - x_i0) < tol:
            return x_i1
        x_i0 = x_i1


def a_func(x):
    return math.sqrt(2 * (x + 1) / x)


def b_func(x):
    return math.log(7 - x)


def c_func(x):
    return math.log(4 - math.sin(x))


if __name__ == "__main__":
    TOL = 1e-8
    print(f"Task a:\n{fpi(TOL, 1, a_func)}")  # . (a) 1.76929235 (b) 1.67282170 (c) 1.12998
    print(f"Task b:\n{fpi(TOL, 2, b_func)}")
    print(f"Task c:\n{fpi(TOL, 1.3, c_func)}")
