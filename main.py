from custom_exception import ArgumentException


def calc_det(a, b, c, n):
    if n == 1:
        return a
    if n == 2:
        return a ** 2 - b * c
    else:
        return a * calc_det(a, b, c, n - 1) - b * c * calc_det(a, b, c, n - 2)


def is_rectangle(matrix: list[list[int]]) -> bool:
    horizontal_length = len(matrix[0])
    vertical_length = len(matrix)
    for horizontal_elements in matrix:
        if len(horizontal_elements) != horizontal_length \
                or len(horizontal_elements) != vertical_length:
            return False
    return True


def is_tridiagonal(matrix):
    a = matrix[0][0]
    b = matrix[1][0]
    c = matrix[0][1]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x - y == 1:
                if b != matrix[x][y]:
                    return False
            elif y - x == 1:
                if c != matrix[x][y]:
                    return False
            elif x == y:
                if a != matrix[x][y]:
                    return False
            elif matrix[x][y] != 0:
                return False
    return True


def check_matrix(matrix):
    if not matrix:
        raise ArgumentException('parameter is not a tridiagonal '
                                'integer matrix')
    if not is_rectangle(matrix):
        raise ArgumentException('parameter is not a tridiagonal '
                                'integer matrix')
    if len(matrix) != 1:
        if not is_tridiagonal(matrix):
            raise ArgumentException('parameter is not a tridiagonal '
                                    'integer matrix')


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal
           integer matrix
    :return: the value of the matrix determinant
    """
    check_matrix(matrix)
    if (len(matrix)) == 1:
        return matrix[0][0]
    n = len(matrix[0])
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    return calc_det(a, b, c, n)


def main():
    matrix = [[6, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [9, 6, -3, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 9, 6, -3, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 9, 6, -3, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 9, 6, -3, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 9, 6, -3, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 6, -3, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 6, -3, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 6, -3, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 6, -3],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 6]]

    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
