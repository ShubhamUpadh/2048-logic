from move import move_down, move_left, move_right, move_up, printGrid
from randomTile import generateRandomTile, generateRandomTileFirstChance
flag = 0
grid = [[0 for _ in range(4)] for _ in range(4)]
while flag < 10:
    if flag == 0:
        print("Welcome to the 2048 game")
        grid = generateRandomTileFirstChance(grid=grid)
        flag = not flag
        printGrid(grid)
        continue
    inputVal = int(input("1 for up, 2 for down, 3 for left, 4 for right - "))
    if inputVal not in [1,2,3,4]:
        print("Enter a value between 1 - 4")
        continue
    if inputVal == 1:
        grid = move_up(grid)
    elif inputVal == 2:
        grid = move_down(grid)
    elif inputVal == 3:
        grid = move_left(grid)
    elif inputVal == 4:
        grid = move_right(grid)
    grid = generateRandomTile(grid)
    printGrid(grid)
    flag += 1