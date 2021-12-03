"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name, global-statement

TESTING = 1
TESTFILE = 0
DEBUG = 0
DAY = "07"
YEAR = "2020"
PART = "2"
ANSWER = None
PUZZLE_DATA = None
BAG_RULES = {}
CONTAINED_BAGS_COUNT = 0

def count_contained_bags(bag_to_find, parent_bag_count):
    """ Count all the bags that can be contained in the bag to find """
    global CONTAINED_BAGS_COUNT
 
    print('entering the function bag:',bag_to_find, parent_bag_count)
    for rule in BAG_RULES[bag_to_find]:
        if rule != "no_other_bags" and not "no_other_bags" in BAG_RULES[rule].keys() :
            CONTAINED_BAGS_COUNT += int(BAG_RULES[bag_to_find][rule])
            print(BAG_RULES[bag_to_find][rule])

    for rule in BAG_RULES[bag_to_find]:
        print('rule:',rule, BAG_RULES[bag_to_find][rule])
        CONTAINED_BAGS_COUNT += int(BAG_RULES[bag_to_find][rule]) * parent_bag_count
        if rule != 'no_other_bags':
            print('next rule:',BAG_RULES[rule], 'Parent bag count:', parent_bag_count )
            count_contained_bags(rule, int(BAG_RULES[bag_to_find][rule]))


def process_puzzle_input(ext=".txt"):
    """ Process puzzle input """
    with open("puzzle_data_" + DAY + "_" + YEAR + ext) as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())
    return puzzle_data

if TESTING:
    if TESTFILE:
        PUZZLE_DATA = process_puzzle_input("_test.txt")
    else:
        PUZZLE_DATA = [
            'light red bags contain 1 bright white bag, 2 muted yellow bags.',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
            'bright white bags contain 1 shiny gold bag.',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
            'faded blue bags contain no other bags.',
            'dotted black bags contain no other bags.'
        ]
else:
    PUZZLE_DATA = process_puzzle_input()

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

ANSWER = 0
BAG_RULES = {}

for bag_rule in PUZZLE_DATA:
    bag_color = bag_rule.split()[0] + '_' + bag_rule.split()[1]
    if not bag_color in BAG_RULES.keys():
        if bag_rule.split('contain')[1].strip() == 'no other bags.':
            BAG_RULES[bag_color] = {'no_other_bags':0}
        else:
            bag_types = {}
            for _ in bag_rule.split('contain')[1].split(','):
                bag_types[_.split()[1]+'_'+_.split()[2]] = _.split()[0]

            BAG_RULES[bag_color] = bag_types

count_contained_bags('shiny_gold',0)
print(CONTAINED_BAGS_COUNT)
ANSWER = 0

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
