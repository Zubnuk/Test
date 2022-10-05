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
    global masAB, masABC, masABCD
    masAB = []
    masABC = []
    masABCD = []

    new_profit_matrix = [[0] * (len(profit_matrix[0])) for i in range(len(profit_matrix) + 1)]

    for row in range(1, len(profit_matrix) + 1):
        for column in range(len(profit_matrix[0])):
            new_profit_matrix[row][column] = profit_matrix[row - 1][column]

    for i in new_profit_matrix:
        print(i)

    def res(kol):
        d = []
        for i in range(kol + 1):
            d.append((i, kol - i))
        return d

    def price(i, index, mas=None):
        global prov

        def get_key(dict, value):
            for k, v in dict.items():
                if v == value:
                    return k

        mas_path = {}
        d = res(i)
        for j in d:
            mas_path[j] = 0
            prov = False
            for item in j:
                if item == 0:
                    continue
                if prov:
                    continue

                if i % 2 == 0 and i / 2 == item:
                    mas_path[j] = new_profit_matrix[item][j.index(item) + index] \
                                  + new_profit_matrix[item][j.index(item) + 1 + index]
                    continue

                if index > 0 and j[0] > 0:
                    prov = True
                    for key, value in mas[item - 1].items():
                        mas_path[j] = value + new_profit_matrix[j[1]][j.index(j[1]) + index]
                    continue

                mas_path[j] += new_profit_matrix[item][j.index(item) + index]

        Max = max(mas_path.values())
        return {get_key(mas_path, Max): max(mas_path.values())}

    for i in range(1, len(new_profit_matrix)):
        masAB.append(price(i, 0))

    for i in range(1, len(new_profit_matrix)):
        masABC.append(price(i, 1, masAB))

    for i in range(1, len(new_profit_matrix)):
        masABCD.append(price(i, 2, masABC))

    print(masAB)
    print(masABC)
    print(masABCD)


def main():
    profit_matrix = [[15, 18, 16, 17],
                  [20, 22, 23, 19],
                  [26, 28, 27, 25],
                  [34, 33, 29, 31],
                  [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
