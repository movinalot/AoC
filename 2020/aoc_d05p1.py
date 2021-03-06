"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name

TESTING = 0
DEBUG = 0
DAY = "05"
YEAR = "2020"
PART = "1"
ANSWER = None
PUZZLE_DATA = None

def process_puzzle_input(ext=".txt"):
    """ Process puzzle input """
    puzzle_data = []
    with open("puzzle_data_" + DAY + "_" + YEAR + ext) as f:
        for line in f:
            puzzle_data.append(line.strip())
    return puzzle_data

if TESTING:
    PUZZLE_DATA = [
        'FBFBBFFRLR',
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL'
    ]
else:
    PUZZLE_DATA = process_puzzle_input()

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

ANSWER = 0
SEAT_ID = 0

for bp in PUZZLE_DATA:
    bp = bp.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    row = '0b'+bp[0:7]
    col = '0b'+bp[-3:]

    if int(row,2)*8+int(col,2) > SEAT_ID:
        SEAT_ID = int(row,2)*8+int(col,2)

    if DEBUG:
        print(int(row,2), int(col,2), int(row,2)*8+int(col,2))

ANSWER = SEAT_ID

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
