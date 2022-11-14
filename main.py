from custom_exception import ArgumentException


def a(n):
    if n == 1:
        return 0
    if n == 2:
        return 2
    return b(n - 1) + c(n - 1)


def b(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return a(n - 1) + c(n - 1)


def c(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return a(n - 1) + b(n - 1)


def set0(n):
    if n == 1:
        return ['0']
    strings = set1(n - 1)
    for x in range(len(strings)):
        strings[x] = '0' + strings[x]
    return strings


def set1(n):
    if n == 1:
        return ['1']
    strings = set1(n - 1) + set0(n - 1)
    for x in range(len(strings)):
        strings[x] = '1' + strings[x]
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
    if type(length) is not int or length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return a(length)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if type(length) is not int or length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return set0(length) + set1(length)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(4))


if __name__ == '__main__':
    main()
