"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2022"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [ 
        "A Y",
        "B X",
        "C Z"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

total_score = 0

# "A X" = 3
# "A Y" = 4
# "A Z" = 8

# "B X" = 1
# "B Y" = 5
# "B Z" = 9

# "C X" = 2
# "C Y" = 6
# "C Z" = 7

for game in puzzle_data:
    
    if game == "A X":
        total_score += 3
    
    if game == "A Y":
        total_score += 4

    if game == "A Z":
        total_score += 8

    if game == "B X":
        total_score += 1
    
    if game == "B Y":
        total_score += 5

    if game == "B Z":
        total_score += 9

    if game == "C X":
        total_score += 2
    
    if game == "C Y":
        total_score += 6

    if game == "C Z":
        total_score += 7

ANSWER = total_score

print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
