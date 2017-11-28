# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "03"
year = "2015"
part = "2"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    #puzzle_data = "^v"
    #puzzle_data = "^>v<"
    puzzle_data = "^v^v^v^v^v"

if debug:
    print(puzzle_data)
    
real_santa_houses = {}
robo_santa_houses = {}

real_x = 0
real_y = 0
robo_x = 0
robo_y = 0

def update_present_count_real_santa(x, y):
    
    if (x,y) in real_santa_houses:
        real_santa_houses[(x,y)] += 1
    else:
        real_santa_houses[(x,y)] = 1

    if debug:
        print('real: (',x,',',y,'):', real_santa_houses[(x,y)])

def update_present_count_robo_santa(x, y):
    
    if (x,y) in robo_santa_houses:
        robo_santa_houses[(x,y)] += 1
    else:
        robo_santa_houses[(x,y)] = 1

    if debug:
        print('robo: (',x,',',y,'):', robo_santa_houses[(x,y)])
        
update_present_count_real_santa(real_x, real_y)
update_present_count_robo_santa(robo_x, robo_y)

for direction in range(0, len(puzzle_data)):

    if direction % 2:
        real = True
        robo = False
    else:
        real = False
        robo = True
        
    if debug:
        print(puzzle_data[direction])
        print("real: ", real, "robo: ", robo)

    if real:
        if puzzle_data[direction] == '^':
            real_y = real_y + 1               
        elif puzzle_data[direction] == '>':
            real_x = real_x + 1
        elif puzzle_data[direction] == 'v':
            real_y = real_y - 1
        elif puzzle_data[direction] == '<':
            real_x = real_x - 1

        update_present_count_real_santa(real_x, real_y)

    else:
        if puzzle_data[direction] == '^':
            robo_y = robo_y + 1               
        elif puzzle_data[direction] == '>':
            robo_x = robo_x + 1
        elif puzzle_data[direction] == 'v':
            robo_y = robo_y - 1
        elif puzzle_data[direction] == '<':
            robo_x = robo_x - 1

        update_present_count_robo_santa(robo_x, robo_y)

all_houses = { **real_santa_houses, **robo_santa_houses }
answer = len(all_houses.keys())
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
