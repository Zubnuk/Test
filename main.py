import copy
import time
from math import factorial
from typing import Any


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def generate_permutations(items: frozenset[Any]) -> list[str]:
    """Generates all permutations by a set of items.

    :param items: a frozenset(immutable) with some items.
    :raise Exception: when the items value is None.
    :return: a list with permutation strings.
    """
    if items is None:
        raise Exception("...")
    if len(items) in (0, 1):
        answer = list(map(str, items))
        return answer

    main_array = []
    for value in items:
        main_array.append(str(value))

    steps = [[[main_array[0]]]]

    for main_index in range(len(main_array) - 1):
        new_step = []
        for _ in range(factorial(main_index + 2)):
            buffer = copy.deepcopy(steps[main_index][_ % factorial(main_index + 1)])
            new_step.append(buffer)
        new_step.sort()

        insert_index = 0
        for permutation_index in range(len(new_step)):
            new_step[permutation_index].insert(insert_index, main_array[main_index + 1])
            insert_index += 1
            if insert_index == main_index + 2:
                insert_index = 0
        insert_index = 0

        steps.append(new_step)

    answer = list(map(''.join, steps[-1]))
    answer = list(set(answer))

    return answer


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
