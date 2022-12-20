from string import ascii_lowercase
from heapq import heappop, heappush

with open('./data-inputs/input-12.in') as file:
    lines = file.read().strip().split()
    
  
# ---------- PART 2 ---------- 
# do the same thing but starting from behind (E) - ends and ending in every "a" in my map 
# so we are searching to the closest "a" and then print how many steps we had to made

grid = [list(line) for line in lines]
n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            start = i,j
            # print(start)
        elif grid[i][j] == "E":
            end = i,j
            # print(end)

def height(s):
    if s in ascii_lowercase:
        # we are searching for index in english alphabet that's our height
        return ascii_lowercase.index(s)
    if s == "S":
        return 0 
    if s == "E":
        return 25

# it yielding us a posible neighbours that we can go to and they meet conditions
def neighbors(i,j):
    # down up right left
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ii = i + di
        jj = j + dj

        # checking if these new points are still in our map
        if not(0 <= ii < n and 0 <= jj < m):
            continue
        
        # here is the difference - we can go only if the next one is one level less 
        if height(grid[ii][jj]) >= height(grid[i][j]) - 1:
            yield ii, jj

# ---------- PART 1 ----------

visited = [[False]* m for _ in range(n)]
# heap that contains costs that we have to pay to achive point and this point 
# "sorted all the time"
# we are backtracking so starting from the end
heap = [(0, end[0], end[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    if height(grid[i][j]) == 0:
        break
    
    for ii, jj in neighbors(i,j):
        heappush(heap, (steps + 1, ii, jj))


# ---------- ANSWERS ----------
print(f"Answer to part 2 day-12: {steps}")


