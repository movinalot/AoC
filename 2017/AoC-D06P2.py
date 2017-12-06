# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "06"
year = "2017"
part = "2"
answer = None
    
if testing:
    puzzle_data = "0\t2\t7\t0"
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.read()

if debug:
    print("Data Len:",len(puzzle_data))

mem_bank = [int(i) for i in puzzle_data.strip().split('\t')]
if debug:
    print(mem_bank)

import operator

mem_banks_seen_before = {}
distribution_cycles = 0

mem_banks_seen_before[(distribution_cycles)] = list(mem_bank)
if debug:
    print(mem_banks_seen_before)

seen_before = False
while not seen_before:
    # Find first largest value
    lrg_mem_blk_index, lrg_mem_blk_value = max(enumerate(mem_bank), key=operator.itemgetter(1))

    if debug:
        print(lrg_mem_blk_index, lrg_mem_blk_value)
        
    # clear and distribute the block
    mem_bank[lrg_mem_blk_index] = 0
    for x in range(0,lrg_mem_blk_value):

        if lrg_mem_blk_index + 1 == len(mem_bank):
            lrg_mem_blk_index = 0
        else:
            lrg_mem_blk_index += 1
            
        mem_bank[lrg_mem_blk_index] += 1

        if debug:
            print(mem_bank)

    # keep track of what has been seen
    distribution_cycles += 1
    mem_banks_seen_before[(distribution_cycles)] = list(mem_bank)

    # has this configuration been seen before and
    # what distribution cycle was it first seen
    distribution_cycle = 0 
    for distribution_cycle in range(0,distribution_cycles):
        if debug:
            print("seen before:",mem_banks_seen_before[(distribution_cycle)],"mem_bank",mem_bank)

        if mem_banks_seen_before[(distribution_cycle)] == mem_bank:
            seen_before = True
            break
        distribution_cycle += 1

    if debug:
        print(mem_bank,distribution_cycles,mem_banks_seen_before)

    if seen_before == True:
        break
   
answer = distribution_cycles - distribution_cycle
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
