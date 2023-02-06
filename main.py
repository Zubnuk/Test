def get_win_sequence(input_string: str) -> str:
    """Selects a subsequence from the source sequence for the task 1.

        :param input_string: the first line contains the number N - the length of
        the source sequence. The second line contains a sequence of uppercase
        Latin letters.
        :return: a subsequence from the source sequence.
        """
    input_string = input_string.split()
    _string = input_string[1]
    count = int(input_string[0])
    _string = _string[:count]
    arr = []
    arr.append(_string[-1])
    for i in range(len(_string)-2,-1,-1):
        arr.append(_string[i] + arr[-1])
    arr.sort()
    return arr[0]


def get_water_volume(input_string: str) -> int:
    """Сalculates the number of blocks filled with water for the task 2.

    :param input_string: the first row contains N - the number of columns
    defining the landscape of the island. The second line contains N natural
    numbers — the height of the columns.
    :return: the number of blocks filled with water
    """
    input_string = input_string.split()
    count = int(input_string[0])
    arr = [int(x) for x in input_string[1:]]
    left_max = [arr[0]]
    right_max = [arr[-1]]
    for i in range(1, len(arr)):
        left_max.append(max(arr[i], left_max[-1]))
    for i in range(len(arr) - 1, 0, -1):
        right_max.append(max(arr[i], right_max[-1]))
    ans = 0
    right_max.reverse()
    for i in range(len(arr)):
        ans += max(min(right_max[i], left_max[i]) - arr[i], 0)
    return ans


def main():
    print(get_water_volume('11\n2 5 2 3 6 9 3 1 3 4 6'))  # 18

    print(get_win_sequence('4\nMAMA'))  # A
    print(get_win_sequence('4\nALLOALLO'))  # ALLO
    print(get_win_sequence('6\nABCOAXLO'))  # ABCOAX


if __name__ == '__main__':
    main()
