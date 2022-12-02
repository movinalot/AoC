"""
John McDonough
    github - movinalot
    Advent of Code 2021
"""

TESTING = 0
DEBUG = 0
DAY = "03"
YEAR = "2021"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

COUNT_1 = [0] * len(puzzle_data[0])
COUNT_0 = [0] * len(puzzle_data[0])

GAMMA = ""
EPSILON = ""

for count, value in enumerate(puzzle_data):

    for binary_number_pos, binary_number_val in enumerate(value):
        if binary_number_val == "1":
            COUNT_1[binary_number_pos] += 1
        else:
            COUNT_0[binary_number_pos] += 1

if DEBUG:
    print(COUNT_1, COUNT_0)

for binary_number in enumerate(COUNT_1):

    if COUNT_1[binary_number[0]] > COUNT_0[binary_number[0]]:
        GAMMA = GAMMA + "1"
        EPSILON = EPSILON + "0"
    else:
        GAMMA = GAMMA + "0"
        EPSILON = EPSILON + "1"

if DEBUG:
    print(GAMMA, EPSILON)
    print(int(GAMMA, 2), int(EPSILON, 2))

ANSWER = int(GAMMA, 2) * int(EPSILON, 2)

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
