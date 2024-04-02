def move_up(grid):
    for i in range(0,3,1):      #addition loop
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] = 2 * grid[i][j]
                grid[i+1][j] = 0
            elif grid[i][j] == 0 and grid[i+1][j] != 0:
                grid[i][j] = grid[i+1][j]
                grid[i+1][j] = 0
    for j in range(4):          # remove extra 0 spaces
        for j in range(3):
            pass
        pass
    return grid

def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end ="")
            if j != len(grid[0]) - 1:
                print(end=" | ")
        print()

def defineGrid():
    grid = [[0,0,2,0],
            [0,0,0,0],
            [0,4,8,0],
            [4,2,2,8]]
    return grid

if __name__ == "__main__":
    grid = defineGrid()
    printGrid(grid)
    print()
    grid = move_up(grid)
    printGrid(grid)