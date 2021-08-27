import math
from typing import Tuple


def fpi(TOL, start_x, func):
    x_i0 = start_x
    x_i1 = None

    # Simulating do while in python
    while True:
        x_i1 = func(x_i0)
        if x_i1 == x_i0 or abs(x_i1 - x_i0) < TOL:
            return x_i1
        print(f"x_i0: {x_i0}")
        print(f"x_i1: {x_i1}")
        x_i0 = x_i1


def a_func(x):
    return (x ** 3 - 2) / 2

def a_func_v2(x):
    return math.sqrt(2*(x+1)/(x))


def b_func(x):
    return 7 - math.e ** x


def c_func(x):
    return math.asin(4 - (math.e ** x))

def iteration(given_function, x0, min_error=0.001, max_iteration=3) -> float:
    i = 0
    error = 1
    xp = []
    x = None
    while error > min_error and i < max_iteration:
        x = given_function(x0)
        error = abs(x0 - x)
        x0 = x
        xp.append(x0)
        i += 1
        print(xp)
    return x

def smfkne(x):
    return x**3-2*x-2

if __name__ == "__main__":
    tol = 1e-8
    print(f"Task a:\n{fpi(tol, 1, a_func_v2)}") # . (a) 1.76929235 (b) 1.67.... (c) 1.12998
    #print(f"Task a:\n{iteration(a_func_v2 , 1.6, tol, 100)}")
# print(f"Task b:\n{fpi(tol, 2, b_func)}")
#print(f"Task c:\n{fpi(tol, 1.3, c_func)}")
