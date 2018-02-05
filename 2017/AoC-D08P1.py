# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "08"
year = "2017"
part = "1"
answer = None
    
if testing:
    puzzle_data = ["b inc 5 if a > 1",
                   "a inc 1 if b < 5",
                   "c dec -10 if a >= 1",
                   "c inc -20 if c == 10"]
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print("Data Len:",len(puzzle_data))

registers = {}
for line in puzzle_data:

    perform_op = False
    
    register = line.split(' ')[0].strip()
    reg_opr  = line.split(' ')[1].strip()
    opr_val  = int(line.split(' ')[2].strip())
    exp_reg  = line.split(' ')[4].strip()
    exp_opr  = line.split(' ')[5].strip()
    exp_val  = int(line.split(' ')[6].strip())

    if debug:
        print(register,reg_opr,opr_val,exp_reg,exp_opr,exp_val)
        
    if register not in registers:
        registers[register] = 0
    if exp_reg not in registers:
        registers[exp_reg] = 0

    if exp_opr == "<":
        if registers[exp_reg] < exp_val:
            perform_op = True
    elif exp_opr == ">":
        if registers[exp_reg] > exp_val:
            perform_op = True
    elif exp_opr == ">=":
        if registers[exp_reg] >= exp_val:
            perform_op = True
    elif exp_opr == "<=":
        if registers[exp_reg] <= exp_val:
            perform_op = True
    elif exp_opr == "==":
        if registers[exp_reg] == exp_val:
            perform_op = True
    elif exp_opr == "!=":
        if registers[exp_reg] != exp_val:
            perform_op = True
        
    if perform_op:
        if reg_opr == "inc":
            registers[register] += opr_val
        elif reg_opr == "dec":
            registers[register] -= opr_val

if debug:
    print(registers)
    
max_value = 0
for key, value in registers.items():
    if value > max_value:
        max_value = value
        
answer = max_value
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
