"""
John McDonough
    github - movinalot
    Advent of Code 2021
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2021"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(int(line))

if DEBUG:
    print(len(puzzle_data), puzzle_data)

DEPTH_INCREASES = 0

for count, value in enumerate(puzzle_data):

    if count == 0:
        continue

    if puzzle_data[count] > puzzle_data[count - 1]:
        DEPTH_INCREASES += 1

ANSWER = DEPTH_INCREASES

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
