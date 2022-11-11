from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if matrix is None:
        raise ArgumentException("parameter is not a tridiagonal integer matrix")

    elif len(matrix) == 0:
        raise ArgumentException("parameter is not a tridiagonal integer matrix")

    leight_matrix = len(matrix)
    for i in range(len(matrix)):
        if len(matrix[i]) != leight_matrix:
            raise ArgumentException("parameter is not a tridiagonal integer matrix")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            if matrix[i][0] == 0:
                continue
            else:
                if matrix[i][j] == 0 and matrix[i][j+1] != 0:
                    raise ArgumentException("parameter is not a tridiagonal integer matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]

    elif len(matrix) > 2:
        matr = [matrix[0][0], matrix[0][1], matrix[1][0]]
        for i in range(len(matrix)-1):
            if matrix[i][i] != matr[0] or matrix[i+1][i] != matr[2] or matrix[i][i+1] != matr[1]:
                raise ArgumentException("parameter is not a tridiagonal integer matrix")

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    n = len(matrix)
    return rec_mat_model(a, b, c, n)


def rec_mat_model(a, b, c, n):
    if n == 1:
        return a
    elif n == 2:
        return a * a - b * c
    else:
        return a * rec_mat_model(a, b, c, n-1) - b * c * rec_mat_model(a, b, c, n-2)


def main():
    matrix = [[1, 2, 0, 0],
              [3, 1, 2, 0],
              [0, 3, 1, 2],
              [0, 0, 3, 1]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
