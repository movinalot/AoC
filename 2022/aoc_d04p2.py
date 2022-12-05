"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "04"
YEAR = "2022"
PART = "2"
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

TOTAL_OVERLAP = 0

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

    common_sections = set(sections_elf1).intersection(set(sections_elf2))
    if len(common_sections):
        TOTAL_OVERLAP += 1

    if DEBUG:
        print(sections_elf1, sections_elf2)

ANSWER = TOTAL_OVERLAP
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
