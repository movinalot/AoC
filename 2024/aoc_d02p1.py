"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2024"
PART = "1"
ANSWER = None


def is_safe(reports):
    """Check if the reports are safe"""

    if DEBUG:
        print("checking if reports are safe")

    safe_reports = True

    for i in range(len(reports) - 1):
        diff_levels = abs(int(reports[i]) - int(reports[i + 1]))
        if DEBUG:
            print(int(reports[i]), int(reports[i + 1]), diff_levels)
        if not 0 < diff_levels <= 3:
            safe_reports = False
            break

    return safe_reports


if TESTING:
    puzzle_data = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_SAFE = 0

for line in puzzle_data:
    line = [int(x) for x in line.strip().split()]
    if sorted(line) == line or sorted(line, reverse=True) == line:
        if DEBUG:
            print("line", line, "is sorted")

        if is_safe(line):
            if DEBUG:
                print("line", line, "is safe")
            TOTAL_SAFE += 1
    else:
        if DEBUG:
            print("line", line, "is not sorted")
        continue

ANSWER = TOTAL_SAFE

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
