def correct_sol_a(t):
    return 0.5 * t ** 2 + 1


# NOTE know that this is bad practice, but this file will never be used by anyone else than me, and only used for this one exercise
def fun_a(t):
    return t


def trapezoid(fun, t0, w0, h, steps, correct_sol):
    w = [w0]
    t = [t0]
    error = [0]
    for i in range(steps):
        t.append(t[i] + h)
        # TODO maybe add y as a param to fun and correct sol so it can be used for different tasks
        # w.append(w[i] + h/2 *(fun(t[i], w[i]) + fun(t[i]+h, w[i] + h*fun(t[i], w[i]))))
        w.append(w[i] + h / 2 * (fun(t[i]) + fun(t[i] + h)))
        error.append(abs(w[i + 1] - correct_sol(t[i + 1])))
    return w, t, error


def print_trapezoid_res(res):
    w, t, error = res
    if not (len(w) == len(t) == len(error)):
        return
    format_string = "{:<8} {:<25} {:<25} {:<15}"
    print(format_string.format("step", "w", "t", "global error"))
    for i in range(len(w)):
        print(format_string.format(i, w[i], t[i], error[i]))


if __name__ == "__main__":
    print("Task a:")
    print_trapezoid_res(trapezoid(fun_a, 0, 1, 0.1, 10, correct_sol_a))
