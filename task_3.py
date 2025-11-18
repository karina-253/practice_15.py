def progress(first_member: float, difference: float,
             n_member: int) -> float:
    '''
    The function calculates the nth term of an arithmetic
    progression recursively.
    Formula = a_n = a_n-1 + d

    Args:
        first_member (float): The first member of the progression
        difference (float):  Progression difference
        n_member (int): The number of the progression term to calculate

    Returns:
        float: the nth term of the arithmetic progression
    '''

    if n_member == 1:
        return first_member

    return difference + progress(first_member, difference, n_member - 1)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        first_member, difference, n_member = map(float, input
        ('Введите первый член, разность и номер члена прогрессии через пробел:').split())

        n_member = int(n_member)

        if n_member < 1:
            print('Ошибка! Номер члена прогрессии должен быть натуральным числом.')
        else:
            print(progress(first_member, difference, n_member))

    except ValueError:
        print('Ошибка! Введите три числа через пробел.')


if __name__ == "__main__":
    main()
