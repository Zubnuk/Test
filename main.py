from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Calculates the value of the tridiagonal matrix determinant
    :param matrix: an integer tridiagonal square matrix
    :raise ArgumentException: when parameter is not a tridiagonal integer matrix
    :return: the value of the matrix determinant
    """
    checker(matrix)
    return det(matrix)


def det(matrix: list[list[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        smaller_matrix1, smaller_matrix2 = [], []
        for row in range(0, len(matrix) - 1):
            smaller_matrix1.append(matrix[row][0:-1])
        for row in range(0, len(matrix) - 2):
            smaller_matrix2.append(matrix[row][0:-2])
        return matrix[0][0] * det(smaller_matrix1) - matrix[0][1] * matrix[1][0] * det(smaller_matrix2)


def checker(matrix: list[list[int]]) -> bool:
    check_int_square(matrix)
    if len(matrix) == 1:
        return True
    main_number, up_number, down_number = matrix[0][0], matrix[0][1], matrix[1][0]

    # формируем массив, по которому будем перемещаться слайсом
    check_array = [0]*(3+(len(matrix)-2)*2)
    check_array[(len(check_array)-1)//2] = main_number
    check_array[((len(check_array) - 1) // 2) - 1] = down_number
    check_array[((len(check_array) - 1) // 2) + 1] = up_number

    for i in range(len(matrix)):
        if matrix[i] != check_array[-len(matrix) - i:len(check_array)-i]:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')


def check_int_square(matrix: list[list[int]]):
    if matrix is None or len(matrix) == 0 or len(matrix[0]) != len(matrix):
        raise ArgumentException('parameter is not a tridiagonal integer matrix')
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise ArgumentException('parameter is not a tridiagonal integer matrix')
        for column_value in row:
            if type(column_value) != int:
                raise ArgumentException('parameter is not a tridiagonal integer matrix')


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
