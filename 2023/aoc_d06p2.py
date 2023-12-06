"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "06"
YEAR = "2023"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "Time:       71530",
        "Distance:  940200",
    ]
else:
    puzzle_data = [
        "Time:              61677571",
        "Distance:   430103613071150",
    ]

if DEBUG:
    print(len(puzzle_data), puzzle_data)

MARGIN_OF_ERROR = 0
WINS = 1

TIMES = puzzle_data[0].split()
DISTANCES = puzzle_data[1].split()

for j in range(1, len(TIMES)):
    WINS_CNT = 0
    for i in range(int(TIMES[j])):
        if i * (int(TIMES[j]) - i) > int(DISTANCES[j]):
            WINS_CNT += 1

    WINS *= WINS_CNT

ANSWER = WINS

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
