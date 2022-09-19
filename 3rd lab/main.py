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
    if items is None:
        raise Exception("when the items value is None.")
    if len(items) == 0:
        return []
    return list(map(lambda x: "".join(str(e) for e in x), (__recursia(list(items), [[]].pop(0)))))


def __recursia(items: list[Any], itog: list[[Any]]) -> list[list]:
    if len(items) == 1:
        itog.append(items)
        return itog
    current = items.pop(0)
    itog = __recursia(items, itog)
    for i in range(len(itog)):
        itog[i].append(current)
    for k in range(len(itog)):
        for j in range(len(itog[-1]) - 1):
            itog.append(itog[k].copy())
            itog[-1][-1], itog[-1][j] = itog[-1][j], itog[-1][-1]
    return itog


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
