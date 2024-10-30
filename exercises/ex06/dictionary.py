"""In this exercise you will get some practice with dictionary functions!"""

__author__ = "730771611"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """inverts the og dict"""
    new_dicts: dict[str, str] = dict()
    for key in input_dict:
        value = input_dict[key]
        if value in new_dicts:
            raise KeyError("Duplicate key found!")
        new_dicts[value] = key
    return new_dicts


def favorite_color(colors: dict[str, str]) -> str:
    """finds the most popular color"""
    color_count: dict[str, int] = {}
    most_popular = ""
    highest_count = 0

    for name in colors:  # for every name in of that color
        color = colors[name]  # color becomes that color
        if (
            color in color_count
        ):  # if this color is already present in the dict, add a number to it(tally)
            color_count[color] += 1
        else:  # if not, add it
            color_count[color] = 1

        # now we have a dict, color_count, with a list of all the colors in the og and how many times each was chosen

        if (
            color_count[color] == highest_count and most_popular == ""
        ):  # otherwise, this must be the highest and first number
            most_popular = color
        elif (
            color_count[color] > highest_count
        ):  # if this color is greater than the highest number, replace it
            most_popular = color
            highest_count = color_count[color]

    return most_popular


# commnte


def count(items: list[str]) -> dict[str, int]:
    """counts how many times sum appears in the dict"""
    frequency: dict[str, int] = {}
    for item in items:
        if item in frequency:  # if its alr there
            frequency[item] += 1
        else:  # if it isnt there
            frequency[item] = 1

    return frequency


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter"""
    result: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """this function will mutate and return None"""
    if day in attendance:  # if they alr in, add again
        if student not in attendance[day]:
            attendance[day] += [student]
    else:
        attendance[day] = [student]
