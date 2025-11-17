def get_digit_char(digit: int) -> str:
    '''
    The function converts a digit to its character representation in numeral systems.

    For digits 0-9 returns the digit itself, for 10-15 returns letters A-F.

    Args:
        digit (int): Digit value from 0 to 15

    Returns:
        str: Character representation of the digit
    '''

    if digit <= 9:
        return str(digit)

    letters = "ABCDEF"
    return letters[digit - 10]


def ten_to_n(number: int, system_base: int) -> str:
    '''
    The function converts a natural number from decimal
     to base-n numeral system recursively.

    Uses recursive division by base to build the base-n representation
    from the most significant digit to the least significant digit.

    Args:
        number (int): Natural number to convert
        system_base (int): Base of the numeral system (2-16)

    Returns:
        str: Number representation in the specified base as string
    '''

    if number < system_base:
        return get_digit_char(number)

    return ten_to_n(number // system_base, system_base) + get_digit_char(number % system_base)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        number = int(input('Введите натуральное число: '))
        system_base = int(input('Введите основание системы счисления(2-16): '))

        if number < 0:
            print("Ошибка: число должно быть положительным")
        elif system_base < 2 or system_base > 16:
            print("Ошибка: основание системы должно быть от 2 до 16")
        else:
            print(ten_to_n(number, system_base))

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены целые числа.")


if __name__ == "__main__":
    main()
