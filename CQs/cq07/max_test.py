__author__ = "730771611"

from find_max import find_and_remove_max

def test1_find_and_remove_max() -> None:
    a: list[int] = [3, 4, 5, 4, 5, 5]  # example list, make sure it removes 5
    assert find_and_remove_max(a) == 5, 5, 5

def test2_find_and_remove_max() -> None:
    a: list[int] = [3, 4, 5, 4, 5, 5]  # make sure we get the final fixed list
    find_and_remove_max(a)
    assert a == [3, 4, 4]


def test3_find_and_remove_max() -> None:
    a: list[int] = []  # empty list should give -1
    assert find_and_remove_max(a) == -1
