"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

import re

TESTING = 0
DEBUG = 0
DAY = "03"
YEAR = "2024"
PART = "2"
ANSWER = None

def use_regex(input_text):
    """ Find all regex in input_text """

    pattern = re.compile(r"mul\(\d*,\d*\)|do\(\)|don't\(\)", re.IGNORECASE)
    return pattern.findall(input_text)

if TESTING:
    puzzle_data = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

SUM_MUL_OPS= 0
DO_SUMS = True

for line in puzzle_data:
    matches = use_regex(line)
    if DEBUG:
        print(matches)
    for match in matches:
        if "do()" in match:
            DO_SUMS = True
        elif "don't()" in match:
            DO_SUMS = False
        elif "mul" in match and DO_SUMS:
            op1, op2 = match.split("(")[1].split(")")[0].split(",")
            SUM_MUL_OPS += int(op1) * int(op2)

ANSWER = SUM_MUL_OPS

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
