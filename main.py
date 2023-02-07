def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    Str = input_string.split("\n")
    data = [Str[1][:int(Str[0])]]
    for i in range(len(data[0]) - 1):
        data.append(data[i][1:])
    return sorted(data)[0]


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    Str = input_string.split("\n")
    data = list(map(int, Str[1].split(' ')))
    L, R = 0, len(data) - 1
    Max_L, Max_R = data[L], data[R]
    result = 0
    while L < R:
        if Max_L >= Max_R:
            result += Max_R - data[R]
            R -= 1
            Max_R = max(Max_R, data[R])
        else:
            result += Max_L - data[L]
            L += 1
            Max_L = max(Max_L, data[L])
    return result


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    # print(get_win_sequence('4\nMAMA'))  # A
    # print(get_win_sequence('8\nALLOALLO'))  # ALLO
    # print(get_win_sequence('21\nASZYAFAXZEWWAVQHJHBPELYZP'))  # AFAXZEWWAVQHJHBPE


if __name__ == '__main__':
    main()
