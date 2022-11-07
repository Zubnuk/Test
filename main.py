import copy

from typing import List

from custom_exception import ArgumentException

def tridiagonal_determinant(matrix: List[List[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if matrix == [] or matrix == None:
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    n = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
    i = j = 0
    while i < n - 1:
        if matrix[i][j] != matrix[i + 1][j + 1]:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        i += 1
        j += 1
    i = 0
    j = 1
    while i < n - 2 or j < n - 2:
        if matrix[i][j] != matrix[i + 1][j + 1]:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        i += 1
        j += 1
    i = 1
    j = 0
    while i < n - 2 or j < n - 2:
        if matrix[i][j] != matrix[i + 1][j + 1]:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        i += 1
        j += 1
    for i in range(n):
        if (i == 0 or i == n - 1) and matrix[i].count(0) < n - 2:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        elif matrix[i].count(0) < n - 3:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
    a = matrix[0][0]
    if n == 1:
        return a
    b = matrix[1][0]
    c = matrix[0][1]
    if n == 2:
        return a ** 2 - b * c
    else:
        matrix_n_1 = copy.deepcopy(matrix)
        del matrix_n_1[0]
        for i in range(len(matrix_n_1)):
            del matrix_n_1[i][0]
        matrix_n_2 = copy.deepcopy(matrix_n_1)
        del matrix_n_2[0]
        for i in range(len(matrix_n_2)):
            del matrix_n_2[i][0]
        return a * tridiagonal_determinant(matrix_n_1) - b * c * tridiagonal_determinant(matrix_n_2)


def main():
    matrix = [[1, 2, 0, 0],
              [3, 1, 2, 0],
              [0, 3, 1],
              [0, 0, 3, 1]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()