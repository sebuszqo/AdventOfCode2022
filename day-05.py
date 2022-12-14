

with open("input-05.in") as f:
    stack_strings, instructions = (i.splitlines() for i in f.read().strip("\n").split("\n\n"))

stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "] 

def displayStacks():
    print("\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


def loadingStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_num].insert(0,string[index])
            stack_num +=1

def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getEndOfStack():
    answer = ''
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

loadingStacks()

#  ----------- PART 1 -----------
for instruction in instructions:
    instruction = instruction.replace("move","").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [ int(i) for i in instruction]
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)
        # print(crate_removed)
answerPart1 = getEndOfStack()


#  ----------- PART 2 -----------
emptyStacks()
loadingStacks()

for instruction in instructions:
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

