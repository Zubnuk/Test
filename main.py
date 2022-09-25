import time
from typing import Any


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def generate_permutations(items: frozenset[Any]) -> list[str]:

    if items is None:
        raise Exception("Элементы отсутствуют")
    if len(items) == 0:
        return []
    return list(map(lambda s: "".join(str(x) for x in s), (permutation(list(items), [[]].pop(0)))))


def permutation(items: list[Any], result: list[[Any]]) -> list[list]:
    if len(items) == 1:
        result.append(items)
        return result
    current = items.pop(0)
    result = permutation(items, result)
    for i in range(len(result)):
        result[i].append(current)
    for z in range(len(result)):
        for v in range(len(result[-1]) - 1):
            result.append(result[z].copy())
            result[-1][-1], result[-1][v] = result[-1][v], result[-1][-1]
    return result

    """mas = []
    mas = list(items)
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

    arr = unique_permutations(mas)

    for line in permutations(arr):
        t = str(line)
        m = ""
        for i in line:
            m += str(i)

        ma_2.append(m)
        
    return ma_"""


def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
