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
    if not (type(profit_matrix) is list):
        raise ArgumentException('parameter is not an integer rectangle matrix')
    if len(profit_matrix) == 0:
        raise ArgumentException('parameter is not an integer rectangle matrix')
    length = len(profit_matrix[0])
    for i in profit_matrix:
        if not (type(i) is list):
            raise ArgumentException('parameter is not an integer rectangle matrix')
        if len(i) != length:
            raise ArgumentException('parameter is not an integer rectangle matrix')
        for j in i:
            if not (type(j) is int):
                raise ArgumentException('parameter is not an integer rectangle matrix')

    global masAB, masABC, masABCD
    masAB = []
    masABC = []
    masABCD = []

    new_profit_matrix = [[0] * (len(profit_matrix[0])) for i in range(len(profit_matrix) + 1)]

    for row in range(1, len(profit_matrix) + 1):
        for column in range(len(profit_matrix[0])):
            new_profit_matrix[row][column] = profit_matrix[row - 1][column]

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
                    if index > 0 and j[0] > 0:
                        prov = True
                        for key, value in mas[item - 1].items():
                            mas_path[j] = value + new_profit_matrix[j[1]][j.index(j[1]) + index + 1]
                        continue

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

    if len(profit_matrix[0]) == 1:
        return {'profit': profit_matrix[0][0], 'parts': [1]}

    if len(profit_matrix[0]) == 2:
        path = []
        profit = 0
        for i in range(1, len(new_profit_matrix)):
            masAB.append(price(i, 0))

        for key, value in masAB[-1].items():
            profit = value
            path.append(key[-1])
            path.append(0)
        path.reverse()

        return {'profit': profit, 'parts': path}

    for i in range(1, len(new_profit_matrix)):
        masAB.append(price(i, 0))

    for i in range(1, len(new_profit_matrix)):
        masABC.append(price(i, 1, masAB))

    for i in range(1, len(new_profit_matrix)):
        masABCD.append(price(i, 2, masABC))

    path = []
    profit = 0
    for key, value in masABCD[-1].items():
        profit = value
        path.append(key[-1])
        if key[0] == 0:
            for i in range(1, len(profit_matrix[0])):
                path.append(0)
            continue
        for k, v in masABC[key[0] - 1].items():
            path.append(k[-1])
            for a, b in masAB[k[0] - 1].items():
                path.append(a[-1])
                path.append(a[0])
    path.reverse()

    return {'profit': profit, 'parts': path}


def main():
    profit_matrix = [[1, 2],
                     [3, 5]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
