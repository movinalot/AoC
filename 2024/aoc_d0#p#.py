"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""
import itertools

TESTING = 1
DEBUG = 0
DAY = "07"
YEAR = "2024"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

for line in puzzle_data:
    print(line)
    print(list(itertools.combinations(list(map(int, line.split(": ")[1].split())), 2)))

ANSWER = None

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
