"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2020"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [1721,979,366,299,675,1456]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(int(line))

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TARGET = 2020

for x in puzzle_data:

    y = TARGET - x
    if y in puzzle_data:
        if DEBUG:
            print(x, y, puzzle_data.index(x), puzzle_data.index(y))

        ANSWER = x * y
        break

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
