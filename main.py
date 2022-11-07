from custom_exception import ArgumentException


def checkerDiagonals(a:int, b:int, c:int,matr:list[list[int]])->bool:
    if len(matr) == 2:
        if matr[0][0] == a and matr[0][1] == b and matr[1][0] == c:
            return True
        else:
            return False
    if matr[0][0] != a or matr[1][0] != c or matr[0][1] != b:
        return False
    if matr[0][2:].count(0) != len(matr[0][2:]):
        return False
    firstColumn = [i[0] for i in matr[2:]]
    if firstColumn.count(0) != len(firstColumn):
        return False
    newMatr = [i[1:] for i in matr[1:]]
    return checkerDiagonals(a, b, c, newMatr)




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
    if not checkerDiagonals(matrix[0][0], matrix[0][1], matrix[1][0],matrix):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0]*matrix[0][1]
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    matrMinus2 = matrix[2:]
    matrMinus2 = [i[2:] for i in matrMinus2]
    matrMinus1 = matrix[1:]
    matrMinus1 = [i[1:] for i in matrMinus1]
    return a*tridiagonal_determinant(matrMinus1) - b*c*tridiagonal_determinant(matrMinus2)



    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    pass


def main():
    matrix = [[2, -3, 0, 0],
              [1, 2, -3, 0],
              [0, 1, 2, -3],
              [0, 0, 1, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
