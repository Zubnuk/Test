from custom_exception import ArgumentException


def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.        
    param length: a target route length.
    raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """

    def get_triangle_path_count_B(length):
        if length == 1 or length == 2:
            return 1
        return get_triangle_path_count(length - 1) + get_triangle_path_count_B(length - 1)

    def get_triangle_path_count_C(length):
        if length == 1 or length == 2:
            return 1
        return get_triangle_path_count(length - 1) + get_triangle_path_count_B(length - 1)

    Exception = 'The parameter length must be an integer greater than 0'
    if length is None:
        raise ArgumentException(Exception)
    if type(length) is not int:
        raise ArgumentException(Exception)
    if length <= 0:
        raise ArgumentException(Exception)
    if length < 2:
        return 0
    if length == 2 or length == 3:
        return 2
    return get_triangle_path_count_B(length - 1) + get_triangle_path_count_C(length - 1)


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """

    def string_begin_with_0(length):
        if length == 1:
            return ['0']
        return ['0' + x for x in string_begin_with_1(length - 1)]

    def string_begin_with_1(length):
        if length == 1:
            return ['1']
        return ['1' + x for x in string_begin_with_1(length - 1) + string_begin_with_0(length - 1)]

    Exception = 'The parameter length must be an integer greater than 0'
    if type(length) is not int:
        raise ArgumentException(Exception)
    if length <= 0:
        raise ArgumentException(Exception)
    return string_begin_with_0(length) + string_begin_with_1(length)


def main():
    print(get_triangle_path_count(7))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
