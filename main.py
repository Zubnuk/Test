from custom_exception import ArgumentException


def get_count_a(length):
    if length == 1:
        return 0
    if length == 2:
        return 2
    return get_count_b(length - 1) + get_count_c(length - 1)


def get_count_b(length):
    if length == 2:
        return 1
    return get_count_a(length-1) + get_count_c(length-1)


def get_count_c(length):
    if length == 2:
        return 1
    return get_count_a(length-1) + get_count_b(length-1)


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
    return get_count_a(length)


def gen_str_with_0(length):
    if length == 1:
        return ['0']
    temp = gen_str_with_1(length-1)
    for x in range(len(temp)):
        temp[x] = '0' + temp[x]
    return temp


def gen_str_with_1(length):
    if length == 1:
        return ['1']
    temp = gen_str_with_1(length-1) + gen_str_with_0(length-1)
    for x in range(len(temp)):
        temp[x] = '1' + temp[x]
    return temp


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    if type(length) is not int or length <= 0:
        raise ArgumentException('The parameter length must be an integer greater than 0')
    return gen_str_with_0(length) + gen_str_with_1(length)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
