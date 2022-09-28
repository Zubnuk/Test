import copy


class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def count_way(way_table: list[list[int]]) -> int:
    """
    :param way_table:  a matrix with information about ability vizit cell 0 - impossible 1 - possible
    :return: int value: the number of any path from the top left cell to the bottom right cell
    """
    if not matrix_checker(way_table):
        raise Exception('The price table is not a rectangular matrix with float values')
    row, col = len(way_table), len(way_table[0])
    if way_table[row - 1][col - 1] == 0:
        return 0
    matr_count = [[0 for i in range(col)] for j in range(row)]
    matr_count[0][0] = way_table[0][0]
    for i in range(1, row):
        matr_count[i][0] = way_table[i - 1][0] * way_table[i][0]
    for i in range(1, col):
        matr_count[0][i] = way_table[0][i - 1] * way_table[0][i]
    for i in range(1, row):
        for j in range(1, col):
            matr_count[i][j] = matr_count[i - 1][j] * way_table[i - 1][j] + matr_count[i][j - 1] * way_table[i][j - 1]
    return matr_count[row - 1][col - 1]


def get_min_cost_path(price_table: list[list[float]]) -> \
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    if not matrix_checker(price_table):
        raise Exception('The price table is not a rectangular matrix with float values')
    clear_matr = copy.deepcopy(price_table)
    for i in range(1, len(price_table)):
        clear_matr[i][0] += clear_matr[i - 1][0]
    for i in range(1, len(clear_matr[0])):
        clear_matr[0][i] += clear_matr[0][i - 1]
    for i in range(1, len(price_table)):
        for j in range(1, len(price_table[0])):
            clear_matr[i][j] += min(clear_matr[i - 1][j], clear_matr[i][j - 1])
    i, j = len(price_table) - 1, len(price_table[0]) - 1
    history = []
    while i + j != 0:
        history.append((i, j))
        pred = clear_matr[i][j] - price_table[i][j]
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if pred == clear_matr[i - 1][j]:
                i -= 1
            else:
                j -= 1
    history.append((0, 0))
    history.reverse()
    return {'cost': clear_matr[len(clear_matr) - 1][len(clear_matr[0]) - 1], 'path': history}


def matrix_checker(price_table) -> bool:
    if not (type(price_table) is list):
        return False
    if len(price_table) == 0:
        return False
    length = len(price_table[0])
    if length == 0:
        return False
    for i in price_table:
        if length != len(i) or not(all(isinstance(x, (int, float)) for x in i)):
            return False
    return True


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))
    test = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
            ]
    print(count_way(test))


if __name__ == '__main__':
    main()
