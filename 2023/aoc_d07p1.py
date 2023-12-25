"""
John McDonough
    github - movinalot
    Advent of Code 2023
"""

TESTING = 0
DEBUG = 0
DAY = "07"
YEAR = "2023"
PART = "1"
ANSWER = None

if TESTING:
    puzzle_data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ]
else:
    with open("puzzle_data_" + DAY + "_" + YEAR + ".txt", encoding="utf-8") as f:
        puzzle_data = []
        for line in f:
            puzzle_data.append(line.strip())

if DEBUG:
    print(len(puzzle_data), puzzle_data)

TOTAL_WINNINGS = 0

CARDS = {
    "A": "E",
    "K": "D",
    "Q": "C",
    "J": "B",
    "T": "A",
    "9": "9",
    "8": "8",
    "7": "7",
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2",
}

FIVE_OF_A_KINDS = []
FOUR_OF_A_KINDS = []
FULL_HOUSES = []
THREE_OF_A_KINDS = []
TWO_PAIRS = []
ONE_PAIRS = []
HIGH_CARDS = []

for line in puzzle_data:
    ORIG_HAND = line.split(" ", maxsplit=1)[0]
    BID = int(line.split(" ")[1])

    HAND = [list(ORIG_HAND).count(card) for card in set(list(ORIG_HAND))]
    HAND.sort()

    HEX_HAND = [CARDS[card] for card in list(ORIG_HAND)]
    HEX_NUM = int("".join(HEX_HAND), base=16)

    if HAND.count(5) == 1:
        FIVE_OF_A_KINDS.append((HEX_NUM, BID))
    elif HAND.count(4) == 1:
        FOUR_OF_A_KINDS.append((HEX_NUM, BID))
    elif HAND.count(3) == 1 and HAND.count(2) == 1:
        FULL_HOUSES.append((HEX_NUM, BID))
    elif HAND.count(3) == 1 and HAND.count(1) == 2:
        THREE_OF_A_KINDS.append((HEX_NUM, BID))
    elif HAND.count(2) == 2 and HAND.count(1) == 1:
        TWO_PAIRS.append((HEX_NUM, BID))
    elif HAND.count(2) == 1 and HAND.count(1) == 3:
        ONE_PAIRS.append((HEX_NUM, BID))
    elif HAND.count(1) == 5:
        HIGH_CARDS.append((HEX_NUM, BID))

    if DEBUG:
        print(ORIG_HAND, set(list(ORIG_HAND)), HAND, HEX_HAND)

FIVE_OF_A_KINDS.sort()
FOUR_OF_A_KINDS.sort()
FULL_HOUSES.sort()
THREE_OF_A_KINDS.sort()
TWO_PAIRS.sort()
ONE_PAIRS.sort()
HIGH_CARDS.sort()

ALL_HANDS = []

for _ in (
    HIGH_CARDS,
    ONE_PAIRS,
    TWO_PAIRS,
    THREE_OF_A_KINDS,
    FULL_HOUSES,
    FOUR_OF_A_KINDS,
    FIVE_OF_A_KINDS,
):
    ALL_HANDS.extend(_)

if DEBUG:
    print(FIVE_OF_A_KINDS)
    print(FOUR_OF_A_KINDS)
    print(FULL_HOUSES)
    print(THREE_OF_A_KINDS)
    print(TWO_PAIRS)
    print(ONE_PAIRS)
    print(HIGH_CARDS)
    print(ALL_HANDS)


for rank, ranked_hand in enumerate(ALL_HANDS):
    TOTAL_WINNINGS += ranked_hand[1] * (rank + 1)

ANSWER = TOTAL_WINNINGS

print("AoC Day: " + DAY + " Year: " + YEAR + " part " + PART + ", answer:", ANSWER)
