"""
John McDonough
    github - movinalot
    Advent of Code 2021
"""

TESTING = 1
DEBUG = 1
DAY = "03"
YEAR = "2021"
PART = "2"
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

O2_GENERATOR = ""
CO2_SCRUBBER = ""

def find_value(value_list, zero_or_one, position_x, o2_or_co2):
    """ Find values with O or 1 in Position X """

    new_list = []
    count_1s = 0
    count_0s = 0

    for count, value in enumerate(value_list):

        if value[position_x] == zero_or_one:
            new_list.append(value)

            if position_x + 1 < len(value):
                if value[position_x] == "1":


for count, value in enumerate(puzzle_data):

    COUNT_1S = 0
    COUNT_0S = 0
    for binary_number_pos, binary_number_val in enumerate(value):
        if binary_number_val == "1":
            COUNT_1S += 1
        else:
            COUNT_0S += 1

    if DEBUG:
        print(COUNT_1S, COUNT_0S)


ANSWER = 0

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)


22 59  7 10  6
33 36 96 55 23
13 85 18 29 28
75 46 83 73 58
34 40 87 56 98

b1r1 = 000000
b1r2 = 000000