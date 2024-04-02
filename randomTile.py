import random

def generateRandomTile(grid):
    emptyCells = [(i,j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if len(emptyCells) != 0:
        randomCell = random.choice(emptyCells)
        randomCellVal = random.choices([2,4],weights=[0.8,0.2])
        grid[randomCell[0]][randomCell[1]] = randomCellVal

if __name__ == "__main__":
    print("here")
    for i in range(3):
        grid = [[4,2,8,4],
                [2,0,2,2],
                [0,0,0,2],
                [0,0,2,0]]
        grid = [[0 for _ in range(4)] for _ in range(4)]
        generateRandomTile(grid)