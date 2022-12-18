from collections import Counter

with open("./data-inputs/input-03.in") as file:
    things = [i for i in file.read().strip().split("\n")]

# my aphabet with points
alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18,"s":19,"t":20, "u":21, "v":22, "w":23, "x":24,"y":25, "z":26,
"A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44,"S":45,"T":46, "U":47, "V":48, "W":49, "X":50,"Y":51, "Z":52}

# *********** PART 1 ***********

sumOfPoints1 = 0
for thing in things:
    # dividing every strings to 2 halfs
    left = set(thing[:len(thing)//2])
    right = set(thing[len(thing)//2:])

    arrayOfDoubled = Counter(list(left) + list(right))
    for x,y in zip(arrayOfDoubled.values(),arrayOfDoubled.keys()):
        if x > 1:
            sumOfPoints1 += alphabet[y]


# *********** PART 2 ***********

sumOfPoints2 = 0
# iterating step = 3 to use i + 1, i + 2, i + 3
for i in range(0,len(things),3):
    first = set(things[i])
    second = set(things[i+1])
    third = set(things[i+2])
    # merge my lists to Counter - to find out what repeats 
    arrayOfTripled = Counter(list(first) + list(second)+ list(third))
    for x,y in zip(arrayOfTripled.values(),arrayOfTripled.keys()):
        # we need only situations where 3 chars are the same --> if x > 2
        if x > 2:
            sumOfPoints2 += alphabet[y]




print(f"Answer to part 1 day-03: {sumOfPoints1}")
print(f"Answer to part 2 day-03: {sumOfPoints2}")


# ************ PART 1 - another solution ***********

# Instead of alphabet dict - it doing the same thing
from string import ascii_letters
totalSum = 0
for thing in things:
    # this loop give me my points - a = 1 etc.
    for point, char in enumerate(ascii_letters):
        # dividing every string to 2 halfs
        left = thing[:len(thing)//2] # do not need even a set()
        right = thing[len(thing)//2:]
        if char in left and char in right:
            # +1 cuz we count from 1 not from 0 
            totalSum += point + 1
print(totalSum)

# *********** "SOLUTION PART 2" - another way ***********

# - similar thing with part 2
# rucksacks = things[i:j]
# j +=3
# for point, char in enumerate(ascii_letters):
#        if char in set(rucksacks[0]) and set(rucksacks[1]) in set(rucksacks[2]):
#             +1 cuz we count from 1 not from 0 
#             totalSum += point + 1 