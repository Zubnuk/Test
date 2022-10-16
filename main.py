from custom_exception import ArgumentException


def __matrix_check(matrix: list[list[int]]) -> bool:  # matrix order check
    if matrix is None:
        return False
    if len(matrix) < 1:
        return False
    for i in range(len(matrix)):
        for element in matrix[i]:
            if type(element) is not int:
                return False
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return False
    return True


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
    if not __matrix_check(profit_matrix):
        raise ArgumentException('parameter is not an integer rectangle matrix.')
    dictionary = {'profit': 0, 'parts': []}
    parts = [[]]
    buff = [[]]
    for i in range(len(profit_matrix) + 1):
        buff.append(list())
        for j in range(len(profit_matrix[0])):
            buff[i].append(0)
    buff.pop()
    for i in range(1, len(buff)):
        for j in range(len(buff[0])):
            buff[i][j] = profit_matrix[i - 1][j]
    # Есть матрица как начальная, но первая строчка - нули
    for i in range(1, len(buff[0])):  # Кол-во сверток-сжатий
        parts.append([])
        list_for_maxs = []  # Значения после сжатия
        for j in range(len(buff)):
            maxInTwoCols = 0
            maxInTwoColsParts = []
            for k in range(j + 1):
                if (buff[k][i - 1] + buff[j - k][i]) > maxInTwoCols:
                    maxInTwoCols = (buff[k][i - 1] + buff[j - k][i])
                    maxInTwoColsParts = [k, j - k]
            list_for_maxs.append(maxInTwoCols)
            parts[i].append(maxInTwoColsParts)
        parts[i].pop(0)
        for j in range(len(list_for_maxs)):
            buff[j][i] = list_for_maxs[j]
    parts.pop(0)
    if len(profit_matrix[0]) == 1:
        parts.append([len(profit_matrix)])
        dictionary['profit'] = int(buff[-1][-1])  # Profit найден
        dictionary['parts'] = parts[0]
        return dictionary
    else:
        bufparts = []
        bufparts.append(parts[-1][-1])
        for i in range(1, len(parts)):
            bufparts.append(parts[len(parts) - 1 - i][bufparts[-1][0] - 1])
        itogparts = []
        for i in range(len(bufparts)):
            if bufparts[i][0] == 0:
                itogparts.append(bufparts[i][1])
                for j in range(len(bufparts) - i):
                    itogparts.append(0)
                break
            elif (i != len(bufparts) - 1):
                itogparts.append(bufparts[i][1])
            else:
                itogparts.append(bufparts[i][1])
                itogparts.append(bufparts[i][0])
        itogparts.reverse()

    dictionary['profit'] = int(buff[-1][-1])  # Profit найден
    dictionary['parts'] = itogparts
    return dictionary


def main():
    profit_matrix = [[15, 18, 16, 17],
                     [20, 22, 23, 19],
                     [26, 28, 27, 25],
                     [34, 33, 29, 31],
                     [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
