__author__ = "730771611"


def find_and_remove_max(lst: list[int]) -> int:
    if len(lst) == 0:
        return -1

    maxvalue = lst[0]  # maxvalue is the first index in the list
    idx = 0
    while idx < len(lst):
        if maxvalue < lst[idx]:
            maxvalue = lst[idx]
        else:  # only add to index if the list doesn't change
            idx += 1

    index = 0
    while index < len(lst):
        if maxvalue == lst[index]:
            lst.pop(index)  # remove that index in the list
        else:
            index += 1

    return maxvalue
