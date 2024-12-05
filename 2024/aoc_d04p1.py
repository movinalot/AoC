"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

TESTING = 0
DEBUG = 0
DAY = "04"
YEAR = "2024"
PART = "1"
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

SEARCH_WORD = "XMAS"
SEARCH_WORD_LEN = len(SEARCH_WORD) - 1
TOTAL_XMAS = 0

for row, i in enumerate(range(len(puzzle_data))):
    for col, j in enumerate(range(len(puzzle_data[i]))):

        # up to left
        if row - SEARCH_WORD_LEN >= 0 and col - SEARCH_WORD_LEN >= 0:
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row - 1][col - 1] == SEARCH_WORD[1]
                and puzzle_data[row - 2][col - 2] == SEARCH_WORD[2]
                and puzzle_data[row - 3][col - 3] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("up to left", row, col, puzzle_data[row][col])
        # straight up
        if row - SEARCH_WORD_LEN >= 0:
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row - 1][col] == SEARCH_WORD[1]
                and puzzle_data[row - 2][col] == SEARCH_WORD[2]
                and puzzle_data[row - 3][col] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("straight up", row, col, puzzle_data[row][col])
        # up to right
        if row - SEARCH_WORD_LEN >= 0 and col + SEARCH_WORD_LEN < len(puzzle_data[i]):
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row - 1][col + 1] == SEARCH_WORD[1]
                and puzzle_data[row - 2][col + 2] == SEARCH_WORD[2]
                and puzzle_data[row - 3][col + 3] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("up to right", row, col, puzzle_data[row][col])
        # straight left
        if col - SEARCH_WORD_LEN >= 0:
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row][col - 1] == SEARCH_WORD[1]
                and puzzle_data[row][col - 2] == SEARCH_WORD[2]
                and puzzle_data[row][col - 3] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("straight left", row, col, puzzle_data[row][col])
        # straight right
        if col + SEARCH_WORD_LEN < len(puzzle_data[i]):
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row][col + 1] == SEARCH_WORD[1]
                and puzzle_data[row][col + 2] == SEARCH_WORD[2]
                and puzzle_data[row][col + 3] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("straight right", row, col, puzzle_data[row][col])
        # down to left
        if row + SEARCH_WORD_LEN < len(puzzle_data) and col - SEARCH_WORD_LEN >= 0:
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row + 1][col - 1] == SEARCH_WORD[1]
                and puzzle_data[row + 2][col - 2] == SEARCH_WORD[2]
                and puzzle_data[row + 3][col - 3] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("down to left", row, col, puzzle_data[row][col])
        # straight down
        if row + SEARCH_WORD_LEN < len(puzzle_data):
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row + 1][col] == SEARCH_WORD[1]
                and puzzle_data[row + 2][col] == SEARCH_WORD[2]
                and puzzle_data[row + 3][col] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("straight down", row, col, puzzle_data[row][col])
        # down to right
        if row + SEARCH_WORD_LEN < len(puzzle_data) and col + SEARCH_WORD_LEN < len(
            puzzle_data[i]
        ):
            if (
                puzzle_data[row][col] == SEARCH_WORD[0]
                and puzzle_data[row + 1][col + 1] == SEARCH_WORD[1]
                and puzzle_data[row + 2][col + 2] == SEARCH_WORD[2]
                and puzzle_data[row + 3][col + 3] == SEARCH_WORD[3]
            ):
                TOTAL_XMAS += 1
                if DEBUG:
                    print("down to right", row, col, puzzle_data[row][col])

ANSWER = TOTAL_XMAS

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
