"""Summing the elements of a list using different loops"""

__author__ = "730771611"


def w_sum(vals: list[float]) -> float:
    idx = 0
    total = 0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


print(w_sum([1.1, 0.9, 1.0]))
print(w_sum([]))


def f_sum(vals: list[float]) -> float:
    total = 0
    for x in vals:  # random placeholder for loop
        total += x
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0
    for x in range(0, len(vals)):
        total = vals[x] + total
    return total
