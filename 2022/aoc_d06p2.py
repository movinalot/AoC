"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""
from collections import Counter

TESTING = 0
DEBUG = 0
DAY = "06"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",     # first marker after character 19
        "bvwbjplbgvbhsrlpgdmjqwftvncz",       # first marker after character 23
        "nppdvjthqldpwncqszvftbrmjlhg",       # first marker after character 23
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",  # first marker after character 29
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"    # first marker after character 26
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

START_OF_MESSAGE_MARKER = 0
DISTINCT_CHARACTERS = 14

for line in puzzle_data:

    for i in range(len(line)):
        chunk = line[i:i+DISTINCT_CHARACTERS]
        count = Counter(chunk)
        NO_REPEATS = True

        if DEBUG:
            print(chunk, count)

        for key, value in count.items():
            if value > 1:
                NO_REPEATS = False
                break

        if NO_REPEATS:
            START_OF_MESSAGE_MARKER = i + DISTINCT_CHARACTERS
            if DEBUG:
                print("no repeats", START_OF_MESSAGE_MARKER)
            break

ANSWER = START_OF_MESSAGE_MARKER
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
