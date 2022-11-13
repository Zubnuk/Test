from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    if not (check_matrix(matrix)):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    if len(matrix) == 1:
        return matrix[0][0]
    return calc_det(matrix[0][0], matrix[0][1], matrix[1][0], len(matrix))


def check_matrix(matrix: list[list[int]]) -> bool:
    if matrix is None:
        return False
    if len(matrix) == 0:
        return False
    if len(matrix) == 1:
        return True
    if len(matrix) != len(matrix[0]):
        return False
    for y in range(len(matrix) - 1):
        if len(matrix[y]) != len(matrix[y + 1]):
            return False
    for i in range(len(matrix) - 1):
        if matrix[i][i] != matrix[0][0] or matrix[i][i + 1] != matrix[0][1] or matrix[i + 1][i] != matrix[1][0]:
            return False
    if matrix[-1][-1] != matrix[0][0]:
        return False
    row = 1
    for x in range(len(matrix) - 2):
        if matrix[row].count(0) != len(matrix) - 3:
            return False
        row = row + 1
    if matrix[0].count(0) != len(matrix) - 2 or matrix[-1].count(0) != len(matrix) - 2:
        return False
    return True


def calc_det(a, b, c, s):
    if s == 1:
        return a
    if s == 2:
        return a * a - b * c
    return a * calc_det(a, b, c, s - 1) - b * c * calc_det(a, b, c, s - 2)


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
