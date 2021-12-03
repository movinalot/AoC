"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name
import copy

TESTING = 1
DEBUG = 0
DAY = "08"
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
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
    ]
else:
    PUZZLE_DATA = process_puzzle_input()

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

EXECUTIONS = {}
POSITION = 0
ACCUMULATOR = 0
CHANGED_INDEX = None

INSTRUCTIONS = copy.deepcopy(PUZZLE_DATA)
while True:

    if POSITION in EXECUTIONS.keys():
        print("LOOPING - BREAKING")
        if DEBUG:
            print(POSITION)
        break
    if INSTRUCTIONS[POSITION].split()[0] == 'nop':
        EXECUTIONS[POSITION] = 'exe'
        if DEBUG:
            print(
                'INSTRUCTION:', INSTRUCTIONS[POSITION],
                'CUR POSITION:', POSITION,
                'ACC:', ACCUMULATOR
            )
        POSITION += 1
        continue
    if INSTRUCTIONS[POSITION].split()[0] == 'acc':
        ACCUMULATOR += int(INSTRUCTIONS[POSITION].split()[1])
        EXECUTIONS[POSITION] = 'exe'
        if DEBUG:
            print(
                'INSTRUCTION:', INSTRUCTIONS[POSITION],
                'CUR POSITION:', POSITION,
                'ACC:', ACCUMULATOR
            )
        POSITION += 1
        continue
    if INSTRUCTIONS[POSITION].split()[0] == 'jmp':
        EXECUTIONS[POSITION] = 'exe'
        if DEBUG:
            print(
                'INSTRUCTION:', INSTRUCTIONS[POSITION],
                'CUR POSITION:', POSITION,
                'ACC:', ACCUMULATOR
            )
        POSITION += int(INSTRUCTIONS[POSITION].split()[1])
        continue

ANSWER = ACCUMULATOR

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
