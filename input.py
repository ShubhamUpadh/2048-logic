from move import move_class
from randomTile import generateRandom
grid = [[0 for _ in range(4)] for _ in range(4)]
moveClass = move_class(grid)
flag = 0
while flag < 10:
    if flag == 0:
        print("Welcome to the 2048 game")
        genR = generateRandom(grid)
        grid = genR.generateRandomTileFirstChance()
        moveClass.updateGrid(grid)
        flag = not flag
        moveClass.printGrid()
        continue
    inputVal = int(input("1 for up, 2 for down, 3 for left, 4 for right - "))
    if inputVal not in [1,2,3,4]:
        print("Enter a value between 1 - 4")
        continue
    if inputVal == 1:
        grid = moveClass.move_up()
    elif inputVal == 2:
        grid = moveClass.move_down()
    elif inputVal == 3:
        grid = moveClass.move_left()
    elif inputVal == 4:
        grid = moveClass.move_right()
    genR = generateRandom(grid)
    grid = genR.generateRandomTile()
    moveClass.updateGrid(grid)
    moveClass.printGrid()
    flag += 1