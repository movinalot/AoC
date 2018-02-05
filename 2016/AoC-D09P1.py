# John McDonough
# github - movinalot
# Advent of Code 2016

testing = 1
debug = 1
day = "01"
year = "2016"
part = "1"
answer = None
    
if testing:
    puzzle_data = "ADVENT"
    puzzle_data = "A(1x5)BC"
    puzzle_data = "(3x3)XYZ"
    puzzle_data = "A(2x2)BCD(2x2)EFG"
    puzzle_data = "(6x2)(1x3)AB"
    #puzzle_data = "X(8x2)(3x3)ABCY"

else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print puzzle_data

file_length = 0
marker_found = False
x = 0
file_str = ''
print len(puzzle_data)
while True:
    if debug:
        print x, puzzle_data[x]
        
    if puzzle_data[x] == '(' and marker_found == False:
        marker = ''
        marker_found = True 
        while True:
            x += 1
            if puzzle_data[x] == ')':
                break
            else:
                marker += puzzle_data[x]
        print marker
        x += 1

        data_len = int(marker.split('x')[0])
        data_rep = int(marker.split('x')[1])

        data_str = puzzle_data[x:x+data_len]
        for i in range(data_rep):
            file_str += data_str

        x += data_len
        print file_str,x
    else:
        file_str += puzzle_data[x]

    if x < len(puzzle_data):
        x += 1
    else:
        break
print file_str
answer = file_length
print "AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer
