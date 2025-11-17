def pownum(base: float, degree: int) -> float:
    '''
    The function calculates the power of a number recursively.

    Args:
        base (float): The basis of the degree
        degree (int): Exponent (natural number)

    Returns:
        float: The result of raising base to exponent
    '''

    if degree == 0:
        return 1

    if degree == 1:
        return base

    return base * pownum(base, degree-1)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        num, deg = map(float, input('Введите основание и показатель'
                                    ' степени через пробел: ').split())

        deg = int(deg)

        if deg < 0:
            print('Ошибка! Степень должна быть натуральным числом.')
        else:
            print(pownum(num, deg))

    except ValueError:
        print('Ошибка! Введите два числа через пробел')


if __name__ == "__main__":
    main()
