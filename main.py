def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    params = input_string.split()
    count = int(params[0])
    letters = [params[1][:count]]

    for i in range(len(letters[0]) - 1):
        letters.append(letters[i][1:])

    return sorted(letters)[0]


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    params = input_string.split()
    count = int(params[0])
    params.pop(0)
    columns = [int(x) for x in params]

    left_col_max_idx = 0  # левый край
    right_col_max_idx = count - 1  # правый край

    lowlands = []  # низменности

    # одновременный проход массива с левого и правого концов
    for i in range(0, count):
        curr_left_col_idx = i
        curr_left_col = columns[curr_left_col_idx]

        curr_right_col_idx = count - i - 1
        curr_right_col = columns[curr_right_col_idx]

        if curr_left_col >= columns[left_col_max_idx]:
            if curr_left_col_idx - left_col_max_idx > 1:  # края низменностей
                lowlands.append((left_col_max_idx, curr_left_col_idx))
            left_col_max_idx = curr_left_col_idx

        if curr_right_col >= columns[right_col_max_idx]:
            if right_col_max_idx - curr_right_col_idx > 1:  # края низменностей
                lowlands.append((curr_right_col_idx, right_col_max_idx))
            right_col_max_idx = curr_right_col_idx

    lowlands = list(set(lowlands))  # убираем дубли
    water_volume = 0
    for left, right in lowlands:
        waterline = min(columns[left], columns[right])
        for i in range(left + 1, right):
            water_volume += waterline - columns[i]

    return water_volume


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
