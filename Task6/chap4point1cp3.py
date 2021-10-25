import numpy as np
import matplotlib.pyplot as plt
from Task6.least_squares import least_squares, rsme


if __name__ == '__main__':
    A = np.array([1, 1960, 1, 1970, 1, 1990, 1, 2000]).reshape(-1, 2)
    b = np.array([3039585530, 3707475887, 5281653820, 6079603571])
    x_approx_a = least_squares(A, b)
    linear_model = lambda c, t: c[0] + c[1] * t
    print("Task a:")
    print(f"c value approximations: {x_approx_a}")
    rsme_a = rsme(A, b, x_approx_a)
    print(f"RSME: {rsme_a}")
    print(f"Linearly estimated value for 1980: {linear_model(x_approx_a, 1980)}")

    A = np.insert(A, 2, A[:, 1] ** 2, axis=1)
    x_approx_b = least_squares(A, b)
    parabola_model = lambda c, t: c[0] + c[1] * t + c[2] * t ** 2
    print("\n\nTask b:")
    print(f"c value approximations: {x_approx_b}")
    rsme_b = rsme(A, b, x_approx_b)
    print(f"RSME: {rsme_b}")
    print(f"Parabola estimated value for 1980: {parabola_model(x_approx_b, 1980)}\n")
    if rsme_a < rsme_b:
        print("Linear model gives best prediction")
    else:
        print("Parabola model gives best prediction")

    plt.scatter(A[:, 1], b)
    linspace = np.linspace(np.min(A[:, 1]), np.max(A[:, 1]))
    plt.plot(linspace, [linear_model(x_approx_a, t) for t in linspace], label="Linear")
    plt.plot(linspace, [parabola_model(x_approx_b, t) for t in linspace], label="Parabola")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()
