"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2024"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

LOCS1 = []
LOCS2 = []

for i, line in enumerate(range(len(puzzle_data))):
    LOCS1.append(puzzle_data[line].split()[0])
    LOCS2.append(puzzle_data[line].split()[1])

LOC_SAME_SUM = 0
for i, j in enumerate(range(len(LOCS1))):
    LOC_SAME_SUM += LOCS2.count(LOCS1[j]) * int(LOCS1[j])


ANSWER = LOC_SAME_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
