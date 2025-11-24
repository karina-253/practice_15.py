from typing import List, Optional


def maxlist(numbers: List[int]) -> Optional[int]:
    '''
    The function finds the maximum element in a list of integers recursively.
    Uses divide and conquer approach by comparing first element
    with maximum of the rest of the list.

    Args:
        numbers (List[int]): List of integers to find maximum from

    Returns:
        Optional[int]: Maximum element or None if list is empty
    '''

    if len(numbers) == 0:
        return 0

    if len(numbers) == 1:
        return numbers[0]

    remain_ind = maxlist(numbers[1:])

    return numbers[0] if numbers[0] > remain_ind else remain_ind


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        numbers = list(map(int, input('Введите целые числа через пробел:').split()))

        if len(numbers) == 0:
            print('Ошибка: список должен содержать хотя бы одно число')
        else:
            print(maxlist(numbers))

    except ValueError:
        print('Ошибка: введите целые числа через пробелы.')


if __name__ == "__main__":
    main()
  
