import copy


class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def calculate_sum_table(price_table: list[list[float]]) -> list[list[float]]:
    sum_table = create_sum_table(price_table)
    horizontal_length = len(sum_table[0])
    vertical_length = len(sum_table)
    for y in range(1, horizontal_length):
        for x in range(1, vertical_length):
            sum_table[x][y] = sum_table[x][y] + \
                              min(sum_table[x - 1][y], sum_table[x][y - 1])
    return sum_table


def calculate_moves_table(sum_table: list[list[float]]) -> \
        list[tuple[int, int]]:
    moves_table = list()
    horizontal = len(sum_table[0]) - 1
    vertical = len(sum_table) - 1
    while not (horizontal == vertical == 1):
        moves_table.append((vertical - 1, horizontal - 1))
        if sum_table[vertical - 1][horizontal] < \
                sum_table[vertical][horizontal - 1]:
            vertical -= 1
        else:
            horizontal -= 1
    moves_table.reverse()
    moves_table.insert(0, (0, 0))
    return moves_table


def is_rectangle(price_table: list[list[float]]) -> bool:
    vertical_length = len(price_table)
    if vertical_length == 0:
        return False
    horizontal_length = len(price_table[0])
    for horizontal_elements in price_table:
        if len(horizontal_elements) != horizontal_length:
            return False
    return True


def is_float(price_table: list[list[float]]) -> bool:
    for horizontal_elements in price_table:
        for element in horizontal_elements:
            if type(element) != float:
                return False
    return True


def is_right(price_table: list[list[float]]):
    if not price_table:
        raise ArgumentException("The price table is not a rectangular matrix "
                                "with float values")
    if not is_rectangle(price_table):
        raise ArgumentException("The price table is not a rectangular matrix "
                                "with float values")
    if not is_float(price_table):
        raise ArgumentException("The price table is not a rectangular matrix "
                                "with float values")


def create_sum_table(price_table: list[list[float]]) -> list[list[float]]:
    sum_table = copy.deepcopy(price_table)
    for elements in sum_table:
        elements.insert(0, float("inf"))
    sum_table.insert(0, [float("inf")] * len(sum_table[0]))
    sum_table[0][1] = 0
    sum_table[1][0] = 0
    return sum_table


def get_min_cost_path(price_table: list[list[float]]) -> \
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost
    of the path, path - an ordered list of tuples with cell indices.
    """
    is_right(price_table)
    sum_table = calculate_sum_table(price_table)
    moves_table = calculate_moves_table(sum_table)
    return {
        "cost": sum_table[-1][-1],
        "path": moves_table
    }


def main():
    table = [[1., 2., 2., 1., 3., 4.],
             [3., 1., 1., 5., 7., 6.],
             [3., 4., 1., 2., 7., 6.],
             [5., 7., 1., 6., 4., 4.],
             [5., 9., 2., 3., 5., 8.],
             [2., 2., 1., 3., 1., 6.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
