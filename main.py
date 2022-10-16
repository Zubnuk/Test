from custom_exception import ArgumentException
from copy import deepcopy

IS_NOT_INT_RECTANGLE_MATRIX_ERROR = "parameter is not an integer rectangle matrix"
PARTS = "parts"
PROFIT = "profit"

DICT = []  # dynamic store - сюда записываются промежуточные результаты вычислений


def error_handler(parameter):  # handle invalid parameter error
    if parameter is None:
        raise ArgumentException(IS_NOT_INT_RECTANGLE_MATRIX_ERROR)
    if len(parameter) == 0:
        raise ArgumentException(IS_NOT_INT_RECTANGLE_MATRIX_ERROR)
    for i in parameter:
        for j in i:
            if not (isinstance(j, int)):
                raise ArgumentException(IS_NOT_INT_RECTANGLE_MATRIX_ERROR)
    for y in range(len(parameter) - 1):
        if len(parameter[y]) != len(parameter[y + 1]):
            raise ArgumentException(IS_NOT_INT_RECTANGLE_MATRIX_ERROR)


def slice_col(matrix, col):  # утила - вырезает колонку из матрицы
    column = []
    for row in matrix:
        column.append(row[col])

    return column


def get_max_profit(profits_list):  # утила - находит объект {profit: ..., parts: ...} с максимальным значение profit
    max_profit = profits_list[0]
    for profit in profits_list:
        if profit[PROFIT] > max_profit[PROFIT]:
            max_profit = profit

    return max_profit


def init_dict(col):  # инициализация dynamic store
    for idx in range(len(col)):
        DICT.append({PROFIT: col[idx], PARTS: [idx + 1]})


def update_dict(col):  # обновление значений в dynamic store
    new_dict = []
    for idx in range(len(col)):
        profit = calc_intermediate_profit(col, idx)
        parts = profit[PARTS]
        new_parts = []
        if parts[0] - 1 == -1:
            for i in range(len(DICT[idx][PARTS])):
                new_parts.append(0)
        else:
            new_parts = deepcopy(DICT[parts[0] - 1][PARTS])

        new_parts.append(parts[1])
        new_dict.append({
            PROFIT: profit[PROFIT],
            PARTS: new_parts
        })

    for i in range(len(new_dict)):
        DICT[i] = new_dict[i]


def calc_intermediate_profit(col, idx):  # перебор значений по бюджету (возвращает максимальное значение)
    first_budget = -1
    second_budget = idx
    profits_list = []

    while first_budget != idx + 1:
        if first_budget == -1:
            profits_list.append({
                PROFIT: col[second_budget],
                PARTS: [0, second_budget + 1]
            })
        elif second_budget == -1:
            profits_list.append({
                PROFIT: DICT[first_budget][PROFIT],
                PARTS: [first_budget + 1, 0]
            })
        else:
            profits_list.append({
                PROFIT: DICT[first_budget][PROFIT] + col[second_budget],
                PARTS: [first_budget + 1, second_budget + 1]
            })

        first_budget += 1
        second_budget -= 1

    return get_max_profit(profits_list)


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

    error_handler(profit_matrix)  # handle invalid parameter error
    init_dict(slice_col(profit_matrix, 0))

    for col_idx in range(1, len(profit_matrix[0])):
        update_dict(slice_col(profit_matrix, col_idx))

    return get_max_profit(DICT)


def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
