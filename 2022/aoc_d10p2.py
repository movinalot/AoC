"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "10"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "addx 15",
        "addx -11",
        "addx 6",
        "addx -3",
        "addx 5",
        "addx -1",
        "addx -8",
        "addx 13",
        "addx 4",
        "noop",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx 5",
        "addx -1",
        "addx -35",
        "addx 1",
        "addx 24",
        "addx -19",
        "addx 1",
        "addx 16",
        "addx -11",
        "noop",
        "noop",
        "addx 21",
        "addx -15",
        "noop",
        "noop",
        "addx -3",
        "addx 9",
        "addx 1",
        "addx -3",
        "addx 8",
        "addx 1",
        "addx 5",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx -36",
        "noop",
        "addx 1",
        "addx 7",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "addx 6",
        "noop",
        "noop",
        "noop",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx 7",
        "addx 1",
        "noop",
        "addx -13",
        "addx 13",
        "addx 7",
        "noop",
        "addx 1",
        "addx -33",
        "noop",
        "noop",
        "noop",
        "addx 2",
        "noop",
        "noop",
        "noop",
        "addx 8",
        "noop",
        "addx -1",
        "addx 2",
        "addx 1",
        "noop",
        "addx 17",
        "addx -9",
        "addx 1",
        "addx 1",
        "addx -3",
        "addx 11",
        "noop",
        "noop",
        "addx 1",
        "noop",
        "addx 1",
        "noop",
        "noop",
        "addx -13",
        "addx -19",
        "addx 1",
        "addx 3",
        "addx 26",
        "addx -30",
        "addx 12",
        "addx -1",
        "addx 3",
        "addx 1",
        "noop",
        "noop",
        "noop",
        "addx -9",
        "addx 18",
        "addx 1",
        "addx 2",
        "noop",
        "noop",
        "addx 9",
        "noop",
        "noop",
        "noop",
        "addx -1",
        "addx 2",
        "addx -37",
        "addx 1",
        "addx 3",
        "noop",
        "addx 15",
        "addx -21",
        "addx 22",
        "addx -6",
        "addx 1",
        "noop",
        "addx 2",
        "addx 1",
        "noop",
        "addx -10",
        "noop",
        "noop",
        "addx 20",
        "addx 1",
        "addx 2",
        "addx 2",
        "addx -6",
        "addx -11",
        "noop",
        "noop",
        "noop"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

REGISTER_X = 1
CYCLES = 0
CRT_DISPLAY = []
CRT_ROWS = 6
CRT_COLS = 40
CRT_ROW = 0

for i in range(CRT_ROWS):
    CRT_DISPLAY.append([])
    for j in range(CRT_COLS):
        CRT_DISPLAY[i].append(".")

for line in puzzle_data:
    if line.startswith("noop"):
        if CYCLES in (REGISTER_X-1, REGISTER_X, REGISTER_X+1):
            CRT_DISPLAY[CRT_ROW][CYCLES] = "#"
        CYCLES += 1

        if CYCLES in (40, 80, 120, 160, 200):
            CRT_ROW += 1
            CYCLES = 0
        continue

    for i in range(2):
        if CYCLES in (REGISTER_X-1, REGISTER_X, REGISTER_X+1):
            CRT_DISPLAY[CRT_ROW][CYCLES] = "#"
        CYCLES += 1

        if CYCLES in (40, 80, 120, 160, 200):
            CRT_ROW += 1
            CYCLES = 0

    REGISTER_X += int(line.split(" ")[1])

ANSWER = CRT_DISPLAY
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:"
)

for i in range(CRT_ROWS):
    for j in range(CRT_COLS):
        print(CRT_DISPLAY[i][j], end="")
    print()
