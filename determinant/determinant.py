def determinant(matrix: [[int]]) -> int:
    """Calculates the value of the matrix determinant

    :param matrix: an integer matrix
    :raise Exception: when the parameter value is not a square matrix
    :return: the value of the matrix determinant
    """

    if __is_not_square_matrix(matrix):
        raise Exception("The parameter value is not a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    row_idx = __choose_row(matrix)
    result = 0
    for column_idx, value in enumerate(matrix[row_idx]):
        if value != 0:
            result += value * __co_factor(matrix, row_idx, column_idx)
    return result


def __is_not_square_matrix(matrix: [[int]]) -> bool:
    if type(matrix) != list or not matrix or type(matrix[0]) != list:
        return True
    first_row_len = len(matrix[0])
    if first_row_len != len(matrix):
        return True
    for row in matrix:
        if type(row) != list or len(row) != first_row_len:
            return True
    return False


def __choose_row(matrix: [[int]]) -> int:
    max_zero_cnt = 0
    target_row_idx = 0
    for idx, row in enumerate(matrix):
        zero_cnt = 0
        for value in row:
            zero_cnt += bool(value == 0)
        target_row_idx = idx if zero_cnt > max_zero_cnt else target_row_idx
        max_zero_cnt = max(zero_cnt, max_zero_cnt)
    return target_row_idx


def __co_factor(matrix: [[int]], row_idx: int, column_idx: int) -> int:
    if len(matrix) < 2:
        raise Exception("Can't calculate co_factor for if matrix order is less"
                        "than 2")
    reduced_matrix = [[val for idx, val in enumerate(row) if idx != column_idx]
                      for idx, row in enumerate(matrix) if idx != row_idx]
    i = row_idx + 1
    j = column_idx + 1
    return (-1)**(i + j) * determinant(reduced_matrix)
