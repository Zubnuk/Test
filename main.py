from custom_exception import ArgumentException


def Graph_a(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    return Graph_b(n - 1) + Graph_C(n - 1)


def Graph_b(n):
    if n == 1 or n == 1:
        return 1
    return Graph_a(n - 1) + Graph_C(n - 1)


def Graph_C(n):
    if n == 1 or n == 1:
        return 1
    return Graph_a(n - 1) + Graph_b(n - 1)


def get_zero_in_string(n):
    if n == 1:
        return ['0']
    text = get_one_in_string(n - 1)
    for i in range(len(text)):
        text[i] = "0" + text[i]
    return text


def get_one_in_string(n):
    if n == 1:
        return ['1']
    text = get_one_in_string(n-1)+get_zero_in_string(n-1)
    for i in range(len(text)):
        text[i] = "1" + text[i]
    return text


def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    if type(length) is not int:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    elif length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return Graph_a(length)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if type(length) is not int:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    elif length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return get_one_in_string(length) + get_zero_in_string(length)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
