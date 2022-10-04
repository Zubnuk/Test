from custom_exception import ArgumentException


def invest_distribution(profit_matrix: list[list[int]]) -> \
        dict[str: int, str: list[int]]:
    checker(profit_matrix)
    col1 = [0] + [int(x[0]) for x in profit_matrix]
    Old_way = [[i] for i in range(len(profit_matrix) + 1)]
    count_col2 = 0
    for i in range(len(profit_matrix[0]) - 1):
        New_way = [[0] * 2 for i in range(len(profit_matrix) + 1)]
        col2 = [0] + [int(x[i + 1]) for x in profit_matrix]
        max_col = []
        for j in range(0, len(col2)):
            count_col2 = 0
            max_invest = 0
            for f in range(0, j + 1):
                var1 = col1[f]
                var2 = col2[j - f]
                if var1 + var2 > max_invest:
                    count_col2 = j - f
                    max_invest = var2 + var1
            New_way[j] = Old_way[j - count_col2] + [count_col2]
            max_col.append(max_invest)
        col1 = max_col
        Old_way = New_way.copy()
    return {'profit': col1[-1], 'parts': Old_way[-1]}


def checker(profit_matrix: list[list[int]]):
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


def main():
    profit_matrix = [[15, 18, 16, 17],
                  [20, 22, 23, 19],
                  [26, 28, 27, 25],
                  [34, 33, 29, 31],
                  [40, 39, 41, 37]]
    print(invest_distribution(profit_matrix))


if __name__ == '__main__':
    main()
