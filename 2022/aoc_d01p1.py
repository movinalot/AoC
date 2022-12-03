"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2022"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "1000", "2000", "3000", "\n", "4000", "\n",
        "5000", "6000", "\n", "7000", "8000", "9000", "\n", "10000"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

ELF_CALORIES = []
TOTAL_ELF_CALORIES = 0

for elf_calories in puzzle_data:

    # Add elf total when newline encountered
    if elf_calories == "\n":
        ELF_CALORIES.append(TOTAL_ELF_CALORIES)
        TOTAL_ELF_CALORIES = 0
    else:
        TOTAL_ELF_CALORIES += int(elf_calories)

# Get the last elf total
ELF_CALORIES.append(TOTAL_ELF_CALORIES)

max_value = max(ELF_CALORIES)
max_index = ELF_CALORIES.index(max_value) + 1

if DEBUG:
    print(f"Max Value: {max_value}")
    print(f"Max Index: {max_index}")
    print(ELF_CALORIES)

ANSWER = max_value

print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
