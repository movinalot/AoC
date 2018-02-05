# John McDonough
# github - movinalot
# Advent of Code 2017

testing = 0
debug = 0
day = "07"
year = "2017"
part = "1"
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
        tmp = line.split('->')[1]
        sub_pros = [x.strip() for x in tmp.split(',')]

    else:
        program = line.split(' ')[0].strip()
        weight  = line.split(' ')[1].strip()

    # Put the program in the programs dict
    if program not in programs:
        programs[(program)] = {"weight":weight,"sub_pro":list(sub_pros),"count":1}
    else:
        programs[(program)]["count"] += 1

    # Put the sub_programs in the programs dict
    for sub_pro in sub_pros:
        if sub_pro not in programs:
            programs[(sub_pro)] = {"weight":weight,"sub_pro":list(sub_pros),"count":1}
        else:
            programs[(sub_pro)]["count"] += 1
        
    if debug:
        print("program",program,"line",line,"sub_pros",sub_pros)

if debug:
    print(programs)
for key, value in programs.items():
    if value["count"] == 1:
        answer = key

print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
