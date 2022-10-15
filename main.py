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

    if profit_matrix is None:
        raise ArgumentException('parameter is not an integer rectangle matrix')

    if len(profit_matrix) == 0:
        raise ArgumentException('parameter is not an integer rectangle matrix')

    for i in profit_matrix:
        for j in i:
            if not (isinstance(j, int)):
                raise ArgumentException('parameter is not an integer rectangle matrix')

    for y in range(len(profit_matrix) - 1):
        if len(profit_matrix[y]) != len(profit_matrix[y + 1]):
            raise ArgumentException('parameter is not an integer rectangle matrix')

    t = profit_matrix
    a = [[0 for i in range(len(t[0]) + 1)] for j in range(len(t) + 1)]
    r = [[[0] * i for i in range(len(t[0]) + 1)] for j in range(len(t) + 1)]
    for j in range(1, len(a[0])):
        for i in range(1, len(a)):
            a[i][j] = t[i - 1][j - 1]
            imax = 0
            step = []
            for x in range(i + 1):
                temp = a[x][j]
                if x != 0:
                    a[x][j] = t[x - 1][j - 1]
                if imax <= a[x][j] + a[i - x][j - 1]:
                    imax = a[x][j] + a[i - x][j - 1]
                    step = [i - x, x]
                a[x][j] = temp
            r[i][j] = r[step[0]][j - 1] + [step[1]]
            a[i][j] = imax
    return {'profit': a[-1][-1], 'parts': r[-1][-1]}


def main():
    profit_matrix = [[5, 4, 4, 7],
                     [6, 22, 8, 12],
                     [1, 10, 15, 12],
                     [1, 12, 23, 15],
                     [6, 15, 42, 18]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
