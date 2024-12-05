"""
John McDonough
    github - movinalot
    Advent of Code 2024
"""

TESTING = 0
DEBUG = 0
DAY = "05"
YEAR = "2024"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

PAGE_RULES = []
PAGE_UPDATES = []

SUM_MIDDLE = 0

for line in puzzle_data:
    if line == "":
        continue

    if line.find("|") > 0:
        PAGE_RULES.append(
            (int(line.split("|", maxsplit=1)[0]), int(line.split("|", maxsplit=1)[1]))
        )
    else:
        PAGE_UPDATES.append([int(x) for x in line.split(",")])

if DEBUG:
    print(PAGE_RULES, PAGE_UPDATES)

for i, update in enumerate(PAGE_UPDATES):
    for j, page in enumerate(update):
        if j < len(update) - 1:
            if DEBUG:
                print("Page pair: ", update[j], update[j + 1])
            if (update[j], update[j + 1]) in PAGE_RULES:
                if DEBUG:
                    print("Found rule: ", update[j], update[j + 1])
            else:
                if DEBUG:
                    print("No found rule: ", update[j], update[j + 1])
                break
        else:
            SUM_MIDDLE += update[int((len(update) - 1) / 2)]
            if DEBUG:
                print("Middle page: ", update[int((len(update) - 1) / 2)])


ANSWER = SUM_MIDDLE

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
