import sys


class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


COST = 'cost'
PATH = 'path'


def get_min_cost_path(price_table: list[list[float]]) -> dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    exception_message = 'The price table is not a rectangular matrix with float values'
    if (price_table is None) or (len(price_table) == 0):
        raise ArgumentException(exception_message)

    row_length = len(price_table[0])
    for i in price_table:
        if (i is None) or (len(i) != row_length):
            raise ArgumentException(exception_message)
        for j in i:
            if type(j) is not float:
                raise ArgumentException(exception_message)

    cpt = __get_completed_price_table__(price_table)  # hereinafter called `cpt`, means completed_price_table

    path = []
    cpt_row_index = len(cpt) - 1
    cpt_col_index = len(cpt[0]) - 1
    cost = cpt[cpt_row_index][cpt_col_index]

    while cpt_row_index > 0 and cpt_col_index > 0:
        curr_row_idx = cpt_row_index - 1
        curr_col_idx = cpt_col_index - 1

        path_idx = (curr_row_idx, curr_col_idx)
        path.insert(0, path_idx)
        check_higher_value = cpt[curr_row_idx][cpt_col_index] >= cpt[cpt_row_index][curr_col_idx]

        if check_higher_value:
            cpt_col_index -= 1
        else:
            cpt_row_index -= 1

    return {COST: cost, PATH: path}


def __get_completed_price_table__(price_table: list[list[float]]) -> list[list[float]]:
    for i, row in enumerate(price_table):
        for j in range(len(row)):
            if (i - 1) < 0 and (j - 1) < 0:
                continue
            if (i - 1) < 0 and (j - 1) > -1:
                price_table[i][j] += price_table[i][j - 1]
            if (i - 1) > -1 and (j - 1) < 0:
                price_table[i][j] += price_table[i - 1][j]
            if (i - 1) >= 0 and (j - 1) >= 0:
                check_higher_value = price_table[i - 1][j] >= price_table[i][j - 1]
                if check_higher_value:
                    price_table[i][j] += price_table[i][j - 1]
                else:
                    price_table[i][j] += price_table[i - 1][j]

    max_value_list = []
    for i in range(len(price_table[0]) + 1):
        max_value_list.append(sys.float_info.max)
    price_table.insert(0, max_value_list)

    for i, row in enumerate(price_table):
        if i == 0:
            continue
        row.insert(0, sys.float_info.max)

    return price_table


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
