def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    length, sequence = input_string.split("\n")
    data = [sequence[:int(length)]]
    for i in range(len(data[0]) - 1):
        data.append(data[i][1:])
    return min(data)


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    data = input_string.strip().split("\n")
    n = int(data[0])
    column_heights = list(map(int, data[1].split()))

    trapped_water = 0
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = column_heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], column_heights[i])

    right_max[n - 1] = column_heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], column_heights[i])

    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - column_heights[i]

    return trapped_water


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
