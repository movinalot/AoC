# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "02"
year = "2017"
part = "1"
answer = None
    
if testing:
    puzzle_data = ["5\t1\t9\t5\n",
                   "7\t5\t3\n",
                   "2\t4\t6\t8\n"]
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print(len(puzzle_data))

checksum = 0
for line in puzzle_data:

    int_values = [int(i) for i in line.strip().split('\t')]
    int_values.sort()
    
    high_low_diff = int_values[len(int_values)-1] - int_values[0]

    if debug:
        print(int_values, len(int_values), high_low_diff)

    checksum += high_low_diff
        
answer = checksum
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
