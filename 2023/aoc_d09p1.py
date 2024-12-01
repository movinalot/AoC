"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 1
DEBUG = 1
DAY = "09"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append([int(number) for number in str(line).split()])

if DEBUG:
    print(len(puzzle_data), puzzle_data)

for row, line in enumerate(puzzle_data):
    READING_HISTORY = []
    READING_HISTORY.append(line)
    READING_DIFF_SUM = -1
    
    while READING_DIFF_SUM != 0:
        for reading_num in range(1,len(line)):
            READING_DIFF = line[reading_num]-line[reading_num-1]
            print(line[reading_num]-line[reading_num-1], end=" ")



EXTRAPOLATION_TOTAL = 0

ANSWER = EXTRAPOLATION_TOTAL

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
