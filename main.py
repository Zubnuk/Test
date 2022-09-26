class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def get_min_cost_path(price_table: list[list[float]]) ->\
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    checker(price_table)
    sum_table = [[float('inf') for column in range(len(price_table[0]) + 1)] for row in range(len(price_table) + 1)]
    sum_table[1][1] = price_table[0][0]

    for row in range(1, len(price_table) + 1):
        for column in range(1, len(price_table[0]) + 1):
            if row == 1 and column == 1:
                continue
            sum_table[row][column] = min(sum_table[row-1][column], sum_table[row][column-1]) + price_table[row-1][column-1]

    path_array = []

    row, column = len(sum_table)-1, len(sum_table[0]) - 1

    path_array.append((len(price_table) - 1, len(price_table[0]) - 1))
    while row * column != 1:
        if sum_table[row-1][column] < sum_table[row][column-1]:
            row -= 1
        else:
            column -= 1
        path_array.append((row-1, column-1))

    return {'cost': sum_table[-1][-1], 'path': list(reversed(path_array))}


def checker(price_table: list[list[float]]) -> Exception:
    if price_table is None:
        raise Exception('The price table is not a rectangular matrix with float values')
    if len(price_table) == 0:
        raise Exception('The price table is not a rectangular matrix with float values')

    first_row_length = len(price_table[0])
    for row in price_table:
        if len(row) != first_row_length:
            raise Exception('The price table is not a rectangular matrix with float values')
        for column_value in row:
            if type(column_value) == str:
                raise Exception('The price table is not a rectangular matrix with float values')


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
