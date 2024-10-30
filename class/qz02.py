stats: list[int] = [7, 8, 9]
index: int = 0
total: int = 100
"""while index < len(stats):
    total -= stats[index]
    index += 1"""
for i in stats:
    total -= stats[index]
    print(total)
    print(stats)
