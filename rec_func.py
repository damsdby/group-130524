x = 500
y = 21

a = 670
b = 5


def create_algorithm(x: int, y: int) -> int:
    """
    this function takes args x and y to find the int number, on which there are divided together without float
    :param x: first number
    :param y: second number
    :return: integer_number(GCD-Greatest Common Divisor), which can be divided into args x and y

    """
    if y == 0:
        return x
    else:
        return create_algorithm(y, x % y)


def create_rec_algorithm_operations(a: int, b: int) -> int:
    """
    this function has two integers a and b and searching/considering different possible variants in the cycles "if"

    :param a: first integer number
    :param b: second integer number
    :return: two integers values in list that gone through cycles
    """
    if a == 0 or b == 0:
        return [a, b]

    if a >= 2 * b:
        a -= 2 * b
        return create_rec_algorithm_operations(a, b)

    if b >= 2 * a:
        b -= 2 * a
        return create_rec_algorithm_operations(a, b)

    return [a, b]


result = create_algorithm(x, y)
print(result)

result = create_rec_algorithm_operations(a, b)
print(result)
