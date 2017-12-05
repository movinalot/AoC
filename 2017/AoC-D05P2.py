# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "05"
year = "2017"
part = "2"
answer = None
    
if testing:
    puzzle_data = ["0",
                   "3",
                   "0",
                   "1",
                   "-3"]
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print("Data Len:",len(puzzle_data))


exit_steps = 0
x = 0
maze = {}

for line in puzzle_data:

    x += 1
    steps = int(line)
    maze[(x)] = steps
    
    if debug:
        print("Key:", x,"Steps: ", steps)

current_loc = 1
next_loc = None

if debug:
    print(maze)
    
while True:

    if (current_loc) not in maze:
        break

    exit_steps += 1
    
    if debug:
        print("Before - Key:", current_loc, "Value:", maze[(current_loc)], "next_loc:", next_loc)

    next_loc = maze[(current_loc)] + current_loc

    if maze[(current_loc)] >= 3:
        maze[(current_loc)] -= 1
    else:
        maze[(current_loc)] += 1

    if debug:
        print("After  - Key:", current_loc, "Value:", maze[(current_loc)], "next_loc:", next_loc)
        print(maze, "\n")
        
    current_loc = next_loc
    
if debug:
    print(maze)
    
answer = exit_steps
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
