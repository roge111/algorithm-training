countCells = int(input())
countWells = 0
perimeter = 0
listWells = []
cell_x_past, cell_y_past = 0, 0
for numberCell in range(countCells):
    perimeter += 4
    cell_x, cell_y = map(int, input().split())
    if [cell_x - 1, cell_y] in listWells:
        countWells += 1
    if  [cell_x + 1, cell_y] in listWells:
        countWells += 1
    if [cell_x, cell_y - 1] in listWells:
        countWells += 1
    if [cell_x + 1, cell_y] in listWells:
        countWells += 1
    listWells.append([cell_x, cell_y])
    cell_x_past, cell_y_past = cell_x, cell_y
result = perimeter - countWells*2
print(result)