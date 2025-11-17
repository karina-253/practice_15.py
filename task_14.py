def numbers(number: int) -> None:
    '''
    The function prints digits of a natural number in reverse order recursively.

    Prints one digit per line by extracting the last digit (remainder)
    and recursively processing the remaining number.

    Args:
        number (int): Natural number to process

    Returns:
        None: Function prints digits.
    '''

    if number < 10:
        print(number)
    else:
        print(number % 10)
        numbers(number // 10)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        number = int(input('Введите натуральное число: '))

        if number <= 0:
            print('Ошибка: число должно быть натуральным')
        else:
            print(numbers(number))

    except ValueError:
        print('Ошибка: введите корректное натуральное число')
        

if __name__ == "__main__":
    main()
