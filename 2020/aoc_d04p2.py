"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name, too-many-boolean-expressions
import re

TESTING = 0
TESTFILE = 0
DEBUG = 0
DAY = "04"
YEAR = "2020"
PART = "2"
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

def year_check(year, b_year, e_year):
    """ Check year is correct length and falls in range """

    return len(year) == 4 and (int(year) >= b_year and int(year) <= e_year)

if TESTING:
    if TESTFILE:
        PUZZLE_DATA = process_puzzle_input("_test_part" + PART + ".txt")
    else:
        PUZZLE_DATA = [
            {
                'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb',
                'hgt': '170', 'pid': '186cm', 'iyr': '2018', 'byr': '1926'
            },
            {
                'iyr': '2019', 'hcl': '#602927', 'eyr': '1967', 'hgt': '170cm',
                'ecl': 'grn', 'pid': '012533040', 'byr': '1946'
            },
            {
                'hcl': 'dab227', 'iyr': '2012', 'ecl': 'brn', 'hgt': '182cm',
                'pid': '021572410', 'eyr': '2020', 'byr': '1992', 'cid': '277'
            },
            {
                'hgt': '59cm', 'ecl': 'zzz', 'eyr': '2038', 'hcl': '74454a',
                'iyr': '2023', 'pid': '3556412378', 'byr': '2007'
            },
            {
                'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012',
                'eyr': '2030', 'byr': '1980', 'hcl': '#623a2f'
            },
            {
                'eyr': '2029', 'ecl': 'blu', 'cid': '129', 'byr': '1989', 'iyr': '2014',
                'pid': '896056539', 'hcl': '#a97842', 'hgt': '165cm'
            },
            {
                'hcl': '#888785', 'hgt': '164cm', 'byr': '2001', 'iyr': '2015',
                'cid': '88', 'pid': '545766238', 'ecl': 'hzl', 'eyr': '2022'
            },
            {
                'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu',
                'byr': '1944', 'eyr': '2021', 'pid': '093154719'
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
        if not year_check(passport['byr'], 1920, 2002):
            continue
        if not year_check(passport['iyr'], 2010, 2020):
            continue
        if not year_check(passport['eyr'], 2020, 2030):
            continue

        if not passport['ecl'] in 'amb' 'blu' 'brn' 'gry' 'grn' 'hzl' 'oth':
            continue

        if not (len(passport['pid']) == 9 and passport['pid'].isnumeric()):
            continue

        if passport['hgt'].endswith('in') or passport['hgt'].endswith('cm'):
            if passport['hgt'].endswith('in'):
                if not 59 <= int(passport['hgt'][:-2]) <= 76:
                    continue

            if passport['hgt'].endswith('cm'):
                if not 150 <= int(passport['hgt'][:-2]) <= 193:
                    continue
        else:
            continue

        if len(passport['hcl']) == 7:
            pattern = re.compile('#{1}[0-9a-f]{6}')
            if not pattern.match(passport['hcl']):
                continue
        else:
            continue

        # if you get here the passport is valid
        ANSWER += 1

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
