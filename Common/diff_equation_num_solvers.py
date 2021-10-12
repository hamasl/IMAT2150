import numpy as np


def euler(w0, t0, h, steps, functions):
    w = np.array([w0])
    t = np.array([t0])
    for i in range(steps):
        t = np.append(t, t[i] + h)
        w = np.vstack((w, w[i] + h * (np.array([f(t[i], w[i]) for f in functions]))))
    return w


def midpoint(w0, t0, h, steps, functions):
    w = np.array([w0])
    t = np.array([t0])
    for i in range(steps):
        t = np.append(t, t[i] + h)
        k = np.array([f(t[i], w[i]) for f in functions])
        w = np.vstack((w, w[i] + h * (np.array([f(t[i] + h / 2, w[i] + h / 2 * k) for f in functions]))))
    return w


def trapezoid(w0, t0, h, steps, functions):
    w = np.array([w0])
    t = np.array([t0])
    for i in range(steps):
        t = np.append(t, t[i] + h)
        k = np.array([f(t[i], w[i]) for f in functions])
        w = np.vstack((w, w[i] + h / 2 * (k + np.array([f(t[i] + h, w[i] + h * k) for f in functions]))))
    return w


def rk4(w0, t0, h, steps, functions):
    w = np.array([w0])
    t = np.array([t0])
    for i in range(steps):
        t = np.append(t, t[i] + h)
        s1 = np.array([f(t[i], w[i]) for f in functions])
        s2 = np.array([f(t[i] + h / 2, w[i] + h / 2 * s1) for f in functions])
        s3 = np.array([f(t[i] + h / 2, w[i] + h / 2 * s2) for f in functions])
        s4 = np.array([f(t[i] + h, w[i] + h * s3) for f in functions])
        w = np.vstack((w, w[i] + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4)))
    return w


def calc_error(w0, t0, steps, w, true_functions):
    errors = np.array([[0 for _ in range(len(w0))]])
    for i in range(1, steps + 1):
        errors = np.vstack((errors, np.array([abs(w[i] - [f(t0 + i * h) for f in true_functions])])))
    return errors


if __name__ == '__main__':
    w0 = np.array([1, 0])
    t0 = 0
    h = 1 / 4
    s = 4
    functions = [lambda t, y: y[0] + y[1], lambda t, y: -y[0] + y[1]]
    print(f"Trapezoid v1")
    print(trapezoid(w0, t0, h, s, functions))

    w0 = np.array([1])
    functions = [lambda t, y: t ** 3 / y[0] ** 2]
    print("\nTrapezoid v2")
    print(trapezoid(w0, t0, h, s, functions))
    print("\nEuler")
    print(euler(w0, t0, h, s, functions))
    print("\nMidpoint")
    print(midpoint(w0, t0, h, s, functions))
    print("\nRK4")
    w = rk4(w0, t0, h, s, functions)
    print(w)
    print("\nRK4 error:")
    print(calc_error(w0, t0, s, w, [lambda t: (3 / 4 * t ** 4 + 1) ** (1 / 3)]))
