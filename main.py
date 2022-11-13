from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    exception_message = 'parameter is not a tridiagonal integer matrix'
    if matrix is None:
        raise ArgumentException(exception_message)
    if len(matrix) == 0:
        raise ArgumentException(exception_message)
    if len(matrix[0]) != len(matrix):
        raise ArgumentException(exception_message)
    for i in range(len(matrix) - 1):
        dl = len(matrix[i])
        if dl != len(matrix[i + 1]):
            raise ArgumentException(exception_message)
    if len(matrix) == 1:
        return matrix[0][0]
    if matrix[0][-1] != matrix[-1][0]:
        raise ArgumentException(exception_message)
    for row in range(len(matrix) - 1):
        for column in range(len(matrix[0]) - 1):
            elem = matrix[row][column]
            if elem != matrix[row + 1][column + 1]:
                raise ArgumentException(exception_message)

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    n = len(matrix)

    def determinant(a, b, c, n):
        if n == 2:
            return a * a - b * c
        if n == 1:
            return a
        return a * determinant(a, b, c, n - 1) - b * c * determinant(a, b, c, n - 2)

    return determinant(a, b, c, n)


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
