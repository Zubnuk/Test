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
        raise Exception("The price table is not a rectangular matrix with float values")
    if len(price_table) == 0:
        raise Exception("The price table is not a rectangular matrix with float values")
    if isinstance(price_table[0][0], str):
        raise Exception("The price table is not a rectangular matrix with float values")

    dlin = len(price_table[0])
    d = 0
    for i in range(len(price_table)):
        d += 1
        for j in range(len(price_table[i])):
            if dlin != len(price_table[i]):
                raise Exception("The price table is not a rectangular matrix with float values")

    new_price_table = [[float('inf')] * (len(price_table[0]) + 1) for i in range(len(price_table) + 1)]
    mas_path = []

    for row in range(1, len(price_table) + 2):
        for column in range(1, len(price_table[0]) + 2):
            if row - 1 < len(price_table) and column - 1 < len(price_table[0]):
                new_price_table[row][column] = price_table[row - 1][column - 1]

    for row in range(1, len(price_table) + 1):
        for column in range(1, len(price_table[0]) + 1):
            print('row', row, ' column', column)
            if row == 1 and column == 1:
                continue

            # print('min ', new_price_table[row - 1][column], new_price_table[row][column - 1])
            # print('+ ', new_price_table[row][column])

            new_price_table[row][column] += \
                min(new_price_table[row - 1][column], new_price_table[row][column - 1])

    Min_path = new_price_table[-1][-1]

    for item in new_price_table:
        print(item)

    mas_path.append((len(price_table) - 1, len(price_table[0]) - 1))
    row, column = len(price_table), len(price_table[0])
    while row != 0 and column != 0:
        if new_price_table[row][column - 1] < new_price_table[row - 1][column]:
            column -= 1
        else:
            row -= 1
        mas_path.append((row - 1, column - 1))

    del mas_path[-1]
    mas_path.reverse()

    return {'cost': Min_path, 'path': mas_path}


def main():
    table = ['ab']
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
