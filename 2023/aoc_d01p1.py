"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

CALIBRATION_SUM = 0

for calibration in puzzle_data:
    # Get first and last number, combine and sum

    nums = [int(x) for x in calibration if x.isdigit()]
    if nums:
        CALIBRATION_SUM += int(str(nums[0]) + str(nums[-1]))

ANSWER = CALIBRATION_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
