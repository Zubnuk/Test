import copy

from custom_exception import ArgumentException


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

    checker(profit_matrix)

    copy_profit = copy.deepcopy(profit_matrix)
    if len(copy_profit) == 1 and len(copy_profit[0]) == 1:
        return {"profit": copy_profit[0][0], "parts": [1]}

    matrix, points = [], []

    for column in range(0, len(profit_matrix[0]) - 1):
        points, point = [], ()
        temp_column = []

        for line in range(0, len(profit_matrix)):
            biggest_sum = copy_profit[line][column + 1]
            point = (0, line + 1)
            for row1 in range(0, line):
                row2 = line - row1 - 1
                if biggest_sum < copy_profit[row1][column] + copy_profit[row2][column + 1]:
                    biggest_sum = copy_profit[row1][column] + copy_profit[row2][column + 1]
                    point = (row1 + 1, row2 + 1)

            if biggest_sum < copy_profit[line][column]:
                biggest_sum = copy_profit[line][column]
                point = (line + 1, 0)

            temp_column.append(biggest_sum)
            points.append(point)

        matrix.append(points)

        for i in range(0, len(profit_matrix)):
            copy_profit[i][column + 1] = temp_column[i]

    max_invest = copy_profit[-1][-1]

    end = {"profit": max_invest, "parts": get_path(matrix)}
    return end


def get_path(matrix):
    index = matrix[-1][-1][0]
    answer = [matrix[-1][-1][1]]

    for path in range(len(matrix) - 2, -1, -1):
        if sum(answer) < len(matrix[0]):
            answer.append(matrix[path][index - 1][1])
            index = matrix[path][index - 1][0]
        else:
            answer.append(0)

    answer.append(index)
    answer.reverse()
    return answer


def checker(profit_matrix: list[list[int]]):
    if profit_matrix is None:
        raise ArgumentException('parameter is not an integer rectangle matrix')
    len_rows = len(profit_matrix)
    if len_rows == 0:
        raise ArgumentException('parameter is not an integer rectangle matrix')

    len_columns = len(profit_matrix[0])

    for row in profit_matrix:
        if len(row) != len_columns:
            raise ArgumentException('parameter is not an integer rectangle matrix')
        for value in row:
            if type(value) != int:
                raise ArgumentException('parameter is not an integer rectangle matrix')


def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
