from numpy import *


# Finds sum of c_n*x_n
def nest(c, x, b=[]):
    d = len(c) - 1
    if b == []:
        b = zeros(d)
    y = c[d]
    for i in range(d - 1, -1, -1):
        y *= (x - b[i])
        y += c[i]
    return y


if __name__ == '__main__':
    x_val = 1.00001
    px = nest(ones(50), x_val)
    qx = ((x_val ** 51 - 1) / (x_val - 1))
    print(f"p({x_val})={px}")
    print(f"q({x_val})={qx}")
    print(f"Error is {abs(qx - px)}")
