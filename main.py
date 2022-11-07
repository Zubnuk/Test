from custom_exception import ArgumentException


def detByValue(a: int, b: int, c: int, n: int):
    if n == 2:
        return a * a - b * c
    if n == 1:
        return a
    return a * detByValue(a, b, c, n - 1) - b * c * detByValue(a, b, c, n - 2)


def checkerDiagonals(a: int, b: int, c: int, matr: list[list[int]]):
    if len(matr) == 2:
        if matr[0][0] != a or matr[0][1] != b or matr[1][0] != c:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        else:
            return

    if matr[0][0] != a or matr[1][0] != c or matr[0][1] != b:
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    if matr[0][2:].count(0) != len(
            matr[0][2:]):  # Если количество 0 не равно длине, то на горизонтальной линии есть что-то, кроме 0
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    firstColumn = [i[0] for i in matr[2:]]
    if firstColumn.count(0) != len(firstColumn):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    newMatr = [i[1:] for i in matr[1:]]
    checkerDiagonals(a, b, c, newMatr)


def checker(tridiagonalMatrix: list[list[int]]):
    if not (type(tridiagonalMatrix) is list):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    if len(tridiagonalMatrix) == 0:
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    length = len(tridiagonalMatrix)
    for i in tridiagonalMatrix:
        if not (type(i) is list):
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        if len(i) != length:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        for j in i:
            if not (type(j) is int):
                raise ArgumentException('parameter is not a tridiagonal integer matrix')


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    checker(matrix)
    if len(matrix) == 1:
        return matrix[0][0]
    checkerDiagonals(matrix[0][0], matrix[0][1], matrix[1][0], matrix)
    return detByValue(matrix[0][0], matrix[0][1], matrix[1][0], len(matrix))

    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    pass


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
