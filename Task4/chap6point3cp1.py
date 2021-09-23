import math
import matplotlib.pyplot as plt
import numpy as np


def fun_y1(_t, y):
    return y[0] + y[1]


def correct_sol_y1(t):
    return math.e ** t * math.cos(t)


def fun_y2(_t, y):
    return y[1] - y[0]


def correct_sol_y2(t):
    return -math.e ** t * math.sin(t)


# TODO add correct solution matrix or array
def eulers_method(fun, t0, w0, h, steps, correct_sol):
    w = [w0]
    t = [t0]
    error = [[0 for _ in range(len(w0))]]
    for i in range(steps):
        t.append(t[i] + h)
        wi = []
        error_i = []
        for j in range(len(w0)):
            # TODO configure param w[i]
            wi.append(w[i][j] + h * fun[j](t[i], w[i]))
            error_i.append(abs(wi[j] - correct_sol[j](t[i + 1])))
        # TODO maybe add y as a param to fun and correct sol so it can be used for different tasks
        w.append(wi)
        error.append(error_i)
    return w, t, error


def print_eulers_res(w, t, error):
    format_string = "{:<8} {:<25} {:<25} {:<20}"
    for j in range(len(w[0])):
        print(f"\n\nSolutions for y{j + 1}:")
        print(format_string.format("step", "w", "t", "error"))
        for i in range(len(w)):
            print(format_string.format(i, w[i][j], t[i], error[i][j]))


if __name__ == "__main__":
    # TODO Question ask for is the reduction in error form h = 0.1 to h = 0.01 consistent with the order of euler method
    h = 0.1
    print(f"Task a with h = {h}:")
    w0 = [1, 0]
    funs = [fun_y1, fun_y2]
    correct_sols = [correct_sol_y1, correct_sol_y2]
    w, t, error = eulers_method(funs, 0, w0, h, 10, correct_sols)
    w_np = np.array(w)
    print_eulers_res(w, t, error)

    fig, axs = plt.subplots(1, 2)
    axs[0].set_title("y1")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")
    axs[0].plot(t, w_np[:, 0], label=f"Computed solution with h {h}")
    axs[0].plot(t, [correct_sol_y1(t[i]) for i in range(len(t))], label="Exact solution")

    axs[1].set_title("y2")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("y")
    axs[1].plot(t, w_np[:, 1], label=f"Computed solution with h {h}")
    axs[1].plot(t, [correct_sol_y2(t[i]) for i in range(len(t))], label="Exact solution")

    h = 0.01
    print(f"\n\nTask a with h = {h}:")
    w, t, error = eulers_method(funs, 0, w0, h, 100, correct_sols)
    w_np = np.array(w)
    print_eulers_res(w, t, error)
    axs[0].plot(t, w_np[:, 0], label=f"Computed solution with h {h}")
    axs[1].plot(t, w_np[:, 1], label=f"Computed solution with h {h}")

    axs[0].legend()
    axs[1].legend()
    plt.show()
