# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 1
debug = 1
day = "07"
year = "2017"
part = "2"
answer = None
    
if testing:
    puzzle_data = ["pbga (66)",
                   "xhth (57)",
                   "ebii (61)",
                   "havc (66)",
                   "ktlj (57)",
                   "fwft (72) -> ktlj, cntj, xhth",
                   "qoyq (66)",
                   "padx (45) -> pbga, havc, qoyq",
                   "tknk (41) -> ugml, padx, fwft",
                   "jptl (61)",
                   "ugml (68) -> gyxo, ebii, jptl",
                   "gyxo (61)",
                   "cntj (57)"]
else:
    with open("puzzle_data_" + day + "_" + year + ".txt") as f:
        puzzle_data = f.readlines()

if debug:
    print("Data Len:",len(puzzle_data))

def populate_programs(program, sub_pros):
    if program not in programs:
        programs[(program)] = {"weight":weight,"sub_pros":list(sub_pros),"count":1,
                               "total_weight":0}
    elif program in programs and len(sub_pros) > 0 and len(programs[(program)]["sub_pros"]) == 0:
        programs[(program)]["sub_pros"] = list(sub_pros)
    else:
        programs[(program)]["count"] += 1
    
programs = {}
for line in puzzle_data:

    sub_pros = []
    if line.find('->') > 0:
        program  = line.split('->')[0].split(' ')[0].strip()
        weight   = line.split('->')[0].split(' ')[1].strip()
        weight   = int(weight[1:weight.find(')')])
        tmp = line.split('->')[1]
        sub_pros = [x.strip() for x in tmp.split(',')]

    else:
        program = line.split(' ')[0].strip()
        weight  = line.split(' ')[1].strip()
        weight  = int(weight[1:weight.find(')')])

    # Put the program in the programs dict
    populate_programs(program, list(sub_pros))

    # Put the sub_programs in the programs dict
    for sub_pro in sub_pros:
        populate_programs(sub_pro, list([]))
        
    if debug:
        print("program",program,"line",line,"sub_pros",sub_pros)

print(programs)
#for key, value in programs.items():
#    if value["count"] != 1 and len(value["sub_pros"]) > 0:
#        print("found", key, programs[key])
#        for sub_pro in programs[key]["sub_pros"]:
#            programs[key]["total_weight"] += programs[sub_pro]["weight"]
#print(programs)
answer = None
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
