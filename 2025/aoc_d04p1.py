"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

# pylint: disable=line-too-long

TESTING = 0
DEBUG = 1
DAY = "04"
YEAR = "2025"
PART = "1"
ANSWER = 0

def get_neighbors(matrix, row, col):
    """
    Finds all valid neighbors (horizontal, vertical, and diagonal) for a 
    given cell (row, col) in a 2D matrix, handling edge cases.
    """
    neighbors = []
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # Define all 8 possible directional offsets:
    # (delta_row, delta_col)
    directions = [
        (-1, -1), (-1, 0), (-1, 1), # Top row (left, center, right)
        (0, -1),           (0, 1),  # Middle row (left, right)
        (1, -1),  (1, 0),  (1, 1)   # Bottom row (left, center, right)
    ]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new coordinates are within the matrix boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if matrix[new_row][new_col] == "@":
                neighbors.append(matrix[new_row][new_col])
                #neighbors.append((new_row, new_col, matrix[new_row][new_col]))

    return neighbors


if TESTING:
    puzzle_data = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

for row_idx, line in enumerate(puzzle_data):
    for col_idx, char in enumerate(line):
        if char == "@":
            neighbors_list = get_neighbors(puzzle_data, row_idx, col_idx)
            if len(neighbors_list) < 4:
                ANSWER += 1
            if DEBUG:
                print(f"Cell ({row_idx}, {col_idx}) has neighbors: {neighbors_list}")

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
