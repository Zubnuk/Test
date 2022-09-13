import copy
import time
from typing import Any


def fibonacci_rec(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Recursive implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_rec(num - 2) + fibonacci_rec(num - 1)



def fibonacci_iter(num: int) -> int:
    """Returns the fibonacci number according to the number specified in the
    parameter. Iterative implementation.

    :param num: the ordinal number of the fibonacci number
    :return: a fibonacci number
    """
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        prev1 = prev2 = 1
        for i in range(3, num):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2



def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant
    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """
    length = len(matrix)
    for i in range(length):
        if len(matrix[i]) != length:
            raise Exception("Матрица не квадратная")
    if length == 1:
        return matrix[0][0]
    if length == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0

    for i in range(len(matrix)):
        result += matrix[0][i] * pow(-1, i) * determinant(det_matrix(matrix, 0, i))

    return result


def det_matrix(matrix: [[int]], i, j):
    """Creates matrix without selected row and column
        :param i: row number
        :param j: column number
        :param matrix: an integer matrix
        :return: new matrix without row i and column j
        """
    new_matrix = copy.deepcopy(matrix)
    del new_matrix[i]
    for i in range(0, len(new_matrix)): del new_matrix[i][j]
    return new_matrix


# def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
#     start_time = time.time()
#     func(**kwargs)
#     print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_rec(x)), x=num)

    matrix = [[1, 2],
              [3, 4]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
