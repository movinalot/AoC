from collections import deque

instructions = ["rect 1x1",
                "rotate row y=0 by 20",
                "rect 1x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 3",
                "rect 2x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 3",
                "rect 2x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 4",
                "rect 2x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 3",
                "rect 2x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 5",
                "rect 1x1",
                "rotate row y=0 by 2",
                "rect 1x1",
                "rotate row y=0 by 6",
                "rect 5x1",
                "rotate row y=0 by 2",
                "rect 1x3",
                "rotate row y=2 by 8",
                "rotate row y=0 by 8",
                "rotate column x=0 by 1",
                "rect 7x1",
                "rotate row y=2 by 24",
                "rotate row y=0 by 20",
                "rotate column x=5 by 1",
                "rotate column x=4 by 2",
                "rotate column x=2 by 2",
                "rotate column x=0 by 1",
                "rect 7x1",
                "rotate column x=34 by 2",
                "rotate column x=22 by 1",
                "rotate column x=15 by 1",
                "rotate row y=2 by 18",
                "rotate row y=0 by 12",
                "rotate column x=8 by 2",
                "rotate column x=7 by 1",
                "rotate column x=5 by 2",
                "rotate column x=2 by 1",
                "rotate column x=0 by 1",
                "rect 9x1",
                "rotate row y=3 by 28",
                "rotate row y=1 by 28",
                "rotate row y=0 by 20",
                "rotate column x=18 by 1",
                "rotate column x=15 by 1",
                "rotate column x=14 by 1",
                "rotate column x=13 by 1",
                "rotate column x=12 by 2",
                "rotate column x=10 by 3",
                "rotate column x=8 by 1",
                "rotate column x=7 by 2",
                "rotate column x=6 by 1",
                "rotate column x=5 by 1",
                "rotate column x=3 by 1",
                "rotate column x=2 by 2",
                "rotate column x=0 by 1",
                "rect 19x1",
                "rotate column x=34 by 2",
                "rotate column x=24 by 1",
                "rotate column x=23 by 1",
                "rotate column x=14 by 1",
                "rotate column x=9 by 2",
                "rotate column x=4 by 2",
                "rotate row y=3 by 5",
                "rotate row y=2 by 3",
                "rotate row y=1 by 7",
                "rotate row y=0 by 5",
                "rotate column x=0 by 2",
                "rect 3x2",
                "rotate column x=16 by 2",
                "rotate row y=3 by 27",
                "rotate row y=2 by 5",
                "rotate row y=0 by 20",
                "rotate column x=8 by 2",
                "rotate column x=7 by 1",
                "rotate column x=5 by 1",
                "rotate column x=3 by 3",
                "rotate column x=2 by 1",
                "rotate column x=1 by 2",
                "rotate column x=0 by 1",
                "rect 9x1",
                "rotate row y=4 by 42",
                "rotate row y=3 by 40",
                "rotate row y=1 by 30",
                "rotate row y=0 by 40",
                "rotate column x=37 by 2",
                "rotate column x=36 by 3",
                "rotate column x=35 by 1",
                "rotate column x=33 by 1",
                "rotate column x=32 by 1",
                "rotate column x=31 by 3",
                "rotate column x=30 by 1",
                "rotate column x=28 by 1",
                "rotate column x=27 by 1",
                "rotate column x=25 by 1",
                "rotate column x=23 by 3",
                "rotate column x=22 by 1",
                "rotate column x=21 by 1",
                "rotate column x=20 by 1",
                "rotate column x=18 by 1",
                "rotate column x=17 by 1",
                "rotate column x=16 by 3",
                "rotate column x=15 by 1",
                "rotate column x=13 by 1",
                "rotate column x=12 by 1",
                "rotate column x=11 by 2",
                "rotate column x=10 by 1",
                "rotate column x=8 by 1",
                "rotate column x=7 by 2",
                "rotate column x=5 by 1",
                "rotate column x=3 by 3",
                "rotate column x=2 by 1",
                "rotate column x=1 by 1",
                "rotate column x=0 by 1",
                "rect 39x1",
                "rotate column x=44 by 2",
                "rotate column x=42 by 2",
                "rotate column x=35 by 5",
                "rotate column x=34 by 2",
                "rotate column x=32 by 2",
                "rotate column x=29 by 2",
                "rotate column x=25 by 5",
                "rotate column x=24 by 2",
                "rotate column x=19 by 2",
                "rotate column x=15 by 4",
                "rotate column x=14 by 2",
                "rotate column x=12 by 3",
                "rotate column x=9 by 2",
                "rotate column x=5 by 5",
                "rotate column x=4 by 2",
                "rotate row y=5 by 5",
                "rotate row y=4 by 38",
                "rotate row y=3 by 10",
                "rotate row y=2 by 46",
                "rotate row y=1 by 10",
                "rotate column x=48 by 4",
                "rotate column x=47 by 3",
                "rotate column x=46 by 3",
                "rotate column x=45 by 1",
                "rotate column x=43 by 1",
                "rotate column x=37 by 5",
                "rotate column x=36 by 5",
                "rotate column x=35 by 4",
                "rotate column x=33 by 1",
                "rotate column x=32 by 5",
                "rotate column x=31 by 5",
                "rotate column x=28 by 5",
                "rotate column x=27 by 5",
                "rotate column x=26 by 3",
                "rotate column x=25 by 4",
                "rotate column x=23 by 1",
                "rotate column x=17 by 5",
                "rotate column x=16 by 5",
                "rotate column x=13 by 1",
                "rotate column x=12 by 5",
                "rotate column x=11 by 5",
                "rotate column x=3 by 1",
                "rotate column x=0 by 1"]


#instructions = ["rect 3x2",
#               "rotate column x=1 by 1",
#               "rotate row y=0 by 4",
#               "rotate column x=1 by 1"]

cols = 50
rows = 6

screen = [["." for _ in range(cols)] for _ in range(rows)]

def screen_print(screen):

    #rows = len(screen)
    #cols = len(screen[0])
    for row in range(rows):
        row_print = ""

        for col in range(cols):
            row_print += screen[row][col]
        print row_print


screen_print(screen)
    
for instruction in instructions:

    if instruction.startswith("rect"):
        tmp = instruction.split(" ")
        cols_rows = tmp[1].split("x")
        #print cols_rows

        for col in range(int(cols_rows[0])):
            for row in range(int(cols_rows[1])):
                screen[row][col] = "#"

    # Rotate COl
    if instruction.startswith("rotate column"):
        tmp = instruction.split(" ")
        rotate_amt = int(tmp[4])
        col = int(tmp[2].split("=")[1])
        #print col, rotate_amt

        tmp_list = []
        for x in range(rows):
            tmp_list.append(screen[x][col])

        d = deque(tmp_list)
        d.rotate(rotate_amt)
        for x in range(rows):
            screen[x][col] = d[x]

    # Rotate ROW
    if instruction.startswith("rotate row"):
        tmp = instruction.split(" ")
        rotate_amt = int(tmp[4])
        row = int(tmp[2].split("=")[1])
        #print row, rotate_amt

        tmp_list = []
        for x in range(cols):
            tmp_list.append(screen[row][x])

        d = deque(tmp_list)
        d.rotate(rotate_amt)
        for x in range(cols):
            screen[row][x] = d[x]

screen_print(screen)
lit_pixels = 0
for row in range(rows):
    for col in range(cols):
        if screen[row][col] == "#":
            lit_pixels += 1

print lit_pixels
