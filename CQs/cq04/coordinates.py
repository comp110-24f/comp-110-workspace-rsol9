"""It will print the formatted pairs of each character in the two input strings."""

__author__ = "730771611"


def get_coords(
    xs: str, ys: str
) -> None:  # defining function get_coords, concatenating different index's of strings

    indexxs: int = 0  # index for counting xs
    while indexxs < len(xs):
        indexys: int = 0  # index for counting ys
        while indexys < len(ys):
            print(xs[indexxs], ys[indexys])
            indexys += 1
        indexxs += 1
