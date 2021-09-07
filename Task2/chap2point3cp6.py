def gaussian(matrix, answer_matrix):
    for j in range(0, len(matrix) - 1):
        if abs(matrix[j][j]) == 0:
            raise Exception("zero pivot encountered")
        for i in range(j + 1, len(matrix)):
            mult = matrix[i][j] / matrix[j][j]
            for k in range(j + 1, len(matrix)):
                matrix[i][k] -= mult * matrix[j][k]
            answer_matrix[i] -= mult * answer_matrix[j]
    x = [None] * len(matrix[0])
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(i + 1, len(matrix)):
            answer_matrix[i] -= matrix[i][j] * x[j]
        x[i] = answer_matrix[i] / matrix[i][i]
    return x


if __name__ == "__main__":
    # Book version 2 ends up with the wrong answer
    a = [
        [1e-20, 1],
        [1, 2]
    ]
    b = [1, 4]
    print(gaussian(a, b))

    # Book version 3 ends up with the correct answer
    a2 = [
        [1, 2],
        [1e-20, 1]
    ]
    b2 = [4, 1]
    print(gaussian(a2, b2))

