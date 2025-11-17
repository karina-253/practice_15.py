from typing import List


def ind_maxlist(numbers: List[int]) -> int:
    '''
    The function finds the index of the maximum element in a list of integers recursively.

    Uses approach by comparing first element index with index
    of maximum element in the rest of the list.

    Args:
        numbers (List[int]): List of integers to find maximum index from

    Returns:
        int: Index of the maximum element in the list.
    '''

    if len(numbers) == 1:
        return 0

    remain_max_ind = ind_maxlist(numbers[1:]) + 1

    if numbers[0] >= numbers[remain_max_ind]:
        return 0
    else:
        return remain_max_ind


def main() -> None:
    '''
     The main function for data entry.
    '''

    try:
        numbers = list(map(int, input().split()))

        if len(numbers) == 0:
            print("Ошибка: список должен содержать хотя бы одно число")
        else:
            print(ind_maxlist(numbers))

    except ValueError:
        print("Ошибка: введите целые числа, разделенные пробелами")


if __name__ == "__main__":
    main()
