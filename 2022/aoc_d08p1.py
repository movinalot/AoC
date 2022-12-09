"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "08"
YEAR = "2022"
PART = "1"
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

TREES_VISIBLE = 0
TREE_HEIGHT_ARRAY = []
TREE_VISIBLE_ARRAY = []

for line in puzzle_data:
    TREE_HEIGHT_ARRAY.append([*line])

for i in range(len(puzzle_data)):
    TREE_VISIBLE_ARRAY.append([])
    if i in (0, len(puzzle_data)-1):
        for _ in range(len(TREE_HEIGHT_ARRAY[i])):
            TREE_VISIBLE_ARRAY[i].append('V')
            TREES_VISIBLE += 1
    else:
        for j in range(len(TREE_HEIGHT_ARRAY[i])):
            if j in (0, len(TREE_HEIGHT_ARRAY[i])-1):
                TREE_VISIBLE_ARRAY[i].append('V')
                TREES_VISIBLE += 1
                continue

            TREE_VISIBLE_ARRAY[i].append('N')

            # Check North visibility
            # print("North")
            NORTH_VISIBLE = True
            for north in range(i-1, -1, -1):
                #print("Column: ", j, "Row: ", north)
                if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[north][j]:
                    continue
                NORTH_VISIBLE = False
                break

            # Check South visibility
            SOUTH_VISIBLE = True
            # print("South")
            for south in range(i+1, len(TREE_HEIGHT_ARRAY), 1):
                #print("Column: ", j, "Row: ", south)
                if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[south][j]:
                    continue
                SOUTH_VISIBLE = False
                break

            # Check East visibility
            EAST_VISIBLE = True
            # print("East")
            for east in range(j-1, -1, -1):
                #print("Column: ", east, "Row: ", i)
                if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[i][east]:
                    continue
                EAST_VISIBLE = False
                break

            # Check West visibility
            WEST_VISIBLE = True
            # print("West")
            for west in range(j+1, len(TREE_HEIGHT_ARRAY[i]), 1):
                #print("Column: ", west, "Row: ", i)
                if TREE_HEIGHT_ARRAY[i][j] > TREE_HEIGHT_ARRAY[i][west]:
                    continue
                WEST_VISIBLE = False
                break

            if NORTH_VISIBLE or SOUTH_VISIBLE or EAST_VISIBLE or WEST_VISIBLE:
                TREE_VISIBLE_ARRAY[i][j] = "V"
                TREES_VISIBLE += 1

if DEBUG:
    print(TREE_HEIGHT_ARRAY)
    print(TREE_VISIBLE_ARRAY)

ANSWER = TREES_VISIBLE
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
