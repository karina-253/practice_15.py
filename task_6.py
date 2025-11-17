def degree5(number: int) -> int:
    '''
    The function determines the exponent of 5 for
    a given natural number recursively.

    Args:
        number (int): Natural number to check

    Returns:
        int: Exponent k if number = 5^k, otherwise -1
    '''

    if number == 1:
        return 0

    if number % 5 != 0 or number < 1:
        return -1

    division = degree5(number // 5)

    if division == -1:
        return -1
    return division + 1


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        number_input = int(input('Введите натуральное число: '))

        if number_input < 1:
            print('Ошибка! Число должно быть натуральным')
        else:
            print(degree5(number_input))

    except ValueError:
        print("Ошибка ввода! Введите целое число.")


if __name__ == "__main__":
    main()
