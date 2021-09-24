import chap6point4cp1 as cp1_64
import chap6point1cp1 as cp1_61
import matplotlib.pyplot as plt


# Runge Kutta of 4th order
def rk4(w0, t0, h, steps, fun, correct_sol):
    w = [w0]
    t = [t0]
    error = [0]
    for i in range(steps):
        t.append(t[i] + h)
        s1 = fun(t[i], w[i])
        s2 = fun(t[i] + h / 2, w[i] + h / 2 * s1)
        s3 = fun(t[i] + h / 2, w[i] + h / 2 * s2)
        s4 = fun(t[i] + h, w[i] + h * s3)
        w.append(w[i] + h / 6 * (s1 + 2 * s2 + 2 * s3 + s4))
        error.append(abs(w[i + 1] - correct_sol(t[i + 1])))
    return w, t, error


if __name__ == "__main__":
    plt.title("RK4 vs correct solution")
    plt.xlabel("x")
    plt.ylabel("y")

    h = 0.1
    res = rk4(1, 0, h, 10, cp1_64.fun, cp1_64.correct_sol)
    print(f"\n\nRK4 with h: {h}")
    cp1_61.print_eulers_res(res)
    w, t, _ = res
    plt.plot(t, w, label=f"RK4 with h: {h}")
    plt.plot(t, [cp1_64.correct_sol(t[i]) for i in range(len(t))], label="Exact solution")


    h = 0.05
    res = rk4(1, 0, h, 20, cp1_64.fun, cp1_64.correct_sol)
    print(f"\n\nRK4 with h: {h}")
    cp1_61.print_eulers_res(res)
    w, t, _ = res
    plt.plot(t, w, label=f"RK4 with h: {h}")

    h = 0.025
    res = rk4(1, 0, h, 40, cp1_64.fun, cp1_64.correct_sol)
    print(f"\n\nRK4 with h: {h}")

    cp1_61.print_eulers_res(res)
    w, t, _ = res
    plt.plot(t, w, label=f"RK4 with h: {h}")

    plt.legend()
    plt.show()
