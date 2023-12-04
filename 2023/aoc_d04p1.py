"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "04"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

POINTS_TOTAL = 0

for line in puzzle_data:
    CARD_DETAILS = {}
    CARD_DETAILS["card"] = line.split(":", maxsplit=1)[0].split(" ")[1].strip()
    CARD_DETAILS["winning_numbers"] = [
        int(num)
        for num in line.split(":")[1].split("|")[0].strip().split(" ")
        if num.isdigit()
    ]
    CARD_DETAILS["my_numbers"] = [
        int(num)
        for num in line.split(":")[1].split("|")[1].strip().split(" ")
        if num.isdigit()
    ]

    if DEBUG:
        print(CARD_DETAILS)

    WIN_COUNT = 0
    for num in CARD_DETAILS["winning_numbers"]:
        if num in CARD_DETAILS["my_numbers"]:
            WIN_COUNT += 1
    if WIN_COUNT > 0:
        POINTS_TOTAL += 2 ** (WIN_COUNT - 1)

ANSWER = POINTS_TOTAL

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
