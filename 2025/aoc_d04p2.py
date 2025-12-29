"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

# pylint: disable=line-too-long

TESTING = 0
DEBUG = 0
DAY = "04"
YEAR = "2025"
PART = "2"
ANSWER = 0

def process_matrix(matrix):
    """
    Processes the matrix to count the number of "@" cells that have fewer than
    four neighboring "@" cells.
    """
    accessible_rolls = []
    count = 0
    for row_idx, row in enumerate(matrix):
        for col_idx, char in enumerate(row):
            if char == "@":
                neighbors_list = get_neighbors(matrix, row_idx, col_idx)
                if len(neighbors_list) < 4:
                    count += 1
                    accessible_rolls.append((row_idx, col_idx))
                if DEBUG:
                    print(f"Cell ({row_idx}, {col_idx}) has neighbors: {neighbors_list}")
    return accessible_rolls

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

current_matrix = [row[:] for row in puzzle_data]

while True:
    rolls = process_matrix(current_matrix)

    if not rolls:
        break

    ANSWER += len(rolls)
    if DEBUG:
        print(f"Found rolls: {len(rolls)} {rolls}")

    for roll in rolls:
        row_index, col_index = roll
        current_matrix[row_index] = current_matrix[row_index][:col_index] + "." + current_matrix[row_index][col_index + 1:]

    if DEBUG:
        for r in current_matrix:
            print(r)

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
