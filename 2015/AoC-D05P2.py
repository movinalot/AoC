# John McDonough
# github - movinalot
# Advent of Code 2015

testing = 0
debug = 0
day = "05"
year = "2015"
part = "2"
answer = None

with open("puzzle_data_" + day + "_" + year + ".txt") as f:
    puzzle_data = f.read()
    
if testing:
    puzzle_data = ["qjhvhtzxzqqjkmpb",
                   "aaa","xxyxx","abcdefeghigh",
                   "uurcxstgmygtbstg",
                   "ieodomkazucvgmuy"]

if debug:
    print(len(puzzle_data))

if not testing:
    puzzle_data = puzzle_data.splitlines()

import re

answer = sum(
      1 for s in puzzle_data
      if len(re.findall(r"([a-z]{2}).*\1", s))
      and re.findall(r"([a-z]).\1", s)
)

print("AoC Day: " + day + " Year: " + year + " part " + part + ", this is the answer:", answer)
