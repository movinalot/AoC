"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name

TESTING = 0
DEBUG = 0
DAY = "03"
YEAR = "2020"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

SLOPES = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]
if DEBUG:
    print(len(puzzle_data), puzzle_data)

ANSWER = 0

grid_line = 0
grid_space = 0
tree_count = 0
grid_lines = len(puzzle_data)-1     # lists start at 0
restart_len = len(puzzle_data[0])-1 # lists start at 0
tree_counts = []

for SLOPE in SLOPES:
    while True:
        if grid_space + SLOPE[0] > restart_len:
            grid_space = grid_space + SLOPE[0] - restart_len - 1 # lists start at 0, wrap around
        else:
            grid_space = grid_space + SLOPE[0]                   # just move to the right

        if DEBUG:
            print(grid_line, grid_space)

        grid_line += SLOPE[1]
        if grid_line > grid_lines:
            if ANSWER == 0:
                ANSWER = tree_count
            else:
                ANSWER *= tree_count
            tree_counts.append(tree_count) # don't need this, but nice to have for debug
            tree_count = 0
            grid_line = 0
            grid_space = 0
            break

        if puzzle_data[grid_line][grid_space] == '#':
            tree_count += 1

if DEBUG:
    print(tree_counts)

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
