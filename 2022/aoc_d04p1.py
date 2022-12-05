"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "04"
YEAR = "2022"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_FULL_CONTAIN = 0

for sections in puzzle_data:
    sections_elf1 = list(
        range(
            int(sections.split(",", maxsplit=1)[0].split("-", maxsplit=1)[0]),
            int(sections.split(",", maxsplit=1)[0].split("-", maxsplit=1)[1])+1
        )
    )
    sections_elf2 = list(
        range(
            int(sections.split(",", maxsplit=1)[1].split("-", maxsplit=1)[0]),
            int(sections.split(",", maxsplit=1)[1].split("-", maxsplit=1)[1])+1
        )
    )

    if DEBUG:
        print(sections_elf1, sections_elf2)

    if set(sections_elf1).issubset(sections_elf2):
        TOTAL_FULL_CONTAIN += 1
        continue
    if set(sections_elf2).issubset(sections_elf1):
        TOTAL_FULL_CONTAIN += 1


ANSWER = TOTAL_FULL_CONTAIN
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
