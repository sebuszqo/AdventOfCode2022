with open("./data-inputs/input-11.in") as file:
    lines = [i for i in file.read().strip().split("\n")]





# monkey = {
#     0: [Operation, Test, true, false]
# }

monkey = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
items = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
inspections = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}
index = 0 
# extracting data
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
for _ in range(20):
    round += 1
    for key in items:
        print("1", key)
        for worry in items[key]:
            print('2',key)
            inspections[key] +=1
            # print(items[key])
            # print(worry)
            
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
                items[int(monkey[key][2])].append(worryAfter)
            else:
                items[int(monkey[key][3])].append(worryAfter)
            # that was wrong !!! - iterators was the problem cuz array was shorter and shorter 
            # items[key].pop(0)
        items[key] = []
        
        # print("\n",items ,round)
    
abc = sorted(inspections.values(), reverse=True)
print(abc[0] * abc[1])
