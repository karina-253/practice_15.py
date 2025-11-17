def fib(member_index: int) -> int:
    '''
    The function calculates the k-th term of the Fibonacci sequence recursively.

    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...

    Args:
        member_index(int): Index of the term to calculate

    Returns:
        int: The k-th member of Fibonacci sequence
    '''

    if member_index <= 0:
        return 0

    elif member_index == 1:
        return 1

    return fib(member_index - 1) + fib(member_index - 2)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        number_input = int(input('Введите номер члена последовательности Фибоначчи:'))

        if number_input < 0:
            print('Ошибка! Номер члена должен быть положительным')
        else:
            print(fib(number_input))

    except ValueError:
        print("Ошибка ввода! Введите целое число.")


if __name__ == "__main__":
    main()
