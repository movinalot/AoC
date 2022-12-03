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
PART = "1"
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

for rucksack_items in puzzle_data:

    half_items = int(len(rucksack_items)/2)

    compartment_1 = set(rucksack_items[:half_items])
    compartment_2 = set(rucksack_items[half_items:])

    common_item = compartment_1.intersection(compartment_2)

    ITEM_PRIORITY = string.ascii_letters.find(next(iter(common_item))) + 1

    TOTAL_COMMON_ITEM_PRIORITY += ITEM_PRIORITY

    if DEBUG:
        print(compartment_1)
        print(compartment_2)

        print(ITEM_PRIORITY)
        print(common_item)

ANSWER = TOTAL_COMMON_ITEM_PRIORITY
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
