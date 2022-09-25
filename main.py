import time
from typing import Any


def get_permutation(sequence):
    length_sequence = len(sequence)
    help_sequence = sequence[::]
    index_sequence = list(range(length_sequence))
    null_sequence = [0] * (length_sequence + 1)
    while True:
        yield help_sequence
        k = 1
        while null_sequence[k] == k:
            null_sequence[k] = 0
            k += 1
        if k == length_sequence:
            return
        null_sequence[k] += 1
        help_sequence[0], help_sequence[index_sequence[k]] = \
            help_sequence[index_sequence[k]], help_sequence[0]
        j = 1
        k = k - 1
        while j < k:
            index_sequence[j], index_sequence[k] = \
                index_sequence[k], index_sequence[j]
            j += 1
            k -= 1


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
        raise Exception("None error")
    if len(items) == 0:
        return []
    permutation_sequences = []
    for sequence in get_permutation(list(items)):
        permutation_sequences.append("".join(map(str, sequence)))
    return permutation_sequences


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
