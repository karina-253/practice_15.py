from typing import List


def odd_list(numbers: List[int], count_elements: int) -> List[int]:
    '''
    The function extracts even numbers from a list of integers recursively.

    Processes the list from end to start using negative indexing
    and builds a new list containing only even numbers.

    Args:
        numbers (List[int]): List of integers to process
        count_elements (int): Number of elements to process

    Returns:
        List[int]: List containing only even numbers from the original list
    '''

    if count_elements <= 0:
        return []

    if numbers[-count_elements] % 2 > 0:
        return odd_list(numbers, count_elements - 1)

    return [numbers[-count_elements]] + odd_list(numbers, count_elements - 1)


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        numbers = list(map(int, input('Введите целые числа через пробел:').split()))
        count_elements = len(numbers)

        print(odd_list(numbers, count_elements))

    except ValueError:
        print("Ошибка: введите корректные целые числа")


if __name__ == "__main__":
    main()
