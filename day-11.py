with open("./data-inputs/input-11.in") as file:
    lines = [i for i in file.read().strip().split("\n")]

# monkey = {
#     0: [Operation, Test, true, false]
# }

# ---------- PART 1 ----------

monkey = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
items = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
inspections = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

# extracting data - loading data function
def loadingData():
    index = 0 
    for line in lines:
            if "Starting items" in line:
                items[index] = line[line.find(":") + 2:].split(", ")
            elif "Operation" in line:
                monkey[index].append(line[line.find("old ") + 4:])
            elif "Test" in line:
                monkey[index].append(line[line.find("by ") + 3:])
            elif "If true" in line: 
                monkey[index].append(line[line.find("monkey") + 7:])
            elif "If false" in line: 
                monkey[index].append(line[line.find("monkey") + 7:])
                index +=1 


# print(monkey)
round = 0
loadingData()
for _ in range(20):
    round += 1
    for key in items:
        for worry in items[key]:
            inspections[key] +=1
            # checking conditions
            if "* " in monkey[key][0]: 
                if monkey[key][0][2:] == "old":
                    worryAfter = int(worry) * int(worry)
                else:
                    worryAfter = int(worry) * int(monkey[key][0][2:])
            elif "+ " in monkey[key][0]:
                # if monkey[key][0][2:] == "old":
                #     worryAfter = int(worry) + int(worry)
                # else:
                worryAfter = int(worry) + int(monkey[key][0][2:])
            worryAfter = int(worryAfter / 3)
            if worryAfter % int(monkey[key][1]) == 0:
                # appending to the new monkey items my worryAfter
                items[int(monkey[key][2])].append(worryAfter)
            else:
                # appending to the new monkey items my worryAfter modulo
                items[int(monkey[key][3])].append(worryAfter)
            # that was wrong !!! - iterators was the problem cuz array was shorter and shorter 
            # items[key].pop(0)
        # cannot use pop - because of iterators so I erase array at once
        items[key] = []
        
        # print("\n",items ,round)
    
# sorting and counting monkey business
sorted_monkey_biz = sorted(inspections.values(), reverse=True)
answer_part_1 = sorted_monkey_biz[0] * sorted_monkey_biz[1]

 
# ---------- PART 2 ---------- - my first solution

monkey = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
items = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
inspections = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

# extracting data - loading data function
def loadingData():
    index = 0 
    for line in lines:
            if "Starting items" in line:
                items[index] = line[line.find(":") + 2:].split(", ")
            elif "Operation" in line:
                monkey[index].append(line[line.find("old ") + 4:])
            elif "Test" in line:
                monkey[index].append(line[line.find("by ") + 3:])
            elif "If true" in line: 
                monkey[index].append(line[line.find("monkey") + 7:])
            elif "If false" in line: 
                monkey[index].append(line[line.find("monkey") + 7:])
                index +=1 

loadingData()
# counting big_modulo number - all of tests in 1 number
big_mod = 1
for mon in monkey:
    big_mod *= int(monkey[mon][1]) 
round = 0

for _ in range(10000):
    round += 1
    for key in items:
        for worry in items[key]:
            inspections[key] +=1
            # checking conditions
            if "* " in monkey[key][0]: 
                if monkey[key][0][2:] == "old":
                    ans = int(worry) * int(worry)
                    # I take only modulo of my answer - thanks to that I acting on smaller numbers --> faster
                    worryAfter = ans % big_mod
                else:
                    ans = int(worry) * int(monkey[key][0][2:])
                    # I take only modulo of my answer - thanks to that I acting on smaller numbers --> faster
                    worryAfter = ans % big_mod
            elif "+ " in monkey[key][0]:
                ans = int(worry) + int(monkey[key][0][2:])
                # I take only modulo of my answer - thanks to that I acting on smaller numbers --> faster
                worryAfter = ans % big_mod
            # worryAfter = int(worryAfter / 3)
            if worryAfter % int(monkey[key][1]) == 0:
                # appending to the new monkey items my worryAfter modulo
                items[int(monkey[key][2])].append(worryAfter)
            else:
                # appending to the new monkey items my worryAfter modulo
                items[int(monkey[key][3])].append(worryAfter)
            # that was wrong !!! - iterators was the problem cuz array was shorter and shorter 
            # items[key].pop(0)
        # cannot use pop - because of iterators so I erase array at once
        items[key] = []
        
        # print("\n",items ,round)
    
# sorting and counting monkey business
sorted_monkey_biz = sorted(inspections.values(), reverse=True)
answer_part_2 = sorted_monkey_biz[0] * sorted_monkey_biz[1]



# ---------- PART 2 ---------- - another solution


with open("./data-inputs/input-11.in") as file:
    raw_data = file.read().strip()
    monkey_parts = raw_data.split("\n\n")

# array that includes all of my monkeys
monkeys = []

# class that represents monkey
class Monkey:
    def __init__(self, items, operation, test) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0
    
    def __str__(self) -> str:
        return f'{self.items}, {self.operation}, {self.test}'

# destructing monkeys and their properties
for i, monkey_part in enumerate(monkey_parts):
    lines = monkey_part.split("\n")
    items = list(map(int, lines[1][2:].split(" ", 2)[2].split(", ")))
    operation = lines[2][2:].split(" ",3)[3].split(" ")

    mod = int(lines[3][2:].split(" ")[-1])
    if_true = int(lines[4][4:].split(" ")[-1])
    if_false = int(lines[5][4:].split(" ")[-1])

    # appending monkey to array of monkeys
    monkeys.append(Monkey(items, operation,[mod, if_true, if_false]))

# counting this big_modulo thing
big_mod = 1 
for monkey in monkeys:
    big_mod *=monkey.test[0]


N = len(monkeys)

# dealing with operations and values
def operations(operation, x):
    left, op, right = operation

    assert left == 'old'

    if op == "+":
        ans = x + int(right)
    else:
        if right == "old":
            ans = x * x
        else:
            ans = x * int(right)
    # returning answer % modulo == the same value + smaller number so easier to act on that later
    return ans % big_mod


# my main for loop
for round in range(10000):
    for i in range(N):
        monkey = monkeys[i]
        for item in monkey.items:
            # using operation function
            item = operations(monkey.operation, item)
                        
            mod, if_true, if_false = monkey.test
            
            # assingin new items to other monkeys
            if item % mod == 0:
                monkeys[if_true].items.append(item)
            else:
                monkeys[if_false].items.append(item)
            
            # increasing inspections of each monkey
            monkey.inspections += 1

        monkey.items = []

# counting amounts of inspecitons
amounts = [m.inspections for m in monkeys]
# sorting all of inspections
sorted_amts = sorted(amounts)
# multiplying the two biggest amounts
# print(sorted_amts[-1] * sorted_amts[-2]) 


# ---------- ANSWERS ----------
print(f"Answer to part 1 day-11: {answer_part_1}")
print(f"Answer to part 2 day-10: {answer_part_2}")


