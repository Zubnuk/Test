import time
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
    if None in items:
        raise Exception("встретился None в списке")
    items = list(items)
    if len(items) == 1:
        return [str(items[0])]
    results = []
    for item in items:
        other_items = [i for i in items if i != item]
        permutations = generate_permutations(frozenset(other_items))
        for permutation in permutations:
            results.append(str(item) + str(permutation))
    return results


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
