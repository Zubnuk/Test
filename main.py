import time
from typing import Any, List, FrozenSet


def print_exec_time(func: callable(object), **kwargs) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def swap_list_elements(items: List[Any], a: int, b: int):
    """
    Swap items element by indexes.

    :param items: list with some items.
    :param a: index of items element.
    :param b: index of items element.
    """
    temp = items[a]
    items[a] = items[b]
    items[b] = temp


def permutations_rec(items: List[Any], idx: int = 0) -> List[str]:
    """
    Recursive permutation generation.

    Пользуясь Поиском с возвратом, заменяем каждый из оставшихся элементов в массиве его первым элементом
    и генерируем все перестановки оставшихся элементов с помощью рекурсивного вызова.

    :param items: list with some items.
    :param idx: kind of current position.
    :return: list with permutation strings.
    """
    result = []
    if idx == len(items) - 1:
        result.append(''.join(map(str, items)))

    for i in range(idx, len(items)):
        swap_list_elements(items, idx, i)
        result.extend(permutations_rec(items, idx + 1))
        swap_list_elements(items, idx, i)

    return result


def generate_permutations(items: FrozenSet[Any]) -> List[str]:
    """Generates all permutations by a set of items.

    :param items: a frozenset(immutable) with some items.
    :raise Exception: when the items value is None.
    :return: a list with permutation strings.
    """
    if items is None or None in items:
        raise Exception("There is None value in items")
    if not len(items):
        return []

    return permutations_rec(list(items))


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
