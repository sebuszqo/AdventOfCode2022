with open("input-07.in") as file:
    commands = [i for i in file.read().strip().split("\n")]

# --------- PART 1 ---------
currentPath = '/home'
dirs = {"/home":0}
for command in commands:
    if command[0:3] == "dir":
        pass
    elif command[0] == "$":             
        if command[2:4] == "cd":
            if command[5:6] == "/":
                currentPath = "/home"
            elif command[5:7] ==  "..":
                currentPath = currentPath[:currentPath.rfind("/")]
            else:
                dir_name = command[5:]
                currentPath = currentPath + "/" + dir_name
                dirs[currentPath] = 0
        elif command[2:4] == "ls":
            pass
    else:
        dir = currentPath
        for i in range(currentPath.count("/")):
            dirs[dir] += int(command.split(" ")[0])
            dir = dir[:dir.rfind("/")]


sumOfDirs = 0
# print(dirs)
for value in dirs.values():
    if value <= 100000:
        sumOfDirs += value

# --------- PART 2 ---------
unusedSpace = 70000000 - dirs["/home"]
spaceWeNeed = 30000000
limit = spaceWeNeed - unusedSpace

arrayOfFilesToDelete = []
for dir,size in zip(dirs.keys(), dirs.values()):
    if size >= limit:
        arrayOfFilesToDelete.append((dir, size))
        arrSorted = sorted(arrayOfFilesToDelete,key = lambda x: x[1])
answerToPart2 = arrSorted[0][1]
    
   



print(f"Answer to part 1 day-07: {sumOfDirs}")
print(f"Answer to part 2 day-07: {answerToPart2}")