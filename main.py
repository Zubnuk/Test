def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    strings = []
    n, st = input_string.split("\n")
    n = int(n)
    strings.append(st[:n])
    for i in range(len(strings[0]) - 1):
        strings.append(strings[i][1:])
    return sorted(strings)[0]


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    n, st = input_string.split("\n")
    st = [int(a) for a in st.split()]
    print(st)
    n = int(n)
    maximum = -1
    maxes_first = []
    maxes_second = []

    for i in range(len(st)):
        if st[i] > maximum:
            maximum = st[i]
            maxes_first.append(maximum)
        else:
            maxes_first.append(maximum)
    maximum = -1
    for i in range(len(st) - 1, -1, -1):
        if st[i] > maximum:
            maximum = st[i]
            maxes_second.append(maximum)
        else:
            maxes_second.append(maximum)
    maxes_second = maxes_second[::-1]
    differences = []
    for i in range(len(maxes_first)):
        differences.append(min(maxes_first[i], maxes_second[i]) - st[i])
    return (sum(differences))


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
