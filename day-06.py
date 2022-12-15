# getting my data from file
with open("input-06.in") as file:
    readedFile = file.read().strip()

# I used sets to findout when some combination of chars is unique 

# function to find first Marker
def findingFristMarker():
    for i in range(len(readedFile)):
        # using set to check if len(set) == 4 if so then I know that chars are unique
        # checking all combinations untill chars are unique then return the value (i+4 - taskt need it) == breaking
        if len(set(readedFile[i:i+4])) == 4: 
            return readedFile[i:i+4], i+4

# function that does the same thing but insted of 4 chars we have 14 chars that have to be unique
def findingFirstMessage():
    for i in range(len(readedFile)):
        # using set to check if len(set) == 14 if so then I know that chars are unique
        # checking all combinations untill chars are unique then return the value (i+14 - tasks need it)== breaking
        if len(set(readedFile[i:i+14])) == 14: 
            return readedFile[i:i+14], i+14

answerPart1 = findingFristMarker()
print(f"Answer to part 1 day-06: {answerPart1[1]}")
answerPart2 = findingFirstMessage()
print(f"Answer to part 2 day-06: {answerPart2[1]}")