def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    count = int(input_string.split()[0])
    word = input_string.split()[1][:count]
    best_word = word
    for i in range(1, count):
        new_word = word[i:]
        # Слова сравниваются по номеру букв поэтомы чем раньше буква тем меньше ее число
        if new_word < best_word:
            best_word = new_word
    return best_word


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    arr_water = input_string.split()
    arr_border = [[], []]
    for i in range(1, int(arr_water[0]) + 1):
        arr_border[0].append(max(0 if i == 1 else arr_border[0][-1], int(arr_water[i])))
        arr_border[1].append(max(0 if i == 1 else arr_border[1][-1], int(arr_water[len(arr_water) - i])))
    arr_border[1].reverse()
    sum = 0
    for i in range(int(arr_water[0])):
        sum += min(arr_border[0][i], arr_border[1][i]) - int(arr_water[i + 1])
    return sum


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
