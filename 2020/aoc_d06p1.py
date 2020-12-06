"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name

TESTING = 0
TESTFILE = 0
DEBUG = 0
DAY = "06"
YEAR = "2020"
PART = "1"
ANSWER = None
PUZZLE_DATA = None

def process_puzzle_input(ext=".txt"):
    """ Process puzzle input """
    with open("puzzle_data_" + DAY + "_" + YEAR + ext) as f:
        puzzle_data = []
        fields = []
        for line in f:
            if len(line.strip()) > 0:
                for x in line.strip():
                    fields.append(x)
            else:
                puzzle_data.append(fields)
                fields = []
        puzzle_data.append(fields) # add the last block of data to the list
    return puzzle_data

if TESTING:
    if TESTFILE:
        PUZZLE_DATA = process_puzzle_input("_test.txt")
    else:
        PUZZLE_DATA = [
            ['a','b','c'],
            ['a','b','c'],
            ['a','b','a','c'],
            ['a','a','a','a'],
            ['b']
        ]
else:
    PUZZLE_DATA = process_puzzle_input()

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

ANSWER = 0

for answer_list in PUZZLE_DATA:
    ANSWER += len(set(answer_list))

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
