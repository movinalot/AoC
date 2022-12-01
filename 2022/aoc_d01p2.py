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


def Nmaxelements(list_in, N):
    final_list = []

    for i in range(0, N):
        max_element = 0

        for j in range(len(list_in)):
            if list_in[j] > max_element:
                max_element = list_in[j]

        list_in.remove(max_element)
        final_list.append(max_element)

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
total_elf_calories = 0

for elf_calories in puzzle_data:

    # Add elf total when newline encountered
    if elf_calories == "\n":
        ELF_CALORIES.append(total_elf_calories)
        total_elf_calories = 0
    else:
        total_elf_calories += int(elf_calories)

# Get the last elf total
ELF_CALORIES.append(total_elf_calories)

ANSWER = sum(Nmaxelements(ELF_CALORIES, 3))

print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
