def  comp(str_1: str, str_2: str, length_1: int, length_2: int) -> int:
    '''
    The function calculate the length of the largest common subsequence.

    Args:
        str_1 (str): The first line
        str_2 (str): The second line
        length_1 (int): Length of the first string
        length_2 (int): Length of the second string

    Returns:
        int: The length of the largest common subsequence
    '''

    if length_1 == 0 or length_2 == 0:
        return 0

    if str_1[length_1 - 1] == str_2[length_2 - 1]:
        return 1 + comp(str_1, str_2,  length_1 - 1, length_2 - 1)

    return max(comp(str_1, str_2,  length_1 - 1, length_2),
               comp(str_1, str_2,  length_1, length_2 - 1))


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        str_1 = input('Введите первую строку: ').strip()
        str_2 = input('Введите вторую строку: ').strip()

        if not str_1 or not str_2:
            print('Ошибка: строки должны быть не пустыми!')
            return

        length_1 = len(str_1)
        length_2 = len(str_2)

        print(comp(str_1, str_2, length_1, length_2))

    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == "__main__":
    main()


