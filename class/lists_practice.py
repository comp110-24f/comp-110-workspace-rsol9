"""basic syntax of lists"""

# two versions:

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# string analogy:
my_name: str = ""  # literal
my_name: str = str()  # constructor

# adding a value to a list, use ()
my_numbers.append(1.5)
print(my_numbers)  # [1.5]
my_numbers.append(2.3)
print(my_numbers)  # [1.5, 2.3]

# new list with already stored values of 102, 86, 94
game_points: list[int] = [102, 86, 94]
print(game_points)

# indexing for strings starts at 0 too! two ways:
# 1:
print(game_points[2])
# 2:
last_game = int = game_points[2]
print(last_game)

# how to modify the list, use []
game_points[1] = 72
print(game_points)

# length of list - starts at 1!
len(game_points)

# removing items from list, use ()
game_points.pop(1)
print(game_points)

# function name: display
# parameter: list of int
# rv: none
# print every element in the input list
# call displace on game_points


def display(int_list: list[int]) -> None:
    """displays all elements of int_list"""
    idx = 0  # OR index: int = 0
    while idx < len(int_list):
        print(int_list[idx])
        idx += 1


print(display(int_list=game_points))


# lists in memory
