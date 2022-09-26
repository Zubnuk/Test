import pprint


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
    new_list = []
    if price_table is None:
        raise Exception("The price table is not a rectangular matrix with float values")
    if len(price_table) != 0:
        length = len(price_table[0])
        for line in price_table:
            if len(line) != length:
                raise Exception("The price table is not a rectangular matrix with float values")
    else:
        raise Exception("The price table is not a rectangular matrix with float values")
    for i in range(len(price_table)):
        for j in range(len(price_table[0])):
            if type(price_table[i][j]) is not float:
                raise Exception("The price table is not a rectangular matrix with float values")

    for i in range(len(price_table) + 1):
        new_list.append([])
        for j in range(len(price_table[0]) + 1):
            new_list[i].append(float("inf"))
    for i in range(1, len(new_list)):
        for j in range(1, len(new_list[0])):
            if i == 1 and j == 1:
                new_list[1][1] = price_table[0][0]
            else:
                new_list[i][j] = price_table[i - 1][j - 1] + min(new_list[i][j - 1], new_list[i - 1][j])
    path = []
    current = (len(new_list) - 1, len(new_list[0]) - 1)
    path.append(current)
    while current != (1, 1):
        i = current[0]
        j = current[1]
        if new_list[i][j - 1] > new_list[i - 1][j]:
            path.append((i - 1, j))
            current = path[-1]
        else:
            path.append((i, j - 1))
            current = path[-1]
    path_indexes = []
    for element in path:
        element = (element[0] - 1, element[1] - 1)
        path_indexes.append(element)
    path_indexes = path_indexes[::-1]
    dictionary = {
        "cost": new_list[-1][-1],
        "path": path_indexes
    }
    return dictionary

    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    pass


def main():
    table = [[1., 2., 2.],
             [3., 4., 1.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
