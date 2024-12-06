"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

TESTING = 0
DEBUG = 0
DAY = "06"
YEAR = "2024"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

GUARD_DIRECTION = "N"
GUARD_VISITED = []
GUARD_ROW = 0
GUARD_COL = 0

for row, line in enumerate(puzzle_data):
    for col, char in enumerate(line):
        if char == "^":
            if DEBUG:
                print("Guard starts at row:", row, "col:", col)
            GUARD_ROW = row
            GUARD_COL = col
            break

while True:
    if (GUARD_ROW, GUARD_COL) not in GUARD_VISITED:
        GUARD_VISITED.append((GUARD_ROW, GUARD_COL))
        if DEBUG:
            print("Guard at row:", GUARD_ROW, "col:", GUARD_COL)

    if GUARD_DIRECTION == "N":
        if DEBUG:
            print("Guard facing North")
        if GUARD_ROW - 1 < 0 or GUARD_COL + 1 > len(puzzle_data[GUARD_ROW]) - 1:
            break
        if puzzle_data[GUARD_ROW - 1][GUARD_COL] == "#":
            if DEBUG:
                print("Guard changing to facing E")
            GUARD_DIRECTION = "E"
            GUARD_COL += 1
        else:
            GUARD_ROW -= 1
        continue

    if GUARD_DIRECTION == "E":
        if DEBUG:
            print("Guard facing East")
        if (
            GUARD_COL + 1 > len(puzzle_data[GUARD_ROW]) - 1
            or GUARD_ROW + 1 > len(puzzle_data) - 1
        ):
            break
        if puzzle_data[GUARD_ROW][GUARD_COL + 1] == "#":
            if DEBUG:
                print("Guard changing to facing S")
            GUARD_DIRECTION = "S"
            GUARD_ROW += 1
        else:
            GUARD_COL += 1
        continue

    if GUARD_DIRECTION == "S":
        if DEBUG:
            print("Guard facing South")
        if GUARD_ROW + 1 > len(puzzle_data) - 1 or GUARD_COL - 1 < 0:
            break
        if puzzle_data[GUARD_ROW + 1][GUARD_COL] == "#":
            if DEBUG:
                print("Guard changing to facing W")
            GUARD_DIRECTION = "W"
            GUARD_COL -= 1
        else:
            GUARD_ROW += 1
        continue

    if GUARD_DIRECTION == "W":
        if DEBUG:
            print("Guard facing West")
        if GUARD_COL - 1 < 0 or GUARD_ROW - 1 < 0:
            break
        if puzzle_data[GUARD_ROW][GUARD_COL - 1] == "#":
            if DEBUG:
                print("Guard changing to facing N")
            GUARD_DIRECTION = "N"
            GUARD_ROW -= 1
        else:
            GUARD_COL -= 1
        continue

ANSWER = len(GUARD_VISITED)

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
