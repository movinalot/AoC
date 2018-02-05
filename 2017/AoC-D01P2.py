# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "01"
year = "2017"
part = "2"
answer = None
    
if testing:
    #puzzle_data = "1212"
    #puzzle_data = "1221"
    #puzzle_data = "123425"
    #puzzle_data = "123123"
    puzzle_data = "12131415"

else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.read()

if debug:
    print(len(puzzle_data))

captcha_sum = 0

full_len = int(len(puzzle_data))
half_len = int((len(puzzle_data)/2))

if debug:
    print(full_len,half_len)

for x in range(0,len(puzzle_data)):
    if debug:
        print(puzzle_data[x])

    if x + half_len >= full_len:
        if debug:
            print(puzzle_data[x],puzzle_data[x-half_len],x,x-half_len)
        if puzzle_data[x] == puzzle_data[x-half_len]:
            captcha_sum += int(puzzle_data[x])

    if x + half_len < full_len:
        if debug:
            print(puzzle_data[x],puzzle_data[half_len+x],x,half_len+x)
        if puzzle_data[x] == puzzle_data[half_len+x]:
            captcha_sum += int(puzzle_data[x])
            
        
answer = captcha_sum
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
