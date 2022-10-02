class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def get_min_cost_path(price_table: list[list[float]]) -> \
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    if price_table is None:
        raise Exception('The price table is not a rectangular matrix with float values')
    if len(price_table) == 0 or not (isinstance((price_table[0][0]), float)):
        raise Exception('The price table is not a rectangular matrix with float values')
    for y in range(len(price_table) - 1):
        if len(price_table[y]) != len(price_table[y + 1]):
            raise Exception('The price table is not a rectangular matrix with float values')
    t = price_table
    a = [[float('inf') for i in range(len(t[0]) + 1)] for j in range(len(t) + 1)]
    a[1][1] = t[0][0]
    for i in range(1, len(t) + 1):  # 1
        for j in range(1, len(t[0]) + 1):  # 3
            a[i][j] = min(a[i][j - 1], a[i - 1][j]) + t[i - 1][j - 1]
            if i == 1 and j == 1:
                a[i][j] = t[0][0]
    i = len(a) - 1
    j = len(a[0]) - 1
    rez = [(i - 1, j - 1)]
    while i != 1 or j != 1:
        if a[i][j - 1] < a[i - 1][j]:
            rez.append(tuple([i - 1, j - 2]))
            j = j - 1
        else:
            rez.append(tuple([i - 2, j - 1]))
            i = i - 1
    rez.reverse()
    return {'cost': a[-1][-1], 'path': rez}


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
