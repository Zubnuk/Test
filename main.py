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


def recur_det(matrix: [[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if len(matrix) > 2:
        det = matrix[0][0] * recur_det(str_col_remover(matrix, 1)) - matrix[0][1] * matrix[1][0] * recur_det(str_col_remover(matrix, 2))
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
    return recur_det(matrix)


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))
