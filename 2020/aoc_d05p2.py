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
PART = "2"
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
SEAT_IDS = []

for bp in PUZZLE_DATA:
    row = '0b'
    col = '0b'
    for x in bp[0:7]:

        if x == 'F':
            row += '0'
        else:
            row += '1'
    for x in bp[-3:]:
        if x == 'L':
            col += '0'
        else:
            col += '1'

    SEAT_IDS.append(int(row,2)*8+int(col,2))

    if DEBUG:
        print(int(row,2), int(col,2), int(row,2)*8+int(col,2))

SEAT_IDS.sort()
for x in range(0,len(SEAT_IDS)-2):
    if SEAT_IDS[x+1] - SEAT_IDS[x] == 2:
        ANSWER = SEAT_IDS[x] + 1
        break

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
