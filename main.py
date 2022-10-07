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
    exception_message = 'parameter is not an integer rectangle matrix'
    if not (type(profit_matrix) is list):
        raise ArgumentException(exception_message)
    if len(profit_matrix) == 0:
        raise ArgumentException(exception_message)
    Len = len(profit_matrix[0])
    for i in profit_matrix:
        if not (type(i) is list):
            raise ArgumentException(exception_message)
        if len(i) != Len:
            raise ArgumentException(exception_message)
        for j in i:
            if not (type(j) is int):
                raise ArgumentException(exception_message)
    if len(profit_matrix[0]) == 1:
        return {'profit': profit_matrix[0][0], 'parts': [1]}

    global mas_buf
    mas_buf = {}
    path = []
    profit = 0

    new_profit_matrix = [[0] * (len(profit_matrix[0])) for i in range(len(profit_matrix) + 1)]
    for row in range(1, len(profit_matrix) + 1):
        for column in range(len(profit_matrix[0])):
            new_profit_matrix[row][column] = profit_matrix[row - 1][column]

    def repositioning(kol):
        d = []
        for i in range(kol + 1):
            d.append((i, kol - i))
        return d

    def price(kol, index, mas=None):
        global prov

        def get_key(dict, value):
            for k, v in dict.items():
                if v == value:
                    return k

        mas_path = {}
        d = repositioning(kol)
        for j in d:
            mas_path[j] = 0
            prov = False
            for item in j:
                if item == 0:
                    continue
                if prov:
                    continue

                if kol % 2 == 0 and kol / 2 == item:
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

    key = 0
    for i in range(0, len(new_profit_matrix[0]) - 1):
        mas_buf[i] = []
        for j in range(1, len(new_profit_matrix)):
            if i > 0:
                key = i - 1
            mas_buf[i].append(price(j, i, mas_buf[key]))

    for key, value in mas_buf[len(new_profit_matrix[0]) - 2][-1].items():
        profit = value

    def get_key(mas):
        for key, value in mas.items():
            return key

    next = 0
    for i in range(len(new_profit_matrix[0]) - 2, -1, -1):
        path.append(get_key(mas_buf[i][next - 1])[-1])
        if i == 0:
            path.append(get_key(mas_buf[i][next - 1])[0])
            break
        next = get_key(mas_buf[i][next - 1])[0]
        if next == 0:
            if i == -1:
                path.append(get_key(mas_buf[i][next - 1])[0])
                break
            for _ in range(i + 1):
                path.append(0)
            break

    path.reverse()
    return {'profit': profit, 'parts': path}


def main():
    profit_matrix = [[5, 4, 4, 7],
                     [6, 7, 8, 12],
                     [1, 10, 15, 12],
                     [2, 12, 23, 15],
                     [6, 15, 42, 18]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
