"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

TESTING = 0
DEBUG = 0
DAY = "06"
YEAR = "2025"
PART = "1"
ANSWER = 0

if TESTING:
    puzzle_data = [
        "123 328  51 64",
        "45 64  387 23",
        "6 98  215 314",
        "*   +   *   +"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

for col in range(len(puzzle_data[0].split())):
    if DEBUG:
        print("Column", col)

    if puzzle_data[len(puzzle_data)-1].split()[col] == "*":
        ROW_TOTAL = 1
    else:
        ROW_TOTAL = 0

    for row in range(len(puzzle_data)-1):

        if puzzle_data[len(puzzle_data)-1].split()[col] == "*":
            ROW_TOTAL *= int(puzzle_data[row].split()[col])
        elif puzzle_data[len(puzzle_data)-1].split()[col] == "+":
            ROW_TOTAL += int(puzzle_data[row].split()[col])

        if DEBUG:
            print(
                "  Row", row, "value:",
                puzzle_data[row].split()[col],
                ROW_TOTAL,
                puzzle_data[len(puzzle_data)-1].split()[col]
            )

    ANSWER += ROW_TOTAL


print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
