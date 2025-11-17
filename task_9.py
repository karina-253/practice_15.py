def combin(total_items: int, chosen_items: int) -> int:
    '''
    The function calculates the number of combinations
     (binomial coefficient) recursively.

    Args:
        total_items (int): Total number of items
        chosen_items (int): Number of items to choose

    Returns:
        int: Number of ways to choose k items from n items
    '''

    if chosen_items == 0 or chosen_items == total_items:
        return 1

    if chosen_items > total_items or chosen_items < 0 or total_items < 0:
        return 0

    return combin(total_items - 1, chosen_items) + combin(total_items - 1, chosen_items - 1)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        total_items, chosen_items = map(int, input('Введите общее количество элементов и'
        ' количество выбираемых через пробел: ').split())

        if total_items < 0 or chosen_items < 0:
            print('Ошибка! Числа должны быть положительными.')
        else:
            print(combin(total_items, chosen_items))

    except ValueError:
        print('Ошибка: введите два числа через пробел')


if __name__ == "__main__":
    main()
