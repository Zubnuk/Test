from custom_exception import ArgumentException


def a(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 2
    return b(n - 1) + c(n - 1)


def b(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return a(n - 1) + c(n - 1)


def c(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return a(n - 1) + b(n - 1)


def start_from_zero(n: int) -> list[str]:
    if n == 1:
        return ['0']
    strings = start_from_one(n - 1)
    for i in range(len(strings)):
        strings[i] = "0" + strings[i]
    return strings


def start_from_one(n: int) -> list[str]:
    if n == 1:
        return ['1']
    strings = start_from_one(n - 1) + start_from_zero(n - 1)
    for i in range(len(strings)):
        strings[i] = "1" + strings[i]
    return strings


def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    if not (type(length) is int) or length <= 0:
        raise ArgumentException('The parameter length must be an integer '
                                'greater than 0')
    return a(length)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if not (type(length) is int) or length <= 0:
        raise ArgumentException('The parameter length must be an integer '
                                'greater than 0')
    return start_from_zero(length) + start_from_one(length)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
