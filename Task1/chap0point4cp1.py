import math


# Function used for task a which will give invalid result
def a_invalid(x):
    return (1 - (1 / math.cos(x))) / (math.tan(x) ** 2)


# Function used for task a which will give valid result
def a_valid(x):
    return -1 / (1 + (1 / math.cos(x)))


def print_for_each(function_name, function):
    i = 1e-1
    while i >= 1e-14:
        print(f"{function_name} for x = {i} answer is {function(i)}")
        i *= 1e-1


# TODO Add reporting of number of correct digits for each x
if __name__ == "__main__":
    print("Original function: ")
    print_for_each("(1-sec(x))/(tan(x))^2", a_invalid)
    print("\nRevised function: ")
    print_for_each("-1/(1+(1/math.cos(x)))", a_valid)
