# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "02"
year = "2015"
part = "2"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    puzzle_data = "2x3x4\n"\
                  "1x1x10\n"

if debug:
    print(puzzle_data)

puzzle_data = puzzle_data.splitlines()

ribbon_len = 0

for dimensions in puzzle_data:
    pkg_ribbon_len = 0
    sides_str = dimensions.split('x')
    sides_int = [int(sides_str[0]),
                 int(sides_str[1]),
                 int(sides_str[2])]
    sides_int.sort()

    pkg_ribbon_len += sides_int[0] + sides_int[0] + sides_int[1] + sides_int[1]
    pkg_ribbon_len += sides_int[0] * sides_int[1] * sides_int[2]

    ribbon_len += pkg_ribbon_len

    if debug:
        print(sides_int, pkg_ribbon_len, ribbon_len)

answer = ribbon_len
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
