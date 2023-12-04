"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "03"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

SCHEMATIC = []
PN_SUM = 0

if DEBUG:
    print(len(puzzle_data), puzzle_data)

for line in puzzle_data:
    SCHEMATIC.append(line.strip())

LINE_NUM = 0
for line in SCHEMATIC:
    NEW_LINE = ""
    for char in line:
        if char.isdigit():
            NEW_LINE = NEW_LINE + char
        else:
            NEW_LINE = NEW_LINE + "."
    NUMS = [number for number in NEW_LINE.split(".") if number.isdigit()]

    if len(NUMS) > 0:
        TOP_CHARS = ""
        BOT_CHARS = ""
        LEFT_CHAR = ""
        RIGHT_CHAR = ""
        ALL_CHARS = ""
        WORKING_LINE = SCHEMATIC[LINE_NUM]

        if DEBUG:
            print("Nums", NUMS)

        for number in NUMS:
            PN_LOC = WORKING_LINE.find(number)
            PN_LEN = len(number)

            tmp_line = WORKING_LINE.replace(number, "." * PN_LEN, 1)
            WORKING_LINE = tmp_line

            TOP_LINE = LINE_NUM - 1
            BOT_LINE = LINE_NUM + 1
            LEFT_POS = PN_LOC - 1
            RIGHT_POS = PN_LOC + PN_LEN

            if DEBUG:
                print(
                    "NUM:",
                    number,
                    "TOP_LINE:",
                    TOP_LINE,
                    "BOT_LINE:",
                    BOT_LINE,
                    "LEFT_POS:",
                    LEFT_POS,
                    "RIGHT_POS:",
                    RIGHT_POS,
                )

            if LEFT_POS < 0:
                LEFT_POS = 0
            else:
                LEFT_CHAR = SCHEMATIC[LINE_NUM][LEFT_POS]

            if RIGHT_POS > len(SCHEMATIC[LINE_NUM]) - 1:
                RIGHT_POS = len(SCHEMATIC[LINE_NUM])
            else:
                RIGHT_CHAR = SCHEMATIC[LINE_NUM][RIGHT_POS]

            if TOP_LINE >= 0:
                TOP_CHARS = SCHEMATIC[TOP_LINE][LEFT_POS : RIGHT_POS + 1]
            if BOT_LINE < len(SCHEMATIC):
                BOT_CHARS = SCHEMATIC[BOT_LINE][LEFT_POS : RIGHT_POS + 1]

            ALL_CHARS = TOP_CHARS + BOT_CHARS + LEFT_CHAR + RIGHT_CHAR

            if DEBUG:
                print("TOP_CHARS:", TOP_CHARS)
                print("LEFT_CHAR:", LEFT_CHAR, RIGHT_CHAR, ":RIGHT_CHAR")
                print("BOT_CHARS:", BOT_CHARS)
                print("ALL_CHARS:", ALL_CHARS)

            for char in ALL_CHARS:
                if char != "." and not char.isdigit():
                    if DEBUG:
                        print("ajacent to char:", char, "number:", number)
                    PN_SUM += int(number)
                    break
    LINE_NUM += 1

ANSWER = PN_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
