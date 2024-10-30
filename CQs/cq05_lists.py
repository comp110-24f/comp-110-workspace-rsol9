"""Mutating functions."""

__author__ = "730771611"


def manual_append(list: list[int], num: int) -> None:  # two parameters
    list.append(num)  # appending


def double(list: list[int]) -> None:
    i: int = 0  # index starting at 0
    while i < len(list):
        list[i] *= 2  # multiply each value by 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
