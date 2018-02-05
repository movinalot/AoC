# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 1
day = "09"
year = "2017"
part = "1"
answer = None
    
if testing:
    puzzle_data = [3,4,1,5]
    cycle = list(range(5))
    
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.read()
    puzzle_data = puzzle_data.split(',')
    cycle = list(range(256))

if debug:
    print("Data Len:",len(puzzle_data))
    print(cycle)


skip_size = 0
start_idx = 0
for number in puzzle_data:
    print(number)
    length = int(number)

    if length > len(cycle):
        continue
    else:
        
        tmp_list = []
        
        for x in range(length):
            if start_idx + x < len(cycle):
                tmp_list.append(cycle[start_idx + x])
            else:
                tmp_list.append(cycle[(start_idx + x) % len(cycle)])
        print(tmp_list)
        tmp_list.reverse()
        print(tmp_list)
        for x in range(length):
            if start_idx + x < len(cycle):
                cycle[start_idx + x] = tmp_list[x]
            else:
                cycle[(start_idx + x) % len(cycle)] = tmp_list[x]
        print(cycle)
        

        if start_idx + length + skip_size < len(cycle):
            start_idx = start_idx + length + skip_size
        else:
            start_idx = (start_idx + length + skip_size) % len(cycle)

        print("start index",start_idx, "skip size",skip_size)

        skip_size += 1
        
    
answer = cycle[0]*cycle[1]
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
