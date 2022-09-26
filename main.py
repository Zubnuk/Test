class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def __matrix_check(matrix: [[int]]) -> bool:  # matrix order check
    if matrix is None:
        return False
    if len(matrix) < 1:
        return False
    for i in range(len(matrix)):
        for element in matrix[i]:
            if type(element) is not float:
                return False
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            return False
    return True


def get_min_cost_path(price_table: list[list[float]]) -> \
        dict[str: float, str: list[tuple[int, int]]]:
    """Searches for the minimum cost path in the table. Each cell in the table
    has some price per visit.
    :param price_table: a matrix with float cell price values.
    :raise ArgumentException: when price_table is not a rectangle float matrix.
    :return: a dictionary with keys: cost - the minimum value of the cost of the
    path, path - an ordered list of tuples with cell indices.
    """
    if not __matrix_check(price_table):
        raise Exception('The price table is not a rectangular matrix '
                        'with float values')
    dictionary = {'cost': 0., 'path': [()]}
    buff = [[]]
    for i in range(len(price_table) + 1):
        buff.append(list())
        for j in range(len(price_table[0]) + 1):
            buff[i].append(1000.)
    buff.pop()
    buff[1][1] = price_table[0][0]
    for i in range(1, len(buff)):
        for j in range(1, len(buff[0])):
            if i == 1 and j == 1:
                continue
            buff[i][j] = price_table[i - 1][j - 1] + min(buff[i][j - 1], buff[i - 1][j])
    x, y = len(buff) - 1, len(buff[0]) - 1
    cords = list()
    while x != 0 and y != 0:
        cords.append([x - 1, y - 1])
        if buff[x - 1][y] < buff[x][y - 1]:
            x = x - 1
        else:
            y = y - 1
    cords.reverse()
    dictionary['cost'] = buff[-1][-1]
    last_cords = list()
    for i in range(len(cords)):
        kort = (cords[i][0], cords[i][1])
        last_cords.append(kort)
    dictionary['path'] = last_cords
    print(dictionary)
    return dictionary


def main():
    table = [[1., 2., 2.],
             [3., 4., 2.],
             [1., 1., 2.]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()