from custom_exception import ArgumentException
import copy

from typing import List


def invest_distribution(profit_matrix: list[list[int]]) -> dict[str: int, str: list[int]]:
    """Calculates the optimal distribution of investments between several
    projects. Investments are distributed in predetermined parts.

    :param profit_matrix: an integer matrix with profit values, investment
    levels as rows and the project index as columns;
    :raise ArgumentException: when parameter is not an integer rectangle matrix.
    :return: a dictionary with keys: profit - the max profit value, parts -
    a list with the part of investments for each project. The result example:
    {'profit': 73, 'parts': [1, 1, 2, 1]}
    """
    if profit_matrix is None or profit_matrix == []:
        raise ArgumentException("parameter is not an integer rectangle matrix")
    for i in range(1, len(profit_matrix)):
        if len(profit_matrix[i]) != len(profit_matrix[0]):
            raise ArgumentException("parameter is not an integer rectangle matrix")
        for j in range(len(profit_matrix[0])):
            if type(profit_matrix[i][j]) is not int:
                raise ArgumentException("parameter is not an integer rectangle matrix")
    if len(profit_matrix) == 1 and len(profit_matrix[0]) == 1:
        return {
            "profit": profit_matrix[0][0],
            "parts": [1]
        }
    profit_matrix_copy = copy.deepcopy(profit_matrix)
    profit_matrix_copy.insert(0, [0 for i in range(len(profit_matrix_copy[0]))])
    columns_count = len(profit_matrix_copy[0])
    current = []
    column = 1
    traces = []
    all_indexes = []
    all_results = []
    for i in range(len(profit_matrix_copy)):
        current.append([profit_matrix_copy[i][0], profit_matrix_copy[i][1]])
    column += 1
    for a in range(len(profit_matrix_copy[0]) - 1):
        max_results = [0]
        max_indexes = []
        for max_number in range(1, len(profit_matrix_copy)):
            maximum = 0
            index = ''
            for j in range(max_number + 1):
                k = max_number - j
                if current[j][0] + current[k][1] > maximum:
                    maximum = current[j][0] + current[k][1]
                    index = str(j) + str(k)
            max_results.append(maximum)
            max_indexes.append(index)
        if column < columns_count:
            for i in range(len(current)):
                current[i][0] = max_results[i]
                current[i][1] = profit_matrix_copy[i][column]
        column += 1
        del max_results[0]
        all_results.append(max_results)
        all_indexes.append(max_indexes)
    ind = ''
    max_copy = 0
    for j in range(len(all_results[0])):
        if all_results[-1][j] > max_copy:
            max_copy = all_results[-1][j]
            ind = all_indexes[-1][j]
    traces.append(int(ind[1]))
    current_ind = int(ind[0]) - 1
    if current_ind != -1:
        for i in range(len(all_indexes) - 2, -1, -1):
            ind = all_indexes[i][current_ind]
            traces.append(int(ind[1]))
            current_ind = int(ind[0]) - 1
        traces.append(int(ind[0]))
    else:
        for _ in range(len(profit_matrix_copy[0]) - 1):
            traces.append(0)
    traces = traces[::-1]
    result = {
        "profit": maximum,
        "parts": traces
    }
    return result


def main():
    profit_matrix = [[15, 18, 16, 17],
                  [20, 22, 23, 19],
                  [26, 28, 27, 25],
                  [34, 33, 29, 31],
                  [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
