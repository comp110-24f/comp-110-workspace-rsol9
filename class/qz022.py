my_list: list[int] = list()

my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)

print(my_list)

my_list.pop(2)
print(my_list)

dog: int = my_list[2]
print(dog)

print(len(my_list))

my_list[0] = 0
print(my_list)

"""
my_dict: dict[int, str] = {}
my_dict[8] = "eight"
my_dict[0] = "zero"
my_dict[3] = "three"
my_dict[-1] = "negative one"
my_dict.pop(3)
my_dict[0] = "cat"
print(len(my_dict))
my_dict[8] = "zero"
print(my_dict)
"""
"""
my_dict: dict[int, str] = {0: "dog", 1: "cat", 2: "mouse", 3: "bird", 4: "whale"}

"""
"""
def size_of_strings(strings: list[str]) -> list[int]:
    result: list[int] = []
    for x in range(0, len(strings)):
        result.append(len(strings[x]))
    return result


def sum(lst: list[str]) -> int:
    total: int = 0
    for i in range(0, len(lst)):
        total += len(lst[i])
    return total


def excl(strings: list[str]) -> None:
    for i in range(0, len(strings)):
        strings[i] += "1"


def ts(string: str) -> list[str]:
    final: list[str] = list()
    for i in range(0, len(string)):
        add: str = string[i]
        final.append(add)


def find_even(nums: list[int]) -> int:
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1


def test_find_even_use_case() -> None:
    nums = [1, 3, 5, 4, 7]
    assert find_even(nums) == 4


def sum_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise Exception("Empty list - no elements to add")

    total: int = numbers[0]
    for i in range(1, len(numbers)):
        total += numbers[i]

    return total


def test_list_sum_use_case() -> None:
    numbers = [1, 2, 3, 4, 5]
    assert sum_numbers(numbers) == 15


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime_use_case() -> None:
    assert is_prime(3) == True


def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    for d in dicts:
        d[key] = value
"""

"""
def odd_and_even(lst: list[int]) -> list[int]:
    new_list: list[int] = list()
    for i in range(0, len(lst)):
        if i % 2 == 0:
            if lst[i] % 2 == 1:
                new_list.append(lst[i])
    return new_list


# WRONG
def short_words(lst: list[str]) -> list[str]:
    new_list: list[str] = list()
    too_long: list[str] = list()
    for i in range(0, len(lst)):
        if len(lst[i]) > 5:
            too_long.append(lst[i])
        else:
            new_list.append(lst[i])


def value_exists(ts: dict[str, int], num: int) -> bool:
    for key in ts:
        if [key] == num:
            return True
        return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        else:
            inp[key] -= n
"""
