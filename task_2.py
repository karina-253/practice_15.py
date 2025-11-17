def count(number: int) -> int:
    '''
    The function calculates the number
    of digits in a natural number recursively.

    Args:
        number (int): Natural number

    Returns:
        int: the number of digits in a natural number
    '''

    if number < 10:
        return 1

    return 1 + count(number // 10)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        number_input = int(input('Введите натуральное число:'))

        if number_input < 1:
            print('Ошибка! Число должно быть натуральным')
        else:
            print(f'Количество цифр в числе: {count(number_input)}')

    except ValueError:
        print('Ошибка ввода! Введите целое число.')


if __name__ == "__main__":
    main()
