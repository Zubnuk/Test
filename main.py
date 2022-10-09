from custom_exception import ArgumentException
from copy import deepcopy


def is_rectangle(profit_matrix: list[list[int]]) -> bool:
    vertical_length = len(profit_matrix)
    if vertical_length == 0:
        return False
    horizontal_length = len(profit_matrix[0])
    for horizontal_elements in profit_matrix:
        if len(horizontal_elements) != horizontal_length:
            return False
    return True


def is_float(profit_matrix: list[list[int]]) -> bool:
    for horizontal_elements in profit_matrix:
        for element in horizontal_elements:
            if type(element) != int:
                return False
    return True


def is_right(profit_matrix: list[list[int]]):
    if not profit_matrix:
        raise ArgumentException('parameter is not an integer rectangle matrix')
    if not is_rectangle(profit_matrix):
        raise ArgumentException('parameter is not an integer rectangle matrix')
    if not is_float(profit_matrix):
        raise ArgumentException('parameter is not an integer rectangle matrix')


def calc_max_profit(first_company, second_company, budget):
    first_budget = budget
    second_budget = 0
    profit_list = []
    while second_budget != budget + 1:
        profit_list.append(
            first_company[first_budget] + second_company[second_budget])
        first_budget -= 1
        second_budget += 1
    max_index = profit_list.index(max(profit_list))
    return {
        "max_budget": max(profit_list),
        "part": max_index
    }


def slice_matrix_horizontal(matrix, horizontal):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][:horizontal + 1]
    return matrix


def calc_parts(profit_matrix, part):
    parts = [0] * (len(profit_matrix) - 1) + [part]
    index = len(parts) - 2
    budget = len(profit_matrix[0]) - parts[-1] - 1
    while budget != 0:
        profit_matrix.pop()
        slice_matrix_horizontal(profit_matrix, budget)
        parts[index] = calc_max_profit_matrix(deepcopy(profit_matrix), None)["part"]
        budget -= parts[index]
        index -= 1
    return parts


def calc_max_profit_matrix(profit_matrix: list[list[int]], part):
    if len(profit_matrix) == 1:
        if part is None:
            part = len(profit_matrix[0]) - 1
        return {'profit': profit_matrix[0][-1],
                'part': part}
    else:
        profit_matrix.insert(0, [0] * len(profit_matrix[0]))
        for i in range(len(profit_matrix[0]) - 1):
            max_profit = calc_max_profit(profit_matrix[1],
                                         profit_matrix[2], i + 1)
            part = max_profit["part"]
            profit_matrix[0][i + 1] = max_profit["max_budget"]
        profit_matrix.pop(1)
        profit_matrix.pop(1)
        return calc_max_profit_matrix(profit_matrix, part)


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    transposed_matrix = [
        [0] * (len(matrix) + 1) for _ in range(len(matrix[0]))
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i + 1] = matrix[i][j]
    return transposed_matrix


def invest_distribution(profit_matrix: list[list[int]]) -> \
        dict[str: int, str: list[int]]:
    """Calculates the optimal distribution of investments between several
    projects. Investments are distributed in predetermined parts.

    :param profit_matrix: an integer matrix with profit values, investment
    levels as rows and the project index as columns;
    :raise ArgumentException: when parameter is not an integer rectangle matrix.
    :return: a dictionary with keys: profit - the max profit value, parts -
    a list with the part of investments for each project. The result example:
    {'profit': 73, 'parts': [1, 1, 2, 1]}
    """
    is_right(profit_matrix)
    result = calc_max_profit_matrix(transpose_matrix(profit_matrix), None)
    profit = result["profit"]
    part = result["part"]
    parts = calc_parts(transpose_matrix(profit_matrix), part)
    return {
        'profit': profit,
        'parts': parts
    }


def main():
    matrix = [[5, 3, 7, 6],
              [9, 10, 11, 12],
              [17, 21, 23, 16],
              [28, 35, 32, 29],
              [42, 42, 42, 43]]
    print(invest_distribution(matrix))


if __name__ == '__main__':
    main()
