from typing import List


def search(list_values: List[int], selected_num: int) -> int:
    '''
    The function checks if selected number exists
     in the list of integers recursively.

    Uses approach by checking first element and recursively
    searching the rest of the list.

    Args:
        numbers (List[int]): List of integers to search in
        target (int): Number to search for

    Returns:
        int: 1 if target found, 0 if not found
    '''

    if not list_values:
        return 0

    if list_values[0] == selected_num:
        return 1

    return search(list_values[1:], selected_num)


def main() -> None:
    '''
    Main function for user input and number search.
    '''

    try:
        numbers = list(map(int, input('Введите список целых чисел через пробел: ').split()))
        selected_num = int(input("Введите искомое число: "))
        print(search(numbers, selected_num))

    except ValueError:
        print("Ошибка ввода данных: введите целые числа")


if __name__ == "__main__":
    main()
