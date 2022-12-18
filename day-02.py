# Opponents column:
# A - ROCK 
# B - PAPER
# C - SCISSORS

# What I have to play - points:
# X - ROCK - 1
# Y - PAPER - 2
# Z - SCISSORS - 3

# 0 - lost
# 3 - draw
# 6 - win


# getting data
with open("./data-inputs/input-02.in") as file:
    rounds = [i for i in file.read().strip().split("\n")]


# Part nr1
# All possible outcomes
# ---------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN = (2 + 6) = 8
# A vs Z = LOSE = (3 + 0) = 3
# B vs X = LOSE = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN = (3 + 6) = 9
# C vs X = WIN = (1 + 6) = 7
# C vs Y = LOSE = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

# my dict to find out how much points I took
possibleOutcomesPart1 = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6,
}

mySumOfPointsPart1 = 0
for round in rounds:
    # adding value of outcome
    mySumOfPointsPart1 += possibleOutcomesPart1[round]



# Part 2
# Y - draw
# X - lose
# Z - win
# All possible outcomes
# ---------------------
# A vs X = LOSE = (3 + 0) = 3
# A vs Y = DRAW = (1 + 3) = 4 
# A vs Z = WIN = (2 + 6) = 8
# B vs X = LOSE = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN = (3 + 6) = 9
# C vs X = LOSE = (2 + 0) = 2 
# C vs Y = DRAW = (3 + 3) = 6
# C vs Z = WIN = (1 + 6) = 7 

# Changed dict with loses draws and wins
possibleOutcomesPart2 = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7,
}

mySumOfPointsPart2 = 0
for round in rounds:
    # adding value of outcome 
    mySumOfPointsPart2 += possibleOutcomesPart2[round]


print(f"Answer to part 1 day-02: {mySumOfPointsPart1}")
print(f"Answer to part 2 day-02: {mySumOfPointsPart2}")