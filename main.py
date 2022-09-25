import time
from typing import Any


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def generate_permutations(items: frozenset[Any]) -> list[str]:
    if None in items:
        raise Exception("There is None Value in items!")
    s = list(items)
    s2 = []
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [str(s[0])]
    for item in s:
        pars = [i for i in s if i != item]
        list1 = generate_permutations(frozenset(pars))
        for k in list1:
            s2.append((str(item)) + str(k))
    return s2

def main():
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3})
    print_exec_time(lambda items: print(generate_permutations(items)),
                    items={1, 2, 3, 4, 5})


if __name__ == '__main__':
    main()
