"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "A Y",
        "B X",
        "C Z"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_SCORE = 0

# "A X" = 3
# "A Y" = 4
# "A Z" = 8

# "B X" = 1
# "B Y" = 5
# "B Z" = 9

# "C X" = 2
# "C Y" = 6
# "C Z" = 7

for game in puzzle_data:

    if game == "A X":
        TOTAL_SCORE += 3

    if game == "A Y":
        TOTAL_SCORE += 4

    if game == "A Z":
        TOTAL_SCORE += 8

    if game == "B X":
        TOTAL_SCORE += 1

    if game == "B Y":
        TOTAL_SCORE += 5

    if game == "B Z":
        TOTAL_SCORE += 9

    if game == "C X":
        TOTAL_SCORE += 2

    if game == "C Y":
        TOTAL_SCORE += 6

    if game == "C Z":
        TOTAL_SCORE += 7

ANSWER = TOTAL_SCORE

print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
