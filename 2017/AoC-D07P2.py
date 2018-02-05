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
        weight   = line.split('->')[0].split(' ')[1].strip()
        weight   = int(weight[1:weight.find(')')])

    # Put the program in the programs dict
    if program in programs:
        programs[(program)]["count"] += 1
        programs[(program)]["sub_pro"] = list(sub_pros)
        programs[(program)]["weight"] = weight
    else:
        programs[(program)] = {"weight":weight,
                               "sub_pro":list(sub_pros),
                               "count":1,
                               "total_weight":0}

    # Put the sub_programs in the programs dict
    for sub_pro in sub_pros:
        if sub_pro in programs:
            programs[(sub_pro)]["count"] += 1
        else:
            programs[(sub_pro)] = {"weight":weight,
                                   "sub_pro":[],
                                   "count":1,
                                   "total_weight":0}
    if debug:
        print("program",program,"line",line,"sub_pros",sub_pros)

if debug:
    print(programs)

same_weight = None
diff_weight = None

for key, value in programs.items():
    if debug:
        print(key, value)
    if value["count"] != 1 and len(value["sub_pro"]) > 0:
        if debug:
            print("found", key, programs[key])
        for sub_pro in programs[key]["sub_pro"]:
            programs[key]["total_weight"] += int(programs[sub_pro]["weight"])

        programs[key]["total_weight"] += int(programs[key]["weight"])

        #if same_weight == None:
        #    same_weight = programs[key]["total_weight"]
        #elif same_weight != programs[key]["total_weight"]:
        #    diff_weight = programs[key]["total_weight"]
        #    print("found", key, programs[key])
        #else:
        #    same_weight = programs[key]["total_weight"]
if debug:
    print(programs)

print(same_weight, diff_weight)
       
answer = None
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
