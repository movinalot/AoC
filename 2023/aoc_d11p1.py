"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""
import re

TESTING = 0
DEBUG = 0
DAY = "11"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

EMPTY_ROWS = []
EMPTY_COLS = []
GALAXIES = []

for row, line in enumerate(puzzle_data):
    GALAXIES.extend([(row, m.start()) for m in re.finditer("#", line)])
    if "#" not in line:
        EMPTY_ROWS.append(row)

for i in range(len(puzzle_data[0])):
    EMPTY_COL = True
    for line in puzzle_data:
        if line[i] == "#":
            EMPTY_COL = False
            break
    if EMPTY_COL:
        EMPTY_COLS.append(i)

if DEBUG:
    print(GALAXIES, EMPTY_ROWS, EMPTY_COLS)

TOTAL_DISTANCE = 0
UNI_GROWTH = 1
for g, galaxy in enumerate(GALAXIES):
    for i in range(g + 1, len(GALAXIES)):
        G1_ROW = galaxy[0]
        G1_COL = galaxy[1]
        G2_ROW = GALAXIES[i][0]
        G2_COL = GALAXIES[i][1]

        for row in EMPTY_ROWS:
            if galaxy[0] > row:
                G1_ROW += UNI_GROWTH
            if GALAXIES[i][0] > row:
                G2_ROW += UNI_GROWTH
        for col in EMPTY_COLS:
            if galaxy[1] > col:
                G1_COL += UNI_GROWTH
            if GALAXIES[i][1] > col:
                G2_COL += UNI_GROWTH

        DISTANCE = abs(G1_ROW - G2_ROW) + abs(G1_COL - G2_COL)
        TOTAL_DISTANCE += DISTANCE

ANSWER = TOTAL_DISTANCE

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
