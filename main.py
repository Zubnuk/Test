from custom_exception import ArgumentException


def get_triangle_path_count_B(length: int) -> int:
    if length == 1 or length == 2:
        return 1
    return get_triangle_path_count(length - 1) + get_triangle_path_count_B(length - 1)
"""Calculates the number of closed routes of a target length between three
    vertices A, B and C that start at the A and end at the B vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :return: the number of routes.
    """


def get_triangle_path_count_C(length: int) -> int:
    if length == 1 or length == 2:
        return 1
    return get_triangle_path_count(length - 1) + get_triangle_path_count_B(length - 1)
"""Calculates the number of closed routes of a target length between three
    vertices A, B and C that start at the A and end at the C vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    greater than 0
    :return: the number of routes.
    """


def get_triangle_path_count(length: int) -> int:
    if not (type(length) is int):
        raise ArgumentException('The parameter length must be an integer greater than 0')
    if length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    if length < 2:
        return 0
    if length == 2 or length == 3:
        return 2
    return get_triangle_path_count_B(length - 1) + get_triangle_path_count_C(length - 1)
"""Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """


def string_begin_with_zero(length: int) -> list[str]:
    if length == 1:
        return ['0']
    return ['0' + x for x in string_begin_with_one(length - 1)]
"""Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes and beginning with zero.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """


def string_begin_with_one(length: int) -> list[str]:
    if length == 1:
        return ['1']
    return ['1' + x for x in string_begin_with_one(length - 1) + string_begin_with_zero(length - 1)]
"""Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes and beginning with ones.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """


def generate_strings(length: int) -> list[str]:
    if not (type(length) is int):
        raise ArgumentException('The parameter length must be an integer greater than 0')
    if length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return string_begin_with_zero(length) + string_begin_with_one(length)
"""Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """


def main():
    print(get_triangle_path_count(10))
    print(generate_strings(3))


if __name__ == '__main__':
    main()
