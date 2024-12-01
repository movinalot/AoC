"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 1
DAY = "05"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

SEEDS = []
CURRENT_MAP = None
MAPS = {}

for puzzle_line in puzzle_data:
    line = puzzle_line.strip()
    if line == "":
        continue

    if line.startswith("seeds:"):
        print(line)
        SEEDS = [int(x) for x in line.split(":")[1].split()]
        continue

    if line.endswith("map:"):
        CURRENT_MAP = line.split()[0]
        MAPS[CURRENT_MAP] = []
        continue

    MAPS[CURRENT_MAP].append([int(x) for x in line.split()])
    continue

if DEBUG:
    print(SEEDS)
    print(MAPS)

ANSWER = None

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
