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
PART = "1"
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

if DEBUG:
    print(len(puzzle_data), puzzle_data)

ANSWER = 0

grid_line = 0
grid_space = 0
move = 3
down = 1
tree_count = 0
grid_lines = len(puzzle_data)-1     # lists start at 0
restart_len = len(puzzle_data[0])-1 # lists start at 0

while True:
    if grid_space + move > restart_len:
        grid_space = grid_space + move - restart_len - 1 # lists start at 0
    else:
        grid_space = grid_space + move

    if DEBUG:
        print(grid_line, grid_space)

    grid_line += down
    if grid_line > grid_lines:
        ANSWER = tree_count
        break

    if puzzle_data[grid_line][grid_space] == '#':
        tree_count += 1


print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
