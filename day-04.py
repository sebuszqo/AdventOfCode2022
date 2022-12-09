# getting data
with open("input-04.in") as file:
    pairs = [i for i in file.read().strip().split("\n")]


# *********** PART 1 ***********

counterFirstPart = 0
for pair in pairs: 
    # splitting to first and second char - 45-33,4-12 -->first(45-33) second(4-12)
    first, second = pair.split(",")

    # list comprehension - to have 2 arrays [first, first] [second, second]
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]
    #  little if statment - to count how many of them are in ranges 
    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
        counterFirstPart += 1

# *********** PART 2 ***********
counterSecondPart = 0
for pair in pairs:
    first, second = pair.split(",")
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]
    if first[0] in range(second[0], second[1]+1) or first[1] in range(second[0],second[1]+1):
        counterSecondPart +=1
    elif second[0] in range(first[0], first[1] + 1) or second[1] in range(first[0], first[1]+1):
        counterSecondPart +=1


print(f"Answer to part 1 day-03: {counterFirstPart}")
print(f"Answer to part 2 day-03: {counterSecondPart}")


