import time
import turtle
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
    s = list(items)
    for i in range(len(s)):
        s[i] = str(s[i])
    if len(items) == 0:
        return []
    if items is None: 
        raise Exception("Items value is None.")
    if len(items) == 1:
        return [s[0]]
    resul = []
    for i in range(len(s)):
       m = s[i]
 
       remLst = s[:i] + s[i+1:]
    
       for p in generate_permutations(remLst):
            resul.append(m + p)
    new_resul=[]
    num = ""
    for i in resul:
        for iyem in i:
            num+=str(iyem)
        new_resul.append(num)
        num = ""
    return new_resul
        



def main():
    print(generate_permutations(frozenset(('a', 'b', 'c'))))
    # print_exec_time(lambda items: print(generate_permutations(items)),
    #                 items=[1,2,3,4,5])


if __name__ == '__main__':
    main()
