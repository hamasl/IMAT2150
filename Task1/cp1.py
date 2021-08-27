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
    x = 1.00001
    px = nest(ones(50), x)
    qx = ((x ** 51 - 1) / (x - 1))
    print(f"p({x})={px}")
    print(f"q({x})={qx}")
    print(f"Error is {math.fabs(qx - px)}")
