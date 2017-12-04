# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "04"
year = "2017"
part = "1"
answer = None
    
if testing:
    puzzle_data = ["aa bb cc dd ee",
                   "aa bb cc dd aa",
                   "aa bb cc dd aaa"]
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print(len(puzzle_data))

import collections
invalid_phrases = 0

for line in puzzle_data:

    str_values = line.strip().split(' ')

    tmp = [item for item, count in collections.Counter(str_values).items() if count > 1]

    if debug:
        print(str_values, tmp, len(tmp))
        
    if len(tmp) > 0:
        invalid_phrases += 1
        
answer = len(puzzle_data) - invalid_phrases
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
