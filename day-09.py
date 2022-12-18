with open("./data-inputs/input-09.in") as file:
    lines = file.read().strip().split("\n")

# head position
hx, hy = 0, 0
# tail position
tx, ty = 0, 0


def isTouching(x1,y1,x2,y2):
    return abs(x1-x2) <=1 and abs(y1-y2) <=1

# ---------- PART 1 ----------
def move_Part_1(dx, dy):
    # bad practise
    global hx, hy, tx, ty

    # updating position of the head by numbers that were given 
    hx += dx
    hy += dy

    # we are updating tail cooridinates only if they are not touching 
    if not isTouching(hx, hy, tx, ty):
        # head never will be more than 2 units above than a tail !
        # hx - tx = negative if head is on the left side of tail
        # hx - tx = positive if head is on the right side of tail
        # hx - tx = 0 if they are in the same cloumn --> hx = tx
        # normalizin it by dividing it 
        sign_x = 0 if hx == tx else (hx-tx) / abs(hx-tx)
        # same thing with the y things
        # again differene bettwen hy and ty move it up or down + up - down 
        sign_y = 0 if hy == ty else (hy-ty) / abs(hy -ty)
        # 
        #    o
        #  h |
        #  y |
        #  - |
        #  h |
        #  t |_ _ _ _ _ _ o
        #       hx - tx
        # 
        tx += sign_x
        ty += sign_y
    
directions = {
        "R": (1,0),
        "U": (0,1),
        "D": (0,-1),
        "L": (-1,0)
    }

tail_visited1 = set()
# adding the tail position to a set to count how much different positions it takes
tail_visited1.add((tx,ty))

for line in lines:
    operation, amount = line.split(" ")
    amount = int(amount)
    dx, dy = directions[operation]

    for _ in range(amount):
        # moving my head and tail
        move_Part_1(dx, dy)
        # adding the tail position to a set to count how much different positions it takes
        tail_visited1.add((tx,ty))


# ---------- PART 2 ----------
with open("./data-inputs/input-09.in") as fin:
    lines = fin.read().strip().split("\n")


knots = [[0, 0] for _ in range(10)]


def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


def move(dx, dy):
    global knots
    knots[0][0] += dx
    knots[0][1] += dy

    for i in range(1, 10):
        hx, hy = knots[i - 1]
        tx, ty = knots[i]

        if not touching(hx, hy, tx, ty):
            sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
            sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

            tx += sign_x
            ty += sign_y

        knots[i] = [tx, ty]


dd = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

tail_visited = set()
tail_visited.add(tuple(knots[-1]))

for line in lines:
    op, amount = line.split(" ")
    amount = int(amount)
    dx, dy = dd[op]

    for _ in range(amount):
        move(dx, dy)
        tail_visited.add(tuple(knots[-1]))

# print(len(tail_visited))

# ---------- ANSWERS ----------
print(f"Answer to part 1 day-09: {len(tail_visited1)}")
print(f"Answer to part 2 day-09: {len(tail_visited)}")