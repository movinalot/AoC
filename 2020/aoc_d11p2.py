"""
John McDonough
 github - movinalot
 Advent of Code 2020
"""
# pylint: disable=invalid-name

import collections
import copy

TESTING = 0
TESTINGFILE = 0
DEBUG = 0
DAY = "11"
YEAR = "2020"
PART = "2"
ANSWER = None
PUZZLE_DATA = None

def process_puzzle_input(ext=".txt"):
    """ Process puzzle input """
    puzzle_data = []
    with open("puzzle_data_" + DAY + "_" + YEAR + ext) as f:
        for line in f:
            puzzle_data.append([x for x in line.strip()])
    return puzzle_data

if TESTING:
    PUZZLE_DATA = [
        ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
        ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'],
        ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
        ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'],
        ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'],
        ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'],
        ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
        ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'],
        ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']
    ]
elif TESTINGFILE:
    PUZZLE_DATA = process_puzzle_input("_test.txt")
else:
    PUZZLE_DATA = process_puzzle_input()

if DEBUG:
    print(len(PUZZLE_DATA), PUZZLE_DATA)

CURRENT_AREA = copy.deepcopy(PUZZLE_DATA)
NEW_AREA = []
OCC_SEATS = 0

while True:
    for row_num, row in enumerate(CURRENT_AREA):
        seat_row = []
        for seat_num, seat in enumerate(row):
            if seat == '.':
                seat_row.append('.')
                continue

            if DEBUG:
                print(row_num,seat_num)

            t_left = (row_num - 1, seat_num - 1)
            t_center = (row_num - 1, seat_num)
            t_right = (row_num - 1, seat_num + 1)
            on_left = (row_num, seat_num - 1)
            on_right = (row_num, seat_num + 1)
            b_left = (row_num + 1, seat_num - 1)
            b_center = (row_num + 1, seat_num)
            b_right = (row_num + 1, seat_num + 1)

            seats = []
            if t_left[0] < 0 or t_left[1] < 0:
                #print(t_left, "no above left seat")
                pass
            else:
                seats.append(CURRENT_AREA[t_left[0]][t_left[1]])

            if t_center[0] < 0:
                #print(t_center, "no above seat")
                pass
            else:
                seats.append(CURRENT_AREA[t_center[0]][t_center[1]])

            if t_right[0] < 0 or t_right[1] > len(row) - 1:
                #print(t_right, "no above right seat")
                pass
            else:
                seats.append(CURRENT_AREA[t_right[0]][t_right[1]])

            if on_left[1] < 0:
                #print(on_left, "no left seat")
                pass
            else:
                seats.append(CURRENT_AREA[on_left[0]][on_left[1]])

            if on_right[1] > len(row) - 1:
                #print(on_right, "no right seat")
                pass
            else:
                seats.append(CURRENT_AREA[on_right[0]][on_right[1]])

            if b_left[0] > (len(CURRENT_AREA) - 1) or b_left[1] < 0:
                #print(b_left, "no below left seat")
                pass
            else:
                seats.append(CURRENT_AREA[b_left[0]][b_left[1]])

            if b_center[0] > (len(CURRENT_AREA) - 1):
                #print(b_center, "no below seat")
                pass
            else:
                seats.append(CURRENT_AREA[b_center[0]][b_center[1]])

            if b_right[0] > (len(CURRENT_AREA) - 1) or b_right[1] > len(row) - 1:
                #print(b_right, "no below right seat")
                pass
            else:
                seats.append(CURRENT_AREA[b_right[0]][b_right[1]])

            if DEBUG:
                print(seats)

            if seat == 'L' and not '#' in seats:
                seat_row.append('#')
            elif seat == '#' and seats.count('#') >= 5:
                seat_row.append('L')
            else:
                seat_row.append(seat)

        NEW_AREA.append(seat_row)
        if DEBUG:
            print(seat_row)

    SAME = True
    for the_row_num, the_row in enumerate(NEW_AREA):
        if collections.Counter(the_row) != collections.Counter(CURRENT_AREA[the_row_num]):
            SAME = False
            break

    if not SAME:
        CURRENT_AREA = copy.deepcopy(NEW_AREA)
        NEW_AREA =[]
    else:
        for _ in NEW_AREA:
            OCC_SEATS += _.count('#')
        ANSWER = OCC_SEATS
        break

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
