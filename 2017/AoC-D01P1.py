# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "01"
year = "2017"
part = "1"
answer = None
    
if testing:
    puzzle_data = "1122"
    puzzle_data = "1111"
    puzzle_data = "1234"
    #puzzle_data = "91212129"
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.read()

if debug:
    print(len(puzzle_data))

captcha_sum = 0

for x in range(0,len(puzzle_data)):
    if debug:
        print(puzzle_data[x])

    if x == len(puzzle_data) - 1:
        if puzzle_data[x] == puzzle_data[0]:
            captcha_sum += int(puzzle_data[x])

        break
    if puzzle_data[x] == puzzle_data[x+1]:
        captcha_sum += int(puzzle_data[x])
        
answer = captcha_sum
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
