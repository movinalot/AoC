"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

# pylint: disable=line-too-long

TESTING = 0
DEBUG = 0
DAY = "03"
YEAR = "2025"
PART = "1"
ANSWER = None


if TESTING:
    puzzle_data = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_JOLTAGE = 0

for line in puzzle_data:

    FIRST_HIGHEST_VALUE = line[0]
    FIRST_HIGHEST_INDEX = 0

    for i in range(len(line) - 2):
        if line[i + 1] > FIRST_HIGHEST_VALUE:
            FIRST_HIGHEST_VALUE = line[i + 1]
            FIRST_HIGHEST_INDEX = i + 1

    if DEBUG:
        print(FIRST_HIGHEST_VALUE, FIRST_HIGHEST_INDEX)

    SECOND_HIGHEST_VALUE = line[FIRST_HIGHEST_INDEX + 1]
    SECOND_HIGHEST_INDEX = FIRST_HIGHEST_INDEX + 1

    for j in range(FIRST_HIGHEST_INDEX + 1, len(line) - 1):
        if line[j + 1] > SECOND_HIGHEST_VALUE:
            SECOND_HIGHEST_VALUE = line[j + 1]
            SECOND_HIGHEST_INDEX = j + 1

    if DEBUG:
        print(SECOND_HIGHEST_VALUE, SECOND_HIGHEST_INDEX)

    LINE_JOLTAGE = int(FIRST_HIGHEST_VALUE + SECOND_HIGHEST_VALUE)

    if DEBUG:
        print("Line joltage:", LINE_JOLTAGE)

    TOTAL_JOLTAGE += LINE_JOLTAGE

ANSWER = TOTAL_JOLTAGE

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
