"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "08"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TREE_HEIGHT_ARRAY = []
HIGHEST_SENIC_SCORE = 0

for line in puzzle_data:
    TREE_HEIGHT_ARRAY.append([*line])

for i in range(len(puzzle_data)):
    if i in (0, len(puzzle_data)-1):
        continue

    for j in range(len(TREE_HEIGHT_ARRAY[i])):
        if j in (0, len(TREE_HEIGHT_ARRAY[i])-1):
            continue

        # Check North visibility
        NORTH_SCORE = 0
        for north in range(i-1, -1, -1):
            if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[north][j]:
                NORTH_SCORE += 1
            elif TREE_HEIGHT_ARRAY[i][j] <= TREE_HEIGHT_ARRAY[north][j]:
                NORTH_SCORE += 1
                break

        # Check South visibility
        SOUTH_SCORE = 0
        for south in range(i+1, len(TREE_HEIGHT_ARRAY), 1):
            if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[south][j]:
                SOUTH_SCORE += 1
            elif TREE_HEIGHT_ARRAY[i][j] <= TREE_HEIGHT_ARRAY[south][j]:
                SOUTH_SCORE += 1
                break

        # Check East visibility
        EAST_SCORE = 0
        for east in range(j-1, -1, -1):
            if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[i][east]:
                EAST_SCORE += 1
            elif TREE_HEIGHT_ARRAY[i][j] <= TREE_HEIGHT_ARRAY[i][east]:
                EAST_SCORE += 1
                break

        # Check West visibility
        WEST_SCORE = 0
        for west in range(j+1, len(TREE_HEIGHT_ARRAY[i]), 1):
            if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[i][west]:
                WEST_SCORE += 1
            elif TREE_HEIGHT_ARRAY[i][j] <= TREE_HEIGHT_ARRAY[i][west]:
                WEST_SCORE += 1
                break

        if NORTH_SCORE * SOUTH_SCORE * EAST_SCORE * WEST_SCORE > HIGHEST_SENIC_SCORE:
            HIGHEST_SENIC_SCORE = NORTH_SCORE * SOUTH_SCORE * EAST_SCORE * WEST_SCORE

if DEBUG:
    print(TREE_HEIGHT_ARRAY)

ANSWER = HIGHEST_SENIC_SCORE
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
