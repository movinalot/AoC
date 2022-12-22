"""
John McDonough
    github - movinalot
    Advent of Code 2022
"""

TESTING = 0
DEBUG = 0
DAY = "07"
YEAR = "2022"
PART = "2"
ANSWER = None

if TESTING:
    puzzle_data = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

DIR_TREE = {}
DIR_TRAVERSAL_LIST = []

for line in puzzle_data:
    if line == "$ cd /":
        DIR_TREE["root"] = 0
        DIR_TRAVERSAL_LIST.append("root")
        if DEBUG:
            print("at root")
            print(DIR_TRAVERSAL_LIST)
        continue
    if line.startswith("$"):
        if line == "$ ls":
            IN_LISTING = True
            if DEBUG:
                print("in listing dir", DIR_TRAVERSAL_LIST[-1])
            continue
        if line.startswith("$ cd"):
            IN_LISTING = False
            if line == "$ cd ..":
                DIR_TRAVERSAL_LIST.pop()
                if DEBUG:
                    print("change up dir")
                    print(DIR_TRAVERSAL_LIST)
                continue
            DIR_TRAVERSAL_LIST.append(
                DIR_TRAVERSAL_LIST[-1]+"-"+line.split(" ")[2])
            if DIR_TRAVERSAL_LIST[-1] not in DIR_TREE:
                DIR_TREE[DIR_TRAVERSAL_LIST[-1]] = 0

            if DEBUG:
                print("change to dir", line.split(" ")[2])
                print(DIR_TRAVERSAL_LIST)
            continue
    if line.startswith("dir"):
        continue

    if DEBUG:
        print(
            "file",
            line.split(" ", maxsplit=1)[1],
            "size",
            line.split(" ", maxsplit=1)[0]
        )
        print(DIR_TRAVERSAL_LIST)
        print(DIR_TREE)

    for i in DIR_TRAVERSAL_LIST:
        add_size = int(line.split(" ", maxsplit=1)[0])
        DIR_TREE[i] += add_size
        if DEBUG:
            print("adding ", add_size, "to dir", i)

SMALLEST = 30000000
for _ in DIR_TREE.values():
    if 70000000 - DIR_TREE['root'] + _ > 30000000:
        if _ < SMALLEST:
            SMALLEST = _
            if DEBUG:
                print("SMALLEST", SMALLEST)

ANSWER = SMALLEST
print(
    "AoC Day: " + DAY + " Year: " + YEAR +
    " part " + PART + ", answer:", ANSWER
)
