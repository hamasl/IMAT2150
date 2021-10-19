import numpy as np

def power_iteration(A, x0, k):
    x = np.zeros((k + 1, len(x0)))
    x[0] = x0
    u = np.zeros((k + 1, len(x0)))
    lam = np.zeros(k + 1)
    # First version of eigenvalue is NaN to clarify that we did not calculate it at this point, and to have lam array
    # align with x and u array. Meaning that lam[i] belongs to x[i]
    lam[0] = np.NAN
    i = 1
    for i in range(1, k + 1):
        u[i - 1] = x[i - 1] / np.linalg.norm(x[i - 1])
        x[i] = A @ u[i - 1]
        lam[i] = np.transpose(u[i - 1]) @ A @ u[i - 1]
    u[i] = x[i] / np.linalg.norm(x[i])
    return u, lam, x


def print_task(A, x0, k, task_title):
    print(task_title)
    print(f"\nA:\n{A}")
    u, lam, x = power_iteration(A, x0, k)
    print(f"\nLast value of u:\n{u[-1]}")
    print(f"\nLast value of lambda:\n{lam[-1]}")
    print(f"\nLast value of x:\n{x[-1]}")


if __name__ == '__main__':
    x0 = np.array([1, 0, 0])
    k = 25

    # Task a
    A = np.array([10, -12, -6, 5, -5, -4, -1, 0, 3]).reshape(3, 3)
    print_task(A, x0, k, "Task a")


    # Task b
    A = np.array([-14, 20, 10, -19, 27, 12, 23, -32, -13]).reshape(3, 3)
    print_task(A, x0, k, "\n\nTask b")
