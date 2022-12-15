with open("input-07.in") as file:
    commands = [i for i in file.read().strip().split("\n")]

# --------- PART 1 ---------
currentPath = '/home'
dirs = {"/home":0}
for command in commands:
    # if my command is dir then I can pass - 'dir' changes nothing
    if command[0:3] == "dir":
        pass
    # every command that starts from $ is important 
    elif command[0] == "$":
        # 'cd' change directory - I'm finding out when it comes
        if command[2:4] == "cd":
            # 'cd /' - makes me go to '/home' path 
            if command[5:6] == "/":
                currentPath = "/home"
            #  'cd ..' - makes me go one dir up ;)
            elif command[5:7] ==  "..":
                # so I'am changing my path one up by cutting my current path from 0 to place where '/' shows 
                currentPath = currentPath[:currentPath.rfind("/")]
            # else - we are changing directory for real one so I'am setting new current path
            else:
                dir_name = command[5:]
                # I'm updating my current directory by adding / and my new dir_name
                currentPath = currentPath + "/" + dir_name
                # checking if currentPath exists in our dirs dict 
                # If yep then we shoulnd be doing 0 size for that dict 
                # I wouldn't say this tasks needs it at all - I mean in this task we never goes to the same dir more than one time
                # and even if we goes, we still dont need to counting from 0 cuz we counted it oneces before
                if currentPath not in dirs.keys():
                    # I'm setting dict of dirs to 0 for that directory
                    dirs[currentPath] = 0
        # If there is ls I cant simply pass - it changes nothing 
        elif command[2:4] == "ls":
            pass
    # else - when my command is not 'dir' or when my command is not starting from $
    # here magic comes
    else:
        # I'm copying my current path - because I need to use it to add size to dirs above
        dir = currentPath
        # I have to add this size of file to every dir that is upper than current dir
        for i in range(currentPath.count("/")):
            # Adding size to current dir
            dirs[dir] += int(command.split(" ")[0])
            # cutting dir one time up
            dir = dir[:dir.rfind("/")]


sumOfDirs = 0
# counting all values that are less or equals 100000
for value in dirs.values():
    if value <= 100000:
        sumOfDirs += value

# --------- PART 2 ---------
# counting unesed Space
unusedSpace = 70000000 - dirs["/home"]
# We need this amount of space to install update
spaceWeNeed = 30000000
# How much we need to delete? 
limit = spaceWeNeed - unusedSpace

arrayOfFilesToDelete = []
for dir,size in zip(dirs.keys(), dirs.values()):
    # if size of directory is bigger than limit I'm adding it to array 
    if size >= limit:
        arrayOfFilesToDelete.append((dir, size)) 
# after that I'm sorting this array from the smallest to the largest sizes 
# and I'm taking the smallest one that meets the conditions
answerToPart2 = sorted(arrayOfFilesToDelete,key = lambda x: x[1])[0][1]
    
# --------- ANSWERS ---------
print(f"Answer to part 1 day-07: {sumOfDirs}")
print(f"Answer to part 2 day-07: {answerToPart2}")