def nod(num_1: int, num_2: int) -> int:
    '''
    The function calculates the greatest common divisor
     of two natural numbers recursively.

    Args:
        num_1 (int): First natural number
        num_2 (int): Second natural number

    Returns:
        int: Greatest common divisor of num_1 and num_2.
    '''

    if num_2 == 0:
        return num_1

    return nod(num_2, num_1 % num_2)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        num_1, num_2 = map(int, input('Введите два натуральных числа через пробел:').split())

        if num_1 < 0 or num_2 < 0:
            print('Ошибка: числа должны быть натуральными')
        else:
            print(nod(num_1, num_2))

    except ValueError:
        print('Ошибка: введите два числа через пробел')


if __name__ == "__main__":
    main()
