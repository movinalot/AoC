"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""
import re
import string

TESTING = 0
DEBUG = 0
DAY = "05"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        "1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

DATA_STACKS = []
INSTRUCTIONS = []

for line in puzzle_data:
    if line.startswith("move"):
        INSTRUCTIONS.append(line)
        continue
    if len(line) == 0:
        continue
    DATA_STACKS.append(line)

NUM_STACKS = len(re.split(r'\s+', DATA_STACKS[-1].strip()))

if DEBUG:
    print(INSTRUCTIONS)
    print(DATA_STACKS)
    print(NUM_STACKS)

CONTAINER_STACKS = []

for _ in range(NUM_STACKS):
    CONTAINER_STACKS.append([])

for stack in DATA_STACKS[:-1]:

    if DEBUG:
        print(stack)

    for stack_num, conatiner_pos in enumerate(range(1, len(stack), 4)):

        if stack[conatiner_pos] in string.ascii_uppercase:
            if DEBUG:
                print(stack[conatiner_pos], stack_num)

            CONTAINER_STACKS[stack_num].append(stack[conatiner_pos])

for count, container_stack in enumerate(CONTAINER_STACKS):
    if DEBUG:
        print(container_stack)

    container_stack.reverse()

    if DEBUG:
        print(container_stack)

if DEBUG:
    print(CONTAINER_STACKS)

for instruction in INSTRUCTIONS:
    num_items = int(instruction.split(" ")[1])
    from_stack = int(instruction.split(" ")[3])
    to_stack = int(instruction.split(" ")[5])

    items = CONTAINER_STACKS[from_stack-1][-num_items:]
    del CONTAINER_STACKS[from_stack-1][-num_items:]
    for item in items:
        CONTAINER_STACKS[to_stack-1].append(item)

    if DEBUG:
        print(CONTAINER_STACKS)

if DEBUG:
    print(CONTAINER_STACKS)

TOP_ITEMS = ""

for container_stack in CONTAINER_STACKS:
    TOP_ITEMS += container_stack[-1]

ANSWER = TOP_ITEMS
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
