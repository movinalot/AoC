"""
John McDonough
    github - movinalot
    Advent of Code 2021
"""

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2021"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

POSITION_HORIZ = 0
POSITION_DEPTH = 0

for count, value in enumerate(puzzle_data):

    motion = value.split()[0]
    amount = int(value.split()[1])

    if DEBUG:
        print(motion, amount)

    if motion == "forward":
        POSITION_HORIZ += amount
    if motion == "up":
        POSITION_DEPTH -= amount
    if motion == "down":
        POSITION_DEPTH += amount

ANSWER = POSITION_HORIZ * POSITION_DEPTH

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
