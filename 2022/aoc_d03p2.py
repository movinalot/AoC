"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

import string

TESTING = 0
DEBUG = 0
DAY = "03"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_COMMON_ITEM_PRIORITY = 0

for i in range(0, len(puzzle_data), 3):

    common_item = set.intersection(
        set(puzzle_data[i]),
        set(puzzle_data[i+1]),
        set(puzzle_data[i+2])
    )

    ITEM_PRIORITY = string.ascii_letters.find(next(iter(common_item))) + 1

    TOTAL_COMMON_ITEM_PRIORITY += ITEM_PRIORITY

    if DEBUG:
        print(common_item)

ANSWER = TOTAL_COMMON_ITEM_PRIORITY
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
