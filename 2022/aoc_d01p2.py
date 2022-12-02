"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "01"
YEAR = "2022"
PART = "2"
ANSWER = None


def num_max_elements(list_in, num_elements):
    """ Return N number of Max Elements """

    final_list = []

    for _ in range(0, num_elements):
        max_element = max(list_in)
        final_list.append(max_element)
        list_in.remove(max_element)

    return final_list


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

ANSWER = sum(num_max_elements(ELF_CALORIES, 3))

print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
