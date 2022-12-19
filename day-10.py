with open("./data-inputs/input-10.in") as file:
    lines = [i for i in file.read().strip().split("\n")]

# counting signal_strngth - DRY function
def signal_strengths(cycles, x):
    return int(cycles * x)

# variables to count etc.
singal_strengths_sum = 0
# array of cycles that we want to count
cycle_array = [20, 60, 100, 140, 180, 220]
# starts from 1
x = 1
# number of been cycles
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


# ---------- PART 2 ----------
cur_X = 1
op = 0 
ans = 0

row = 0
column = 0

X =[1] * 241

for line in lines:
    parts = line.split(" ")

    if parts[0] == "noop":
        op += 1
        X[op] = cur_X

    elif parts[0] == "addx":
        V = int(parts[1])

        X[op + 1] = cur_X
        cur_X += V

        op += 2
        X[op] = cur_X

ans = [[None] * 40 for _ in range(6)]


for row in range(6):
    for col in range(40):
        conuter = row * 40 + col + 1
        if abs(X[conuter - 1] - (col)) <= 1:
            ans[row][col] = "##"
        else:
            ans[row][col] = "  "

for row in ans:
    print("".join(row))


# ---------- ANSWERS ----------
print(f"Answer to part 1 day-10: {singal_strengths_sum}")
# print(f"Answer to part 2 day-10: {answerPart2}")
