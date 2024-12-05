"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

TESTING = 0
DEBUG = 0
DAY = "04"
YEAR = "2024"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

SEARCH_WORD = "MAS"
SEARCH_WORD_LEN = len(SEARCH_WORD) - 1
TOTAL_XMAS = 0

for row, i in enumerate(range(len(puzzle_data))):
    for col, j in enumerate(range(len(puzzle_data[i]))):

        if (
            puzzle_data[row][col] == "A"
            and row - 1 >= 0
            and col - 1 >= 0  # up to left
            and row - 1 >= 0
            and col + 1 < len(puzzle_data[i])  # up to right
            and row + 1 < len(puzzle_data)
            and col - 1 >= 0  # down to left
            and row + 1 < len(puzzle_data)
            and col + 1 < len(puzzle_data[i])  # down to right
        ):
            if (
                (
                    puzzle_data[row - 1][col - 1] == "M"
                    and puzzle_data[row + 1][col + 1] == "S"
                )
                or (
                    puzzle_data[row - 1][col - 1] == "S"
                    and puzzle_data[row + 1][col + 1] == "M"
                )
            ) and (
                (
                    puzzle_data[row - 1][col + 1] == "M"
                    and puzzle_data[row + 1][col - 1] == "S"
                )
                or (
                    puzzle_data[row - 1][col + 1] == "S"
                    and puzzle_data[row + 1][col - 1] == "M"
                )
            ):
                TOTAL_XMAS += 1


ANSWER = TOTAL_XMAS

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
