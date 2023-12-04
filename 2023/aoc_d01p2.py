"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2023"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

CALIBRATION_SUM = 0
WORD_NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in puzzle_data:
    CALIBRATION = line.strip()
    # Get first and last number, either a word or a digit combine and sum
    WORDS = []
    WORDS_LEFT = [
        (CALIBRATION.find(word), WORD_NUMS.index(word) + 1)
        for word in WORD_NUMS
        if CALIBRATION.find(word) != -1
    ]
    WORDS_RIGHT = [
        (CALIBRATION.rfind(word), WORD_NUMS.index(word) + 1)
        for word in WORD_NUMS
        if CALIBRATION.rfind(word) != -1
    ]

    WORDS = WORDS_LEFT + WORDS_RIGHT

    NUM_POS = 0
    for num in line:
        if num.isdigit():
            WORDS.append((NUM_POS, int(num)))
        NUM_POS += 1

    WORDS.sort()
    CALIBRATION_SUM += int(str(WORDS[0][1]) + str(WORDS[-1][1]))

ANSWER = CALIBRATION_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
