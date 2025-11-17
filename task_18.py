def simmetr(string: str, start_ind: int, end_ind: int) -> bool:
    '''
    The function checks if a substring from start to end index is symmetric recursively.

    Args:
        string (str): The input string to check
        start_ind(int): Starting index of the substring
        end_ind (int): Ending index of the substring

    Returns:
        bool: True if the substring is symmetric, False otherwise
    '''

    if start_ind >= end_ind:
        return True

    if string[start_ind] == string[end_ind]:
        return simmetr(string, start_ind + 1, end_ind - 1)

    return False


def main() -> None:
    """
    Main function for user input and symmetry checking.
    """
    try:
        string = input('Введите строку: ')
        start_ind = int(input('Введите начальный индекс: '))
        end_ind = int(input('Введите конечный индекс: '))

        if start_ind < 0 or end_ind >= len(string) or start_ind > end_ind:
            print('Ошибка: некорректные индексы')

        else:
            print(simmetr(string, start_ind, end_ind))

    except ValueError:
        print("Ошибка: индексы должны быть целыми числами")


if __name__ == "__main__":
    main()
