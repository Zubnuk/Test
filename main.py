def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    pass


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    pass


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
