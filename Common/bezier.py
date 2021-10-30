import matplotlib.pyplot as plt
import numpy as np


def get_bezier(x, y):
    b_x = 3 * (x[1] - x[0])
    c_x = 3 * (x[2] - x[1]) - b_x
    d_x = x[3] - x[0] - b_x - c_x

    b_y = 3 * (y[1] - y[0])
    c_y = 3 * (y[2] - y[1]) - b_y
    d_y = y[3] - y[0] - b_y - c_y

    return lambda t: x[0] + b_x * t + c_x * t ** 2 + d_x * t ** 3, lambda t: y[
                                                                                 0] + b_y * t + c_y * t ** 2 + d_y * t ** 3


if __name__ == '__main__':
    x = np.array([1, 1, 3, 2])
    y = np.array([1, 3, 3, 2])

    x_t, y_t = get_bezier(x, y)

    arr = np.arange(0, 1.01, 0.01)
    plt.title("Bezier curve")
    plt.scatter(x, y)
    plt.plot([x_t(t) for t in arr], [y_t(t) for t in arr])
    plt.show()
