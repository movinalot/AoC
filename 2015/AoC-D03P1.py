# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "03"
year = "2015"
part = "1"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    puzzle_data = ">"
    #puzzle_data = "^>v<"
    #puzzle_data = "^v^v^v^v^v"

if debug:
    print(puzzle_data)
    
houses = {}
x = 0
y = 0

def update_present_count(x, y):
    
    if (x,y) in houses:
        houses[(x,y)] += 1
    else:
        houses[(x,y)] = 1

    if debug:
        print('(',x,',',y,'):',houses[(x,y)])
    
update_present_count(x, y)

for direction in range(0, len(puzzle_data)):

    if debug:
        print(puzzle_data[direction])

    if puzzle_data[direction] == '^':
        y = y + 1               
    elif puzzle_data[direction] == '>':
        x = x + 1
    elif puzzle_data[direction] == 'v':
        y = y - 1
    elif puzzle_data[direction] == '<':
        x = x - 1

    update_present_count(x, y)

answer = len(houses.keys())
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
