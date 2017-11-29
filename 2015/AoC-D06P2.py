# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "06"
year = "2015"
part = "1"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.readlines()
    
if testing:
    puzzle_data = ["turn on 0,0 through 2,2"]
                   #"toggle 0,0 through 999,0",
                   #"turn off 499,499 through 500,500"]

if debug:
    print(len(puzzle_data))

#if not testing:
#    puzzle_data = puzzle_data.splitlines()

lights = {}
for x in range(1000):
    for y in range(1000):
        lights[(x,y)] = 0

for line in puzzle_data:
    line_tokens = line.split(' ')

    if debug:
        print(line_tokens)

    if line_tokens[0] == "turn":
        operator = line_tokens[0] + "-" + line_tokens[1]
        start_point = line_tokens[2]
        start_x = int(line_tokens[2].split(',')[0])
        start_y = int(line_tokens[2].split(',')[1])
        end_point = line_tokens[4]
        end_x = int(line_tokens[4].split(',')[0])
        end_y = int(line_tokens[4].split(',')[1])
    else:
        operator = line_tokens[0]
        start_point = line_tokens[1]
        start_x = int(line_tokens[1].split(',')[0])
        start_y = int(line_tokens[1].split(',')[1])
        end_point = line_tokens[3]
        end_x = int(line_tokens[3].split(',')[0])
        end_y = int(line_tokens[3].split(',')[1])

    if debug:
        print("operator:    ", operator)
        print("start_point: ", start_point)
        print("start_x:     ", start_x)
        print("end_x:       ", end_x)
        print("end_point:   ", end_point)
        print("start_y:     ", start_y)
        print("end_y:       ", end_y)

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):

            if operator == "turn-on":
                lights[(x,y)] += 1
                if debug:
                    print("turning on:  ",x, "," ,y)
            if operator == "turn-off":
                if lights[(x,y)] - 1 <= 0:
                    lights[(x,y)] = 0
                else:
                    lights[(x,y)] -= 1
                if debug:
                    print("turning off: ",x, "," ,y)
            if operator == "toggle":
                lights[(x,y)] += 2
                if debug:
                    print("turning off: ",x, "," ,y)

lights_on_brightness = 0
for x in range(1000):
    for y in range(1000):
        lights_on_brightness += lights[(x,y)]
            
answer = lights_on_brightness
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
