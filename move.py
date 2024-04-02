from collections import deque
def move_up(grid):
    for i in range(0,3,1):      #addition loop
        for j in range(4):
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] = 2 * grid[i][j]
                grid[i+1][j] = 0
            elif grid[i][j] == 0 and grid[i+1][j] != 0:
                grid[i][j] = grid[i+1][j]
                grid[i+1][j] = 0
    for j in range(4):          # remove extra 0 spaces using queues
        q = deque()
        for i in range(4):
            if grid[i][j] != 0:
                q.append(grid[i][j])
                grid[i][j] = 0
        for i in range(4):
            if len(q) == 0:
                grid[i][j] = 0
            else:
                grid[i][j] = q.popleft()
    return grid

def move_down(grid):
    
    for j in range(4):          # remove extra 0 spaces using queues
        q = deque()
        for i in range(3,-1,-1):
            if grid[i][j] != 0:
                q.append(grid[i][j])
                grid[i][j] = 0
        for i in range(3,-1,-1):
            if len(q) == 0:
                grid[i][j] = 0
            else:
                grid[i][j] = q.popleft()
    for i in range(3,0,-1):      #addition loop
        for j in range(4):
            if grid[i][j] == grid[i-1][j]:
                grid[i][j] = 2 * grid[i][j]
                grid[i-1][j] = 0
            elif grid[i][j] == 0 and grid[i-1][j] != 0:
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = 0
    return grid

def move_left(grid):
    for i in range(4):  # remove extra 0s
        q = deque()
        for j in range(4):
            if grid[i][j] != 0:
                q.append(grid[i][j])
                grid[i][j] = 0
        for j in range(4):
            if len(q) != 0:
                grid[i][j] = q.popleft()
            else:
                grid[i][j] = 0
    #printGrid(grid)
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] = 2*grid[i][j]
                grid[i][j+1] = 0
            elif grid[i][j] == 0 and grid[i][j+1] != 0:
                grid[i][j] = grid[i][j+1]
                grid[i][j+1] = 0
    return grid

def move_right(grid):
    for i in range(4):  # remove extra 0s
        q = deque()
        for j in range(3,-1,-1):
            if grid[i][j] != 0:
                q.append(grid[i][j])
                grid[i][j] = 0
        for j in range(3,-1,-1):
            if len(q) != 0:
                grid[i][j] = q.popleft()
            else:
                grid[i][j] = 0
    printGrid(grid)
    for i in range(4):
        for j in range(3,0,-1):
            if grid[i][j] == grid[i][j-1]:
                grid[i][j] = 2*grid[i][j]
                grid[i][j-1] = 0
            elif grid[i][j] == 0 and grid[i][j-1] != 0:
                grid[i][j] = grid[i][j-1]
                grid[i][j-1] = 0
    return grid

def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end ="")
            if j != len(grid[0]) - 1:
                print(end=" | ")
        print()
    print("")

def defineGrid():
    grid = [[4,2,8,4],
            [2,0,2,2],
            [0,0,0,2],
            [0,0,2,0]]
    return grid

if __name__ == "__main__":
    grid = defineGrid()
    printGrid(grid)
    grid = move_right(grid)
    printGrid(grid)