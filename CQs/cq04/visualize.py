"""this will import the concat function under concatenation.py"""

__author__ = "730771611"


from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

"""importing both files"""
x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
