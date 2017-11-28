# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "01"
year = "2015"
part = "2"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()

if testing:
    puzzle_data = "()())"

if debug:
    print(len(puzzle_data))
    
bldg_floor = 0

for x in range(0, len(puzzle_data)):

    if debug:
        print(puzzle_data[x])

    if puzzle_data[x] == '(':
        bldg_floor = bldg_floor + 1
    else:
        bldg_floor = bldg_floor - 1
        
    if bldg_floor == -1:
        answer = x + 1
        break
    
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
