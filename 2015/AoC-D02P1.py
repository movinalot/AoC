# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "02"
year = "2015"
part = "1"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    puzzle_data = "2x3x4\n"\
                  "1x1x10\n"

if debug:
    print(puzzle_data)

puzzle_data = puzzle_data.splitlines()

wrapping_paper = 0

for dimensions in puzzle_data:
    sides = dimensions.split('x')
    sq_feet_sides = [int(sides[0])* int(sides[1]),
                     int(sides[0])* int(sides[2]),
                     int(sides[1])* int(sides[2])]
    sq_feet_sides.sort()

    for sq_feet_side in sq_feet_sides:
        wrapping_paper += sq_feet_side * 2

    wrapping_paper += sq_feet_sides[0]

    if debug:
        print(sq_feet_sides, wrapping_paper)
        
answer = wrapping_paper
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
