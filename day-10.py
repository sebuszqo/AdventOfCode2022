with open("./data-inputs/input-10.in") as file:
    lines = [i for i in file.read().strip().split("\n")]

# counting signal_strngth - DRY function
def signal_strengths(cycles, x):
    return int(cycles * x)


singal_strengths_sum = 0
# array of cycles that we want to count
cycle_array = [20, 60, 100, 140, 180, 220]
x = 1
cycles = 0

# commented lines are the another solution of this challange
# list_x=[X]

# ---------- PART 1 ----------
for line in lines:
    # simple if's
    if line[0:4] == "addx":
        # list_x.extend([x,x])
        for _ in range(2):
            cycles += 1
            if cycles in cycle_array:
                singal_strengths_sum += signal_strengths(cycles, x)     
        x += int(line[5:])
    elif line[0:4] == "noop":
        # list_x.append(x)
        cycles += 1 
        if cycles in cycle_array:
            singal_strengths_sum += signal_strengths(cycles, x)   
        

# singal_strengths_sum = sum(list_x[cycle] * cycle for cycle in range(20, len(list_x), 40))


# ---------- ANSWERS ----------
print(f"Answer to part 1 day-10: {singal_strengths_sum}")
# print(f"Answer to part 2 day-10: {answerPart2}")
