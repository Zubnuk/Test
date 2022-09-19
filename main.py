import time
from typing import Any


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def generate_permutations(items: frozenset[Any]) -> list[str]:
    mas = []
    mas = set(items)
    ma_2 = []

    def permutation(s):
        if len(s) == 1:
            return [s]

        perm_list = []
        for a in s:
            remaining_elements = [x for x in s if x != a]
            z = permutation(remaining_elements)

            for t in z:
                perm_list.append([a] + t)

        return perm_list

    arr = mas

    for line in permutation(arr):
        t = str(line)
        m = ""
        for i in line:
            m += str(i)

        ma_2.append(m)

    return ma_2


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
