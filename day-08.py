# with open("input-08.in") as file:
#     trees = [i for i in file.read().strip().split("\n")]
with open("./data-inputs/input-08.in") as file:
    trees = [i for i in file.read().strip().split("\n")]

# print(trees)

visibleRows = len(trees)
visibleColumns = len(trees[0])

visibleEdges =  2 * visibleColumns + 2 * (visibleColumns-2)

# variable to count totat sum of visible trees
total = visibleEdges
scores = []

# first and the last one row and column is visible so I don't have to check them anyway
for row in range(1,visibleRows-1):
    for column in range(1, visibleColumns-1):
        # print(column)
        # at which row and then which column we are currently
        tree = trees[row][column]
        # I am looking for all trees located on the left side of my tree
        # from one to current column + 1 cuz it counts from 0 and we need substract something in first loop
        left = [trees[row][column-i] for i in range(1, column+1)]
        # I am looking for all trees located on the right side of my tree
        # difference between our current column and sum of all columns
        right = [trees[row][column+i]for i in range(1,visibleColumns - column)]
        # print(right)
        # I am looking for all trees located above my tree
        # difference between our current row and sum of all rows
        up = [trees[row-i][column] for i in range(1, row+1)]
        # I am looking for all trees located below my tree
        down = [trees[row+i][column] for i in range(1, visibleRows - row)]
        

        # --------- PART 1 ---------
        if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
            total += 1
         # --------- PART 2 ---------
        
        score = 1
        for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] == tree:
                    tracker +=1
                    break
                else:
                     break
            score *= tracker

        scores.append(score)



    
# --------- ANSWERS ---------
print(f"Answer to part 1 day-08: {total}")
print(f"Answer to part 2 day-08: {max(scores)}")