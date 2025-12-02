"""
John McDonough
    github - movinalot
    Advent of Code 2025
"""

# pylint: disable=line-too-long

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2025"
PART = "2"
ANSWER = None

def find_patterns(the_id):
    """ Find the patterns in the current ID """

    curr_id_factors = []
    find_patterns_result = 0

    if DEBUG:
        print(f"The factors of the length of {len(str(the_id))} are:")
    for i in range(1, len(str(the_id)) + 1):
        if len(str(the_id)) % i == 0:
            curr_id_factors.append(i)

    if DEBUG:
        print (f"Checking ID: {the_id} with factors: {curr_id_factors}")

    for factor in curr_id_factors[:-1]:
        curr_id_line = str(the_id)

        curr_id_factor_segments = [curr_id_line[i:i+factor] for i in range(0, len(curr_id_line), factor)]

        if DEBUG:
            print(f"  segments for factor {factor}: {curr_id_factor_segments}")

        if len(set(curr_id_factor_segments)) == 1:
            find_patterns_result = the_id
            break

    return find_patterns_result

if TESTING:
    puzzle_data = [
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

SILLY_ID_SUM = 0

for id_sequence in puzzle_data[0].split(","):
    if DEBUG:
        print(id_sequence)
    RANGE_PARTS = id_sequence.split("-")
    START = int(RANGE_PARTS[0])
    END = int(RANGE_PARTS[1])

    for curr_id in range(START, END + 1):
        if DEBUG:
            print(curr_id, len(str(curr_id)))

        result = find_patterns(curr_id)
        if result:
            SILLY_ID_SUM += result
            if DEBUG:
                print(f"Found matching ID: {result}")

ANSWER = SILLY_ID_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
