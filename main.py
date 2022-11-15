from custom_exception import ArgumentException

PARAM_NOT_INT_OR_NOT_GREATER_THAN_ZERO = "The parameter length must be an integer greater than 0"


def error_handler(parameter):
    if type(parameter) is not int or parameter <= 0:
        raise ArgumentException(PARAM_NOT_INT_OR_NOT_GREATER_THAN_ZERO)


def rec_base(n) -> int:
    # базовый случай рекурсии для городов B и C
    return 1 if n == 1 or n == 2 else 0


def route_a(route_length) -> int:
    # взаимная рекурсия для города A
    # базовый случай рекурсии для города А другой, так как он стартовый
    return 0 if route_length < 2 else 2 if route_length == 2 else route_b(route_length - 1) + route_c(route_length - 1)


def route_b(route_length) -> int:
    # взаимная рекурсия для города B
    return rec_base(route_length) or route_a(route_length - 1) + route_c(route_length - 1)


def route_c(route_length) -> int:
    # взаимная рекурсия для города C
    return rec_base(route_length) or route_a(route_length - 1) + route_b(route_length - 1)


def get_triangle_path_count(length: int) -> int:
    """Calculates the number of closed routes of a target length between three
    vertices A, B and C that start and end at the A vertex. Аll paths between
    vertices A, B, and C are valid.
    :param length: a target route length.
    :raise ArgumentException: when the parameter length must is not an integer.
    greater than 0
    :return: the number of routes.
    """
    error_handler(length)
    return route_a(length)


def generate_strings_start_with_zero(length: int) -> list[str]:
    # взаимно рекурсивный проход всевозможных строк заданной длины length, начиная с нуля,
    # но с учетом условия, что двух нулей подряд быть не может
    return ["0"] if length == 1 else ["0" + strings for strings in generate_strings_start_with_one(length - 1)]


def generate_strings_start_with_one(length: int) -> list[str]:
    # взаимно рекурсивный проход всевозможных строк заданной длины length, начиная с единицы
    return ["1"] if length == 1 else ["1" + strings for strings in generate_strings_start_with_zero(length - 1)
                                      + generate_strings_start_with_one(length - 1)]


def generate_strings(length: int) -> list[str]:
    """Generates target lengthed strings consisting zeroes and ones
    non-duplicated zeroes.
    :param length: target string length.
    :raise ArgumentException: when integer is not equal or greater than zero.
    :return: the list of strings consisting zeroes and ones.
    """
    error_handler(length)
    return generate_strings_start_with_zero(length) + generate_strings_start_with_one(length)


def main():
    print(get_triangle_path_count(4))
    print(generate_strings(5))


if __name__ == '__main__':
    main()
