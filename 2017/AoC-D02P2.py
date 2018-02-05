# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "02"
year = "2017"
part = "2"
answer = None
    
if testing:
    puzzle_data = ["5\t9\t2\t8\n",
                   "9\t4\t7\t3\n",
                   "3\t8\t6\t5\n"]
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print(len(puzzle_data))

checksum = 0
for line in puzzle_data:
    
    int_values = [int(i) for i in line.strip().split('\t')]
    int_values.sort(reverse=True)

    if debug:
        print(int_values, len(int_values))

    for x in range(0,len(int_values)-1):
        for y in range(x+1,len(int_values)):
            if int_values[x]%int_values[y] == 0:
                checksum += int_values[x]/int_values[y]           

answer = int(checksum)
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
