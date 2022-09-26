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
    mas = price_table
    mas_2 = [[1000] * (len(mas) + 2) for i in range(len(mas) + 2)]

    for i in range(1, len(mas) + 2):
        for j in range(1, len(mas) + 2):
            if i - 1 < len(mas) and j - 1 < len(mas):
                mas_2[i][j] = mas[i - 1][j - 1]

    for i in range(1, len(mas_2)):
        for j in range(1, len(mas_2)):
            start = mas_2[i][j]
            if i + 1 < len(mas_2) and j + 1 < len(mas_2):
                if mas_2[i + 1][j] < mas_2[i][j + 1]:
                    mas_2[i + 1][j] += start
                elif mas_2[i + 1][j] == mas_2[i][j + 1]:
                    mas_2[i + 1][j] += start
                else:
                    mas_2[i][j + 1] += start


    for item in mas_2:
        print(item)


def main():
    table = [[1, 2, 2],
             [3, 4, 2],
             [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == '__main__':
    main()
