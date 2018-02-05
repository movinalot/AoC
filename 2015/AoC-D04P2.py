# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "04"
year = "2015"
part = "2"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    puzzle_data = "abcdef"

if debug:
    print(len(puzzle_data))

import hashlib
x = 0

while True:

    md5_input = puzzle_data.encode() + str(x).encode()
    md5_hash = hashlib.md5(md5_input).hexdigest()

    if md5_hash.startswith("000000"):
        if debug:
            print(x, md5_hash)
        break

    x = x + 1

answer = x
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
