from custom_exception import ArgumentException


def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    check(length)
    return a_amount(length)


def check(length):
    if length is None or str(length).isdigit() is False or length <= 0:
        raise ArgumentException('The parameter length must be an '
                                'integer greater than 0')


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    check(length)
    return list(set(set0("", length)+set1("", length)))


def set1(string, num):
    if num <= len(string):
        arr = []
        arr.append(string)
        return arr
    return set1(string + "1", num) + set0(string + "1", num)


def set0(string, num):
    if num <= len(string):
        arr = []
        arr.append(string)
        return arr
    return set1(string + "0", num)


def a_amount(num):
    if num == 0:
        return 1
    else:
        return b_amount(num - 1) + c_amount(num - 1)


def b_amount(num):
    if num <= 0:
        return 0
    else:
        return a_amount(num - 1) + c_amount(num - 1)


def c_amount(num):
    if num <= 0:
        return 0
    else:
        return b_amount(num - 1) + a_amount(num - 1)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
