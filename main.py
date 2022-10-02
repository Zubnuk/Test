import copy 

class ArgumentException(Exception):
    """Exception raised for errors in the input parameter.
    Attributes:
        message -- explanation of the error
    """

    def init(self, message):
        self.message = message
        super().init(self.message)

def matrix_checker(table)->bool:
    if not (type(table) is list):
        return False
    if len(table) == 0:
        return False
    length = len(table[0])
    if length == 0:
        return False
    for i in table:
        if length != len(i) or not (all(isinstance(x, (int, float)) for x in i)):
            return False
    return True

def get_min_cost_path(table: list[list[float]]) -> \
    dict[str: float, str: list[tuple[int, int]]]:
        if not matrix_checker(table):
            raise Exception('The price table is not a rectangular matrix with float values')
        copied_matrix = copy.deepcopy(table)
        for i in range(1, len(table)):
            copied_matrix[i][0] += copied_matrix[i - 1][0]
        for i in range(1, len(copied_matrix[0])):
            copied_matrix[0][i] += copied_matrix[0][i - 1]
        for i in range(1, len(table)):
            for j in range(1, len(table[0])):
                copied_matrix[i][j] += min(copied_matrix[i - 1][j], copied_matrix[i][j - 1])
        i, j = len(table) - 1, len(table[0]) - 1
        path = []
        while i + j != 0:
            path.append((i , j ))
            if copied_matrix[i - 1][j] < copied_matrix[i][j - 1]:
                i = i - 1
            else:
                j = j - 1
        path.append((0, 0))
        path.reverse()
        return {'cost': copied_matrix[len(copied_matrix) - 1][len(copied_matrix[0]) - 1], 'path': path}


def main():
        table = [[3., 5., 2.],
                [3., 4., 6.],
                [5., 3., 7.]]
        print(get_min_cost_path(table))



if __name__ == '__main__':
        main()