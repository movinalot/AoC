"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2025"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

dial_list = list(range(100))
dial_list_length = len(dial_list)

CURR_INDEX = 50
PASSWORD = 0

for line in puzzle_data:
    if DEBUG:
        print(line)
    DIRECTION = line[0]
    CLICKS = int(line[1:])
    NEW_INDEX = 0
    ROTATIONS = 0

    if DIRECTION == "L":
        NEW_INDEX = (CURR_INDEX - CLICKS) % dial_list_length
        if (CURR_INDEX - CLICKS) < 0:
            ROTATIONS  = int(abs((CURR_INDEX - CLICKS) / dial_list_length)) + 1
            if CURR_INDEX == 0:
                ROTATIONS -= 1
            if NEW_INDEX == 0:
                ROTATIONS -= 1
            if DEBUG:
                print(NEW_INDEX,CURR_INDEX, CLICKS, CURR_INDEX - CLICKS)
                print("passing 0: backwards ", ROTATIONS, "times")
    else:       # direction == "R"
        NEW_INDEX = (CURR_INDEX + CLICKS) % dial_list_length
        if (CURR_INDEX + CLICKS) > dial_list_length:
            ROTATIONS = int(abs((CURR_INDEX + CLICKS) / dial_list_length))
            if CURR_INDEX == 0 and CLICKS < dial_list_length:
                ROTATIONS -= 1
            if NEW_INDEX == 0:
                ROTATIONS -= 1
            if DEBUG:
                print(NEW_INDEX, CURR_INDEX, CLICKS, CURR_INDEX + CLICKS)
                print("passing 0: forwards ", ROTATIONS, "times")

    CURR_INDEX = NEW_INDEX

    if CURR_INDEX == 0:
        PASSWORD += 1
        if DEBUG:
            print(f"CURR_INDEX == 0, PASSWORD incremented to: {PASSWORD}")
    PASSWORD += ROTATIONS

ANSWER = PASSWORD

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
