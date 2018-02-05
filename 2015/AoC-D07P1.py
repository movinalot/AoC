# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 1
debug = 0
day = "07"
year = "2015"
part = "1"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.readlines()
    
if testing:
    puzzle_data = ["123 -> x",
                   "456 -> y",
                   "c -> l",
                   "x AND y -> d",
                   "x OR y -> e",
                   "x LSHIFT 2 -> f",
                   "y RSHIFT 2 -> g",
                   "NOT x -> h",
                   "NOT y -> i"]

if debug:
    print(len(puzzle_data))

wires = {}

for line in puzzle_data:
    line_tokens1 = line.split('->')
    line_tokens2 = line_tokens1[0].split(' ')

    # Assignment
    if len(line_tokens2) == 2:
        wire = line_tokens1[1].strip()
        value = line_tokens2[0].strip()
        print("assignment:", line)
        print ("0:",value,"1:",wire)
        if value.isnumeric():
            wires[wire] = int(value)
        else:
            wires[wire] = None
            wires[value] = None
        print(wires)
    # Operation
    elif len(line_tokens2) == 4:
        oper = line_tokens2[1].strip()
        wire1 = line_tokens2[0].strip()
        wire2 = line_tokens2[2].strip()
        value = line_tokens1[1].strip()
        print("operation:", line)
        print ("0:",wire1,"1:",oper,"2:",wire2,"3:",value)
        if (wire1 in wires or wire1.isnumeric()) and (wire2 in wires or wire2.isnumeric()):
            if oper == AND:
                if 
        
    # Negation
    elif len(line_tokens2) == 3:
        oper = line_tokens2[0].strip()
        wire = line_tokens2[1].strip()
        value = line_tokens1[1].strip()
        print("negation:", line)
        print ("0:",oper,"1:",wire,"2:",value)
        if wire in wires and wires[wire] != None:
            wires[value] = 65535 - wires[wire]
        else:
            wires[wire] = None
            wires[value] = None
        print(wires)
    else:
        print("don't know:", line)
        

            
answer = None
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
