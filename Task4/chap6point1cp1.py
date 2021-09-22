import math


def correct_sol_a(t):
    return 0.5 * t ** 2 + 1


# NOTE know that this is bad practice, but this file will never be used by anyone else than me, and only used for this one exercise
def fun_a(t, y):
    y
    return t


def correct_sol_b(t):
    return math.e ** (1 / 3 * t ** 3)


def fun_b(t, y):
    return t ** 2 * y


def eulers_method(fun, t0, w0, h, steps, correct_sol):
    w = [w0]
    t = [t0]
    error = [0]
    for i in range(steps):
        t.append(t[i] + h)
        # TODO maybe add y as a param to fun and correct sol so it can be used for different tasks
        w.append(w[i] + h * fun(t[i], w[i]))
        error.append(abs(w[i + 1] - correct_sol(t[i + 1])))
    return w, t, error


def print_eulers_res(res):
    w, t, error = res
    if not (len(w) == len(t) == len(error)):
        return
    format_string = "{:<8} {:<25} {:<25} {:<15}"
    print(format_string.format("step", "w", "t", "error"))
    for i in range(len(w)):
        print(format_string.format(i, w[i], t[i], error[i]))


if __name__ == "__main__":
    print("Task a:")
    print_eulers_res(eulers_method(fun_a, 0, 1, 0.25, 4, correct_sol_a))

    print("\n\nTask b:")
    print_eulers_res(eulers_method(fun_b, 0, 1, 0.25, 4, correct_sol_b))
