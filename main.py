def gcd_recursive(first_number: int, second_number: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Recursive implementation.

    :param first_number: first number
    :param second_number: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if first_number is None or second_number is None:
        raise Exception("Can't find the greatest common divisor of None.")

    # Base
    if first_number == second_number:
        return first_number
    if first_number * second_number == 0:
        return first_number + second_number

    if first_number < second_number:
        first_number, second_number = second_number, first_number

    return gcd_recursive(first_number - second_number, second_number)


def gcd_iterative_slow(first_number: int, second_number: int) -> int:
    """Calculates the greatest common divisor of two numbers.
    Iterative implementation using subtraction.

    :param first_number: first number
    :param second_number: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if first_number is None or second_number is None:
        raise Exception("Can't find the greatest common divisor of None.")

    if first_number == second_number:
        return first_number
    if first_number * second_number == 0:
        return first_number + second_number

    while first_number != second_number and first_number * second_number != 0:
        if first_number < second_number:
            first_number, second_number = second_number, first_number
        first_number -= second_number
    return first_number


def gcd_iterative_fast(first_number: int, second_number: int) -> int:
    """Calculates the greatest common divisor of two numbers
    Iterative implementation using division.

    :param first_number: first number
    :param second_number: second number
    :except Exception: when a or b value is None
    :return: greatest common divisor
    """
    if first_number is None or second_number is None:
        raise Exception("Can't find the greatest common divisor of None.")

    while second_number:
        first_number, second_number = second_number, first_number % second_number
    return first_number


def lcm(first_number: int, second_number: int) -> int:
    """Calculates the least common multiple of two numbers

    :param first_number: first number
    :param second_number: second number
    :except Exception: when a or b value is None
    :return: the least common multiple
    """
    if first_number is None or second_number is None:
        raise Exception("Can't find the least common multiple of None.")

    return int((first_number * second_number) / gcd_iterative_fast(first_number, second_number))


def main():
    print(gcd_recursive(1005002, 1354))


if __name__ == '__main__':
    main()
