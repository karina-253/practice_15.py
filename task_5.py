def mod_number(dividend: int, divisor: int) -> int:
    '''
    The function calculates the remainder of dividing natural number
     by natural number recursively.

    Args:
        dividend (int): Dividend (natural number)
        divisor (int): Divisor (natural number)

    Returns:
        int: Remainder of dividend divided by divisor
    '''

    if dividend < divisor:
        return dividend

    return mod_number(dividend - divisor, divisor)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        dividend, divisor = map(int, input('Введите два натуральных'
        'числа через пробел: ').split())

        if dividend < 0 or divisor <= 0:
            print('Ошибка! Числа должны быть натуральными.')
        else:
            print(mod_number(dividend, divisor))

    except ValueError:
        print('Ошибка: введите два числа через пробел')


if __name__ == "__main__":
    main()
