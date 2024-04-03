import random

def generateRandomTile(grid:list[list[int]])->list[list[int]]:
    emptyCells = [(i,j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if len(emptyCells) != 0:
        randomCell = random.choice(emptyCells)
        randomCellVal = random.choices([2,4],weights=[0.8,0.2])
        grid[randomCell[0]][randomCell[1]] = randomCellVal[0]
    return grid

def generateRandomTileFirstChance(grid:list[list[int]])->list[list[int]]:
    randomCell = random.choice([(i,j) for i in range(4) for j in range(4)])
    grid[randomCell[0]][randomCell[1]] = 2
    emptyCells = [(i,j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    randomCell = random.choice(emptyCells)
    grid[randomCell[0]][randomCell[1]] = 2
    return grid

def printGrid(grid:list[list[int]])->list[list[int]]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end ="")
            if j != len(grid[0]) - 1:
                print(end=" | ")
        print()
    print("")

if __name__ == "__main__":
    print("here")
    for i in range(3):
        grid = [[4,2,8,4],
                [2,0,2,2],
                [0,0,0,2],
                [0,0,2,0]]
        grid = [[0 for _ in range(4)] for _ in range(4)]
        generateRandomTile(grid)
    for i in range(3):
        grid = [[0 for _ in range(4)]for _ in range(4)]
        grid = generateRandomTileFirstChance(grid)
        printGrid(grid)
        