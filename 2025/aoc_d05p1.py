"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

# pylint: disable=line-too-long

TESTING = 0
DEBUG = 0
DAY = "05"
YEAR = "2025"
PART = "1"
ANSWER = 0


if TESTING:
    puzzle_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",

        "1",
        "5",
        "8",
        "11",
        "17",
        "32"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

fresh_ranges = []
ingredients = []
for line in puzzle_data:
    if line == "":
        continue
    if "-" in line:
        fresh_ranges.append(line)
    else:
        ingredients.append(int(line))

for ingredient in ingredients:
    for fresh_range in fresh_ranges:
        low, high = map(int, fresh_range.split("-"))
        if low <= ingredient <= high:
            ANSWER += 1
            break

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
