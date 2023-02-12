import string

def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    alph = string.ascii_uppercase
    count = int(input_string.split()[0])
    letters = input_string.split()[1][:count]
    temp = []
    for i in alph:
        if letters.count(i) == 1:
            return letters[letters.index(i):]
        elif letters.count(i) > 1:
            indent = 0
            for j in range(letters.count(i)):
                temp.append(letters[letters.index(i, indent):])
                indent = letters.index(i, indent)+1
            return min(temp)





def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    count = int(input_string.split()[0])
    letters = input_string.split()[1:]
    temp_max = 0
    left_border, right_border=[],[]
    for i in range(1, count-1):
        temp_max = max(temp_max, int(letters[i - 1]))
        left_border.append(temp_max)
    temp_max = 0
    for j in range(count - 2, 0, -1):
        temp_max = max(temp_max, int(letters[j + 1]))
        right_border.append(temp_max)
    right_border.reverse()
    water = 0
    for x in range(count-2):
        if min(left_border[x], right_border[x])-int(letters[x+1]) > 0:
            water += min(left_border[x], right_border[x])-int(letters[x+1])
    return water



def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18
    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
