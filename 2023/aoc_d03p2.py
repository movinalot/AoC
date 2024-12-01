"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

import re

TESTING = 1
DEBUG = 1
DAY = "03"
YEAR = "2023"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
        "....*.....",
        "....*.....",
        ".342.582..",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

for row, line in enumerate(puzzle_data):
    GEARS=[(row, m.start()) for m in re.finditer("\\*", line)]

    if len(GEARS) == 0:
        continue

    print(GEARS)

    for g, gear in enumerate(GEARS):
        print(gear)
        if puzzle_data[gear[0] - 1][gear[1] - 1].isdigit():
            print("upleft")
        if puzzle_data[gear[0] - 1][gear[1]].isdigit():
            print("upcenter")
        if puzzle_data[gear[0] - 1][gear[1] + 1].isdigit():
            print("upright")
        if puzzle_data[gear[0]][gear[1] - 1].isdigit():
            print("left")
        if puzzle_data[gear[0]][gear[1] + 1].isdigit():
            print("right")
        if puzzle_data[gear[0] + 1][gear[1] - 1].isdigit():
            print("downleft")
        if puzzle_data[gear[0] + 1][gear[1]].isdigit():
            print("downcenter")
        if puzzle_data[gear[0] + 1][gear[1] + 1].isdigit():
            print("downright")


ANSWER = None

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
