import chap2point2cp1 as cp1


def lc_back_substitution(l, b):
    c = [None] * len(b)
    c[0] = b[0]
    for i in range(1, len(b)):
        c[i] = b[i]
        for j in range(0, i):
            c[i] -= l[i][j] * c[j]
    return c


def ux_back_substitution(u, b):
    x = [None] * len(b)
    for i in range(len(u) - 1, -1, -1):
        for j in range(i + 1, len(u)):
            b[i] -= u[i][j] * x[j]
        x[i] = b[i] / u[i][i]
    return x


if __name__ == "__main__":
    # Task a
    a = [[3, 1, 2], [6, 3, 4], [3, 1, 5]]
    ab = [0, 1, 3]
    a_l, a_u = cp1.lu(a)
    print(ux_back_substitution(a_u, lc_back_substitution(a_l, ab)))

    # Task b
    b = [[4, 2, 0], [4, 4, 2], [2, 2, 3]]
    bb = [2, 4, 6]
    b_l, b_u = cp1.lu(b)
    print(ux_back_substitution(b_u, lc_back_substitution(b_l, bb)))
