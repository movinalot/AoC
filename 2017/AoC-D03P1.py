# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "03"
year = "2017"
part = "1"
answer = None
    
if testing:
    puzzle_data = 36
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.read()
        puzzle_data = int(puzzle_data)

if debug:
    print(puzzle_data)

points = {}
x = 0
y = 0

# Get started
points[(x,y)] = 1
direction = 'e'

for num in range(2,puzzle_data+1):

    if debug:
        print("start",direction, x, y, num-1)
        
    if direction == 'e':
        if (x+1,y) in points:
            y -= 1
        else:
            x += 1
            direction = 'n'
    elif direction == 'w':
        if (x-1,y) in points:
            y += 1
        else:
            x -= 1
            direction = 's'
    elif direction == 'n':
        if (x,y+1) in points:
            x += 1
        else:
            y += 1
            direction = 'w'
    elif direction == 's':
        if (x,y-1) in points:
            x -= 1
        else:
            y -= 1
            direction = 'e'

    points[(x,y)] = num

    if debug:
        print("stop ",direction, x, y, num)

if debug:
    print(points)

answer = abs(0-x) + abs(0-y)
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
