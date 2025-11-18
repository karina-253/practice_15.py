def sum_progress(first_member: float, difference: float,
             members_count: int) -> float:
    '''
    The function calculates the sum of the first n terms of an
     arithmetic progression recursively.
    Formula: a_n = a_1 + (n - 1) + d
    S_n = a_n + S_n-1

    Args:
        first_member (float): The first member of the progression
        difference (float):  Progression difference
        n_member (int): The number of terms to sum

     Returns:
        float: The sum of the first n terms of the arithmetic progression
    '''

    if members_count == 1:
        return first_member

    nth_member = first_member + (members_count - 1) * difference
    return nth_member + sum_progress(first_member, difference, members_count - 1)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        first_member, difference, members_count = map(float, input('Введите первый член,'
        ' разность и количество членов прогрессии через пробел:').split())

        members_count = int(members_count)

        if members_count < 1:
            print('Ошибка! Количество членов прогрессии должен быть натуральным числом.')
        else:
            print(sum_progress(first_member, difference, members_count))

    except ValueError:
        print('Ошибка! Введите три числа через пробел.')


if __name__ == "__main__":
    main()
