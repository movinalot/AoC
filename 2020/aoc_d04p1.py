"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name

TESTING = 1
TESTFILE = 0
DEBUG = 0
DAY = "04"
YEAR = "2020"
PART = "1"
ANSWER = None
PUZZLE_DATA = None

def process_puzzle_input(ext=".txt"):
    """ Process puzzle input """
    with open("puzzle_data_" + DAY + "_" + YEAR + ext) as f:
        puzzle_data = []
        passport_fields = {}
        for line in f:
            fields = line.split()
            if len(fields) > 0:
                for x in line.split():
                    key = x.split(':')[0]
                    val = x.split(':')[1]
                    passport_fields[key] = val
            else:
                puzzle_data.append(passport_fields)
                passport_fields = {}
        puzzle_data.append(passport_fields) # add the last block of passport data to the list
    return puzzle_data

if TESTING:
    if TESTFILE:
        PUZZLE_DATA = process_puzzle_input("_test.txt")
    else:
        PUZZLE_DATA = [
            {
                'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd',
                'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'
            },
            {
                'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884',
                'hcl': '#cfa07d', 'byr': '1929'
            },
            {
                'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108',
                'byr': '1931', 'hgt': '179cm'
            },
            {
                'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011',
                'ecl': 'brn', 'hgt': '59in'
            }
        ]
else:
    PUZZLE_DATA = process_puzzle_input()

REQ_FIELDS = {
    'byr': '(Birth Year)',
    'iyr': '(Issue Year)',
    'eyr': '(Expiration Year)',
    'hgt': '(Height)',
    'hcl': '(Hair Color)',
    'ecl': '(Eye Color)',
    'pid': '(Passport ID)'
}

REQ_KEYS = REQ_FIELDS.keys()

OPT_FIELDS = {
    'cid':'(Country ID)'
}

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

ANSWER = 0
for passport in PUZZLE_DATA:

    if passport.keys() >= REQ_KEYS:
        ANSWER += 1

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
