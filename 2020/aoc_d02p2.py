"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2020"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

ANSWER = 0
for x in puzzle_data:
    values = x.split()
    rule_letter = values[1][0]
    rule_digit_1 = int(values[0].split('-')[0])-1
    rule_digit_2 = int(values[0].split('-')[1])-1
    password = values[2]

    if rule_letter in (password[rule_digit_1], password[rule_digit_2]):
        if password[rule_digit_1] != password[rule_digit_2]:
            ANSWER = ANSWER + 1

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
