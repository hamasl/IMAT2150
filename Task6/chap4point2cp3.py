import math

import numpy as np
from matplotlib import pyplot as plt

from Task6.least_squares import least_squares, e_norm2

if __name__ == '__main__':
    A = np.array([1, 1960, 1, 1970, 1, 1990, 1, 2000]).reshape(-1, 2)
    b = np.array([3039585530, 3707475887, 5281653820, 6079603571])

    b_modified = np.array([math.log(i) for i in b])
    exp_model = lambda c, t: c[0] * math.e ** (c[1] * t)
    c = least_squares(A, b_modified)

    #TODO find estimate error, dont think this is correct
    print(f"Estimation error: {e_norm2(A, b_modified, c)}")


    # From the equation c1 = e ** k, since c returns [k, c2]
    c[0] = math.e**(c[0])
    print(f"C-values are: {c}")
    print(f"Population in 1980: {exp_model(c, 1980)}")

    plt.scatter(A[:, 1], b)
    linspace = np.linspace(np.min(A[:, 1]), np.max(A[:, 1]))
    plt.plot(linspace, [exp_model(c, t) for t in linspace], label="Exponential")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


