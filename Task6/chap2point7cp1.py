import numpy as np
from Task6.newtons_multivariate_method import newtons_multivariate

if __name__ == '__main__':
    # TODO add searches for multiple solutions:
    print("Task a:")
    df_a = lambda x: np.array([2 * x[0], 2 * x[1], 2 * (x[0] - 1), 2 * x[1]]).reshape(2, 2)
    f_a = lambda x: np.array([x[0] ** 2 + x[1] ** 2 - 1, (x[0] - 1) ** 2 + x[1] ** 2 - 1])
    print(newtons_multivariate(f_a, df_a, np.array([1, 1]), 10))
    print(newtons_multivariate(f_a, df_a, np.array([1, -1]), 10))

    print("\n\nTask b:")
    df_a = lambda x: np.array([2 * x[0], 8 * x[1], 4 * x[0], 2 * x[1]]).reshape(2, 2)
    f_a = lambda x: np.array([x[0] ** 2 + 4 * x[1] ** 2 - 4, 4 * x[0] ** 2 + x[1] ** 2 - 4])
    print(newtons_multivariate(f_a, df_a, np.array([1, 1]), 10))
    print(newtons_multivariate(f_a, df_a, np.array([1, -1]), 10))
    print(newtons_multivariate(f_a, df_a, np.array([-1, 1]), 10))
    print(newtons_multivariate(f_a, df_a, np.array([-1, -1]), 10))

    print("\n\nTask c:")
    df_a = lambda x: np.array([2 * x[0], -8 * x[1], 2 * (x[0] - 1), 2 * x[1]]).reshape(2, 2)
    f_a = lambda x: np.array([x[0] ** 2 - 4*x[1] ** 2 - 4, (x[0] - 1) ** 2 + x[1] ** 2 - 4])
    print(newtons_multivariate(f_a, df_a, np.array([1, 1]), 10))
    print(newtons_multivariate(f_a, df_a, np.array([1, -1]), 10))
