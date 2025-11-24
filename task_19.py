def count_squares(length: int, width: int) -> int:
    '''
    The function calculates the number of squares that can be cut off from
    a rectangle recursively, if the largest square is cut off each time.

    Args:
        length (int): Rectangle length (natural number)
        width (int): Rectangle width (natural number)

    Returns:
        int: The total number of squares that can be cut of
    '''

    if length == 0 or width == 0:
        return 0

    if length < width:
        return count_squares(width, length)

    squares = length // width
    remain = length % width

    return squares + count_squares(width, remain)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        length, width = map(int, input('Введите стороны прямоугольника'
        ' через пробел:').split())

        if length < 0 or width < 0:
            print("Ошибка: число должно быть положительным")
        else:
            print(count_squares(length, width))

    except ValueError:
        print("Ошибка ввода! Убедитесь, что введены натуральные числа.")


if __name__ == "__main__":
    main()
