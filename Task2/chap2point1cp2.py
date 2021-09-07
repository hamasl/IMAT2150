import chap2point1cp1 as cp1


def generate_hilbert(dimension):
    hilbert = []
    for i in range(dimension):
        hilbert.append([])
        for j in range(dimension):
            # Hilbert uses 1/(i+j-1) since i and j starts at 1 and not 0, we need to add one 1 for i and j eac
            # Resulting in 1/(i+j-1+1+1) = 1/(i+j-1+2) = 1/(i+j+1)
            hilbert[i].append(1 / (i + j + 1))
    return hilbert


def generate_column_vector_of_value(length, value):
    ones = []
    for i in range(length):
        ones.append(value)
    return ones


if __name__ == "__main__":
    value = 1.0

    task_a_size = 2
    hilbert_a = generate_hilbert(task_a_size)
    ones_a = generate_column_vector_of_value(task_a_size, value)
    print("Task a")
    print(hilbert_a)
    print(cp1.naive_gaussian(hilbert_a, ones_a))

    task_b_size = 5
    hilbert_b = generate_hilbert(task_b_size)
    ones_b = generate_column_vector_of_value(task_b_size, value)
    print("\nTask b")
    print(hilbert_b)
    print(cp1.naive_gaussian(hilbert_b, ones_b))

    task_c_size = 10
    hilbert_c = generate_hilbert(task_c_size)
    ones_c = generate_column_vector_of_value(task_c_size, value)
    print("\nTask c")
    print(hilbert_c)
    print(cp1.naive_gaussian(hilbert_c, ones_c))
