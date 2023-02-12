def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

    :param input_string: the first line contains the number N - the length of
    the source sequence. The second line contains a sequence of uppercase
    Latin letters.
    :return: a subsequence from the source sequence.
    """
    n = int(input_string.split('\n')[0])
    str = input_string.split('\n')[1][:n]
    res = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for l in range(len(alphabet)):
        if len(str) > 0 and str.__contains__(alphabet[l]):
            a_indexes = []
            for i in range(len(str)):
                if str[i] == alphabet[l]:
                    a_indexes.append(i)
            if a_indexes[-1] == len(str) - 1:
                return alphabet[l]
            strings_start_letter = []
            for index in a_indexes:
                strings_start_letter.append(str[index:])
            res = min(strings_start_letter)
            if len(res) == len(str):
                return res
            else:
                return res


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    n, blocks_str = input_string.split("\n")
    blocks = list(map(int, blocks_str.split()))
    right = []
    left = []
    cur_max = blocks[0]
    for block_h in blocks:
        if block_h > cur_max:
            cur_max = block_h
        right.append(cur_max)
    cur_max = blocks[-1]
    for block_h in reversed(blocks):
        if block_h > cur_max:
            cur_max = block_h
        left.append(cur_max)
    left.reverse()
    ans = 0
    for i in range(len(blocks)):
        ans += min(right[i], left[i]) - blocks[i]
    return ans


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('8\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
