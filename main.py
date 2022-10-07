from custom_exception import ArgumentException


def tridiagonal_determinant(matrix: list[list[int]]) -> int:
    pass


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print(tridiagonal_determinant(matrix))


if __name__ == '__main__':
    main()
