import math
import time
from typing import Any


def print_exec_time(func: callable(object), **kwargs) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

def generate_permutations(items):
    """Generates all permutations by a set of items.

    :param items: a frozenset(immutable) with some items.
    :raise Exception: when the items value is None.
    :return: a list with permutation strings.
    """
    arr = list(items)
    length = len(arr)
    quant = factorial(length)
    result = []

    if length == 0:
        return result

    for i in range(1, quant + 1):
        s = ""
        symbols_left = length
        temp_arr = arr.copy()
        period = 1

        for j in range(length):
            period *= symbols_left
            position = (math.ceil(i * period / quant) - 1) % symbols_left
            s += str(temp_arr[position])
            temp_arr.pop(position)
            symbols_left -= 1
        result.append(s)
    return result


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
