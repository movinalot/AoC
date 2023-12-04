"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "02"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line)

if DEBUG:
    print(len(puzzle_data), puzzle_data)

GAME_ID_SUM = 0
LIMITS = {"red": 12, "green": 13, "blue": 14}
VALID_GAME = True

for line in puzzle_data:
    GAME_ID = line.split(":", maxsplit=1)[0].strip()

    for handfuls_of_cubes in line.split(":")[1].split(";"):
        cubes = handfuls_of_cubes.strip()
        VALID_GAME = True
        for cube_type in cubes.split(","):
            if cube_type:
                color = cube_type.split()[1]
                count = int(cube_type.split()[0])
                if count > LIMITS[color]:
                    VALID_GAME = False
                    break
        if not VALID_GAME:
            break
    if VALID_GAME:
        GAME_ID_SUM += int(GAME_ID.split()[1])


ANSWER = GAME_ID_SUM

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
