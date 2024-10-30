"""implement some more list utility functions"""

__author__ = "730771611"


def only_evens(lst: list[int]) -> list[int]:

    result = []

    for num in lst:
        if num % 2 == 0:
            result.append(num)

    return result


def sub(lst: list[int], start: int, end: int) -> list[int]:

    new_list = []

    if len(lst) == 0 or start >= len(lst) or end <= 0:
        return new_list

    if start < 0:  # anything less than 0 is now 0
        start = 0

    if end > len(
        lst
    ):  # anything greater than the ength of the list is now the last item
        end = len(lst)

    for i in range(start, end):  # add everything in between that range
        new_list.append(lst[i])

    return new_list


def add_at_index(lst: list[int], element: int, index: int) -> None:

    if index < 0 or index > len(lst):
        raise IndexError("Index is out of bounds for the input list")

    lst.append(0)  # this will shift the numbers in the list down the right

    i = len(lst) - 1  # i is now the last element in the list

    while i > index:  # while the last element in the list is less that the given index
        lst[i] = lst[i - 1]  # shift the last element to the rigth one, and keep going
        i -= 1

    lst[index] = element
