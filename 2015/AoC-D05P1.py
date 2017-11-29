# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "05"
year = "2015"
part = "1"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    puzzle_data = ["ugknbfddgicrmopn",
                   "aaa",
                   "jchzalrnumimnmhp",
                   "haegwjzuvuyypxyu",
                   "dvszwmarrgswjxmb"]

if debug:
    print(len(puzzle_data))

if not testing:
    puzzle_data = puzzle_data.splitlines()

def contains_vowels(input_str):
    vowel_count = 0

    for vowel in ['a','e','i','o','u']:
        vowel_count += input_str.count(vowel)
    if debug:
        print("vc:",vowel_count)
    return vowel_count

def contains_2chars(input_str):
    for x in range(0,len(input_str)):
        if input_str.count(input_str[x] + input_str[x]) >= 1:
            if debug:
                print("double char: ",input_str[x] + input_str[x])
            return True
    return False

def contains_badseq(input_str):

    for badseq in ['ab','cd','pq','xy']:
        if input_str.count(badseq) >= 1:
            if debug:
                print(badseq, input_str.count(badseq))
            return True
    return False

number_of_nice_strings = 0

for santa_string in puzzle_data:

    if not contains_2chars(santa_string):
        if debug:
            print("Naughty string: ", santa_string)
        continue
    
    if contains_badseq(santa_string):
        if debug:
            print("Naughty string: ", santa_string)
        continue
    
    if (contains_vowels(santa_string)) <= 2:
        if debug:
            print("Naughty string: ", santa_string)
        continue

    if debug:
        print("Nice string: ", santa_string)

    number_of_nice_strings = number_of_nice_strings + 1

answer = number_of_nice_strings
print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
