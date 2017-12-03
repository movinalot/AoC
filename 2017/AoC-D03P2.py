# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "03"
year = "2017"
part = "2"
answer = None
    
if testing:
    puzzle_data = 12
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.read()
        puzzle_data = int(puzzle_data)

if debug:
    print(puzzle_data)

def adjacent_sum(x,y):
    adjacent_cell_sum = 0

    """ Only previously created
        will be in dict points
    (x-1,y+1)(x+0,y+1)(x+1,y+1)
    (x-1,y+0)(x+0,y+0)(x+1,y+0)
    (x-1,y-1)(x+0,y-1)(x+1,y-1)
    """

    # above
    if (x-1,y+1) in points:
        adjacent_cell_sum += points[(x-1,y+1)]
    if (x+0,y+1) in points:
        adjacent_cell_sum += points[(x+0,y+1)]
    if (x+1,y+1) in points:
        adjacent_cell_sum += points[(x+1,y+1)]

    # sides
    if (x-1,y+0) in points:
        adjacent_cell_sum += points[(x-1,y+0)]
    if (x+1,y+0) in points:
        adjacent_cell_sum += points[(x+1,y+0)]

    # below
    if (x-1,y-1) in points:
        adjacent_cell_sum += points[(x-1,y-1)]
    if (x+0,y-1) in points:
        adjacent_cell_sum += points[(x+0,y-1)]
    if (x+1,y-1) in points:
        adjacent_cell_sum += points[(x+1,y-1)]

    return adjacent_cell_sum
    
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

    points[(x,y)] = adjacent_sum(x,y)

    if points[(x,y)] > puzzle_data:
        break

    if debug:
        print("stop ",direction, x, y, num)

if debug:
    print(points)

answer = points[(x,y)]
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
