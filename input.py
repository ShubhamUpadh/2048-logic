from move import move_class
from randomTile import generateRandom
from gameEndCondition import gameEndConditions

grid = [[0 for _ in range(4)] for _ in range(4)]
moveClass = move_class(grid)
firstMove = True

while True:                                      # play the game infinitely

    if firstMove == True:                             # this means that this is the first chance 
        print("Welcome to the 2048 game")
        genR = generateRandom(grid)
        grid = genR.generateRandomTileFirstChance()
        moveClass.updateGrid(grid)
        firstMove = not firstMove
        moveClass.printGrid()
        continue

    # Game continuation logic
    gameState = gameEndConditions()
    gameStateVal = gameState.executionLogic(grid)

    if gameStateVal in (100,200):
        print(gameState.gameConditionsDict[gameStateVal])
        break
    
    changeGrid = True
    inputVal = int(input("1 for up, 2 for down, 3 for left, 4 for right - "))
    if inputVal not in [1,2,3,4]:
        print("Enter a value between 1 - 4")
        continue
    if inputVal == 1:
        gridRet, changeGrid = moveClass.move_up()
    elif inputVal == 2:
        grid, changeGrid = moveClass.move_down()
    elif inputVal == 3:
        grid, changeGrid = moveClass.move_left()
    elif inputVal == 4:
        grid, changeGrid = moveClass.move_right()
    
    if changeGrid:  #if any change in grid, thenn only generate a random element
        #print(changeGrid)
        genR = generateRandom(grid)
        grid = genR.generateRandomTile()
        moveClass.updateGrid(grid)
    
    moveClass.printGrid()
    print(changeGrid)