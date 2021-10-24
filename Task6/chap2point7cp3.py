import numpy as np
from Task6.newtons_multivariate_method import newtons_multivariate

if __name__ == '__main__':
    df_a = lambda x: np.array([3 * x[0]**1+1, -3 * x[1]**2, 2 * x[0], 2 * x[1]]).reshape(2, 2)
    f_a = lambda x: np.array([x[0] ** 3 - x[1] ** 3 + x[0], x[0] ** 2 + x[1] ** 2 - 1])
    #TODO only first solution works
    print(newtons_multivariate(f_a, df_a, np.array([1, 1]), 50))
    print(newtons_multivariate(f_a, df_a, np.array([-0.5, 1]), 50))
    print(newtons_multivariate(f_a, df_a, np.array([-1, 1]), 10))
    print(newtons_multivariate(f_a, df_a, np.array([1, -0.5]), 50))
