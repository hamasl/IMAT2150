import chap2point2cp1 as cp1


def back_substitution(L, U, b):
    c = [None] * len(L[0])
    for i in range(len(L) - 1, -1, -1):
        for j in range(i + 1, len(L)):
            b[i] -= L[i][j] * c[j]
        c[i] = b[i] / L[i][i]

    x = [None] * len(U[0])
    for i in range(len(U) - 1, -1, -1):
        for j in range(i + 1, len(U)):
            c[i] -= U[i][j] * x[j]
        x[i] = c[i] / U[i][i]
    return x


if __name__ == "__main__":
    # Task a
    a = [[3, 1, 2], [6, 3, 4], [3, 1, 5]]
    ab = [0, 1, 3]
    a_l, a_u = cp1.lu(a)
    print(back_substitution(a_l, a_u, ab))

    # Task b
    b = [[4, 2, 0], [4, 4, 2], [2, 2, 3]]
    bb = [2, 4, 6]
    b_l, b_u = cp1.lu(b)
    print(back_substitution(b_l, b_u, bb))
    # TODO NB should maybe be 1, -1, 3.0
