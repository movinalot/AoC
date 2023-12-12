"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "08"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "RL",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            if line.strip() != "":
                puzzle_data.append(line.strip())

DIRECTIONS = {}
CURR_LOC = "AAA"
NEW_LOC = None
STEPS = 0

for n, line in enumerate(puzzle_data):
    if n == 0:
        pass
    else:
        DIRECTIONS[line.split("=")[0].strip()] = (
            line.split("=")[1].strip().replace(")", "").replace("(", "")
        )

if DEBUG:
    print(len(puzzle_data), puzzle_data)

LEFT_RIGHT = list(puzzle_data[0])
CURR_DIR = 0

while True:
    if CURR_LOC == "ZZZ":
        break

    DIRECTION = LEFT_RIGHT[CURR_DIR]
    if CURR_DIR < len(LEFT_RIGHT) - 1:
        CURR_DIR += 1
    else:
        CURR_DIR = 0

    if DIRECTION == "R":
        NEW_LOC = DIRECTIONS[CURR_LOC].split(",")[1].strip()
    elif DIRECTION == "L":
        NEW_LOC = DIRECTIONS[CURR_LOC].split(",")[0].strip()

    STEPS += 1
    CURR_LOC = NEW_LOC

ANSWER = STEPS

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
