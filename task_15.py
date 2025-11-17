def ten_to_bin(number: int) -> str:
    '''
    The function converts a natural number from decimal to binary system recursively.

    Uses recursive division by 2 to build the binary representation
    from the most significant bit to the least significant bit.

    Args:
        number (int): Natural number to convert to binary

    Returns:
        str: Binary representation of the number as a string
    '''

    if number < 2:
        return str(number)

    return ten_to_bin(number // 2) + str(number % 2)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        number = int(input('Введите натуральное число: '))

        if number < 0:
            print('Ошибка: число должно быть положительным')
        else:
            print(ten_to_bin(number))

    except ValueError:
        print('Ошибка ввода данных: введите целое число')


if __name__ == "__main__":
    main()
  
