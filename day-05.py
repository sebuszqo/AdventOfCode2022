
# here I'm getting data - I have 2 parts of file first with crates second with instructions
with open("input-05.in") as f:
    stack_strings, instructions = (i.splitlines() for i in f.read().strip("\n").split("\n\n"))

# here I'm making a dict whre keys are numbers 1, 3, 4, 5, etc and values will be my crates
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}
# here I'm taking indexes where my keys and values are exacly in file
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "] 
print(stack_strings)
# printing my stack
def displayStacks():
    print("\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

# function to load stacks to dict
def loadingStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        # using index if index is == " " then nothing
        # indexes are indexes where only something is or is not - I mean it is not going from 1 to 10 (1,2,3,4) etc. 
        # but it knows exacly what indexes values have
        for index in indexes:
            if string[index] == " ":
                pass
            # Inserting crate if it exists to first place in value array 
            else:
                stacks[stack_num].insert(0,string[index])
            #  ++ stack_num 
            stack_num +=1

# function to make stacks empty after Part 1
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

# getting string which contains all of ends of stacks
def getEndOfStack():
    answer = ''
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

loadingStacks()

#  ----------- PART 1 -----------
for instruction in instructions:
    # making instructions more clear and making a array of ints number[]
    instruction = instruction.replace("move","").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [ int(i) for i in instruction]
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        # poping crates from from_stack and appending it to to_stack
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)
        # print(crate_removed)
answerPart1 = getEndOfStack()


#  ----------- PART 2 -----------
emptyStacks()
loadingStacks()

for instruction in instructions:
    # doing the same thing
    instruction = instruction.replace("move","").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [ int(i) for i in instruction]
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    # that is the part of stack that should be removed --> for example ['D', 'Z', 'S', 'F', 'M']- that should be removed ['D', 'Z', 'S', 'F', 'M'] - that is oryginal stack
    crates_to_remove = stacks[from_stack][-crates:]
    # we have to remove these stacks that we dont need any more somehow -- so :-creates - we cut arrray from 0 to -(number of crates to remove)
    stacks[from_stack] = stacks[from_stack][:-crates]
    # print(crates_to_remove,stacks[from_stack])
    for crate in crates_to_remove:
        stacks[to_stack].append(crate) #adding these crates to final stack
answerPart2 = getEndOfStack()

print(f"Answer to part 1 day-03: {answerPart1}")
print(f"Answer to part 2 day-03: {answerPart2}")

