import numpy as np


def newtons_multivariate(f, df, x0, k):
    x = np.zeros((k + 1, len(x0)))
    x[0, :] = x0
    for i in range(k):
        s = np.linalg.solve(df(x[i]), -f(x[i]))
        x[i + 1, :] = x[i, :] + s
    return x[k, :]