"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

from itertools import product

TESTING = 0
DEBUG = 0
DAY = "07"
YEAR = "2024"
PART = "2"
ANSWER = None


def check_calibrations(calibration_data, product_set):
    """ "Check Calibrations"""

    target_value = int(calibration_data.split(": ", maxsplit=1)[0])
    operand_values = [int(x) for x in calibration_data.split(": ")[1].split()]
    operator_values = list(product(product_set, repeat=len(operand_values) - 1))

    if DEBUG:
        print("starting with: ", target_value, operand_values, operator_values)

    for ops in operator_values:
        if DEBUG:
            print("ops", ops)
        current_value = operand_values[0]
        for i, op in enumerate(ops):

            if DEBUG:
                print(current_value, op, operand_values[i + 1])

            if op == "|":
                current_value = int(str(current_value) + str(operand_values[i + 1]))
            elif op == "+":
                current_value += operand_values[i + 1]
            elif op == "*":
                current_value *= operand_values[i + 1]

        if current_value == target_value:
            if DEBUG:
                print(current_value)
            return current_value
    return None


if TESTING:
    puzzle_data = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_CALIBRATION = 0

for line in puzzle_data:

    if DEBUG:
        print(line)

    calibration = check_calibrations(line, "+*")
    if calibration is not None:
        TOTAL_CALIBRATION += calibration
    else:
        calibration = check_calibrations(line, "+*|")
        if calibration is not None:
            TOTAL_CALIBRATION += calibration

ANSWER = TOTAL_CALIBRATION

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
