"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

# pylint: disable=line-too-long

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2025"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

SILLY_ID_SUM = 0

for id_sequence in puzzle_data[0].split(","):
    if DEBUG:
        print(id_sequence)
    RANGE_PARTS = id_sequence.split("-")
    START = int(RANGE_PARTS[0])
    END = int(RANGE_PARTS[1])

    for curr_id in range(START, END + 1):
        if DEBUG:
            print(curr_id, len(str(curr_id)))

        if len(str(curr_id)) % 2 == 0:
            MIDPOINT = int(len(str(curr_id)) / 2)
            FIRST_HALF = str(curr_id)[:MIDPOINT]
            SECOND_HALF = str(curr_id)[MIDPOINT:]
            if FIRST_HALF == SECOND_HALF:
                if DEBUG:
                    print(f"Found matching ID: {curr_id}")
                SILLY_ID_SUM += curr_id


ANSWER = SILLY_ID_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
