from custom_exception import ArgumentException

IS_NOT_TRIDIAGONAL_MATRIX_ERROR = "parameter is not a tridiagonal integer matrix"


def error_handler(matrix: list[list[int]]):
    error = ArgumentException(IS_NOT_TRIDIAGONAL_MATRIX_ERROR)

    if matrix is None:
        raise error
    if len(matrix) == 0:
        raise error

    row_count = len(matrix)
    col_count = len(matrix[0])

    # не продолжать, если единичная матрица
    if row_count == 1:
        return

    if row_count != col_count:
        raise error

    # проверка элементов верхнего правого угла и левого нижнего
    if matrix[0][-1] != matrix[-1][0]:
        raise error

    for row in range(row_count - 1):
        # проверка, что все строки одинаковой длины
        if len(matrix[row]) != len(matrix[row + 1]):
            raise error

        # проверка элементов по диагонали (что все равны)
        for col in range(col_count - 1):
            if matrix[row][col] != matrix[row + 1][col + 1]:
                raise error


def rec_tridiagonal_determinant(a: int, b: int, c: int, n: int) -> int:
    """Calculates the value of the tridiagonal matrix determinant !recursively!
    :param a: matrix element
    :param b: matrix element
    :param c: matrix element
    :param n: matrix dimension
    :return: the value of the matrix determinant
    """
    if n == 1:
        return a
    elif n == 0:
        return 1

    return a * rec_tridiagonal_determinant(a, b, c, n - 1) - b * c * rec_tridiagonal_determinant(a, b, c, n - 2)


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """

    error_handler(matrix)

    if len(matrix) == 1:
        return matrix[0][0]

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    n = len(matrix)

    return rec_tridiagonal_determinant(a, b, c, n)


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
