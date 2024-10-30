"""implement algorithms to practice computational thinking"""

__author__ = "730771611"


def all(lst: list[int], num: int) -> bool:
    if len(lst) == 0:  # if it's empty
        return False
    for item in lst:  # for every item, if it isn't the number, say it's false
        if item != num:
            return False
    return True


def max(lst: list[int]) -> int:
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")

    max_value = lst[0]  # the max value is the first item in the list
    for num in range(1, len(lst)):
        # for every num in the range, if the number is greater than the first[max_value] itll replace the max_value
        if lst[num] > max_value:
            max_value = lst[num]
    return max_value


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    if len(lst1) != len(lst2):
        return False
    for idx in range(
        len(lst1)
    ):  # for every item in the list, we are seeing if it is the same at every point in both lists
        if lst1[idx] != lst2[idx]:
            return False
    return True


def extend(lst1: list[int], lst2: list[int]) -> None:
    for item in lst2:
        lst1.append(item)
