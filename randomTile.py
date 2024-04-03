import random

class generateRandom:

    def __init__(self,grid) -> None:
        self.grid = grid
    
    def printGrid(self)->list[list[int]]:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j],end ="")
                if j != len(self.grid[0]) - 1:
                    print(end=" | ")
            print()
        print("")
        
    def generateRandomTile(self)->list[list[int]]:
        emptyCells = [(i,j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if len(emptyCells) != 0:
            randomCell = random.choice(emptyCells)
            randomCellVal = random.choices([2,4],weights=[0.8,0.2])
            self.grid[randomCell[0]][randomCell[1]] = randomCellVal[0]
        return self.grid

    def generateRandomTileFirstChance(self)->list[list[int]]:
        randomCell = random.choice([(i,j) for i in range(4) for j in range(4)])
        self.grid[randomCell[0]][randomCell[1]] = 2
        emptyCells = [(i,j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        randomCell = random.choice(emptyCells)
        self.grid[randomCell[0]][randomCell[1]] = 2
        return self.grid


if __name__ == "__main__":
    print("here")
    for i in range(3):
        grid = [[4,2,8,4],
                [2,0,2,2],
                [0,0,0,2],
                [0,0,2,0]]
        #grid = [[0 for _ in range(4)] for _ in range(4)]
        genR = generateRandom(grid)
        genR.generateRandomTile()
        genR.printGrid()
    for i in range(3):
        grid = [[0 for _ in range(4)]for _ in range(4)]
        genR = generateRandom(grid)
        genR.generateRandomTileFirstChance()
        #genR.printGrid()
        