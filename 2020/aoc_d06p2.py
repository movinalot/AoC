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
PART = "2"
ANSWER = None
PUZZLE_DATA = None

def process_puzzle_input(ext=".txt"):
    """ Process puzzle input """
    with open("puzzle_data_" + DAY + "_" + YEAR + ext) as f:
        puzzle_data = []
        group = []
        person = []
        for line in f:
            if len(line.strip()) > 0:
                for x in line.strip():
                    person.append(x)
                group.append(person)
                person = []
            else:
                puzzle_data.append(group)
                group = []
        puzzle_data.append(group)


    return puzzle_data

if TESTING:
    if TESTFILE:
        PUZZLE_DATA = process_puzzle_input("_test.txt")
    else:
        PUZZLE_DATA = [
            [
                ['a', 'b', 'c']
            ],
            [
                ['a'],
                ['b'],
                ['c']
            ],
            [
                ['a', 'b'],
                ['a', 'c']
            ],
            [
                ['a'],
                ['a'],
                ['a'],
                ['a']
            ],
            [
                ['b']
            ]
        ]
else:
    PUZZLE_DATA = process_puzzle_input()

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

ANSWER = 0

for group in PUZZLE_DATA:
    ANSWER += len(set.intersection(*[set(person) for person in group]))

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
