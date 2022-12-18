
# getting data
with open("./data-inputs/input-01.in") as file:
    data = [i for i in file.read().strip().split("\n")]
    # print(data)

# dealing with sorting and summing calories
elfSum = 0
arrOfsum = [] 
for i in data:
    if i != '':
        elfSum += int(i)
    if i == '':
        arrOfsum.append(elfSum)
        elfSum = 0

arrOfsum.sort(reverse=True)
print(f'Answer to part 1 day-01: {arrOfsum[0]}')
print(f'Answer to part 2 day-01: {sum(arrOfsum[:3])}')
