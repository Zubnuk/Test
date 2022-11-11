from custom_exception import ArgumentException


def is_tridiagonal(matrix: [[int]]) -> bool:
    if matrix is None:  # None
        return False

    if len(matrix) == 0:  # len = 0
        return False

    for i in range(len(matrix)):  # not rectangle
        if len(matrix[i]) != len(matrix):
            return False
    for i in range(len(matrix)):  # main diag
        if matrix[i][i] != matrix[0][0]:
            return False
    if len(matrix) < 3:
        return True
    for i in range(len(matrix) - 1):  # low diag
        if matrix[i + 1][i] != matrix[1][0]:
            return False
        for j in range(i - 1):
            if matrix[i + 1][j] != 0 and i > 1:
                return False
    for i in range(len(matrix) - 1):  # high diag
        if matrix[i][i + 1] != matrix[0][1]:
            return False
        for j in range(i - 1):
            if matrix[j][i + 1] != 0 and i > 1:
                return False
    return True


def recur_det(a, b, c, n) -> int:
    if n == 1:
        return a

    if n == 2:
        return a * a - b * c

    if n > 2:
        det = a * recur_det(a, b, c, n - 1) - b * c * recur_det(a, b, c, n - 2)
        return det


def str_col_remover(matrix: [[int]], num: int) -> [[int]]:
    matr = [[]]
    matr.pop()
    for i in range(num, len(matrix)):
        matr.append([])
        for j in range(num, len(matrix)):
            matr[-1].append(matrix[i][j])
    return matr


def tridiagonal_determinant(matrix: [[int]]) -> int:
    if not is_tridiagonal(matrix):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    if len(matrix) > 1:
        a = matrix[0][0]
        b = matrix[1][0]
        c = matrix[0][1]
        n = len(matrix)
        return recur_det(a, b, c, n)
    else:
        return matrix[0][0]


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))
