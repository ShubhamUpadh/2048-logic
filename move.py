from collections import deque

class move_class:
    def __init__(self,grid):
        self.grid = grid
        self.orgGrid = [[val for val in row] for row in grid]
    
    def updateChangeGrid(self) -> list[list[int]]:
        self.orgGrid = [[val for val in row] for row in self.grid]
    
    def anyChange(self) -> bool:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid != self.orgGrid:
                    return True
        return False

    def updateGrid(self,grid):
        self.grid = [[x for x in y] for y in grid]
    
    def printGrid(self)->list[list[int]]:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                printVal = str(self.grid[i][j]) + " "*(4-len(str(self.grid[i][j])))
                print(printVal,end ="")
                if j != len(self.grid[0]) - 1:
                    print(end=" | ")
            print()
        print("")

        
    def move_up(self)->list[list[int]]:
        self.updateChangeGrid()     # update the dummy grid to current grid
        for j in range(4):          # remove extra 0 spaces using queues
            q = deque()
            for i in range(4):
                if self.grid[i][j] != 0:
                    q.append(self.grid[i][j])
                    self.grid[i][j] = 0
            for i in range(4):
                if len(q) == 0:
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = q.popleft()
        for i in range(0,3,1):      #addition loop
            for j in range(4):
                if self.grid[i][j] == self.grid[i+1][j]:
                    self.grid[i][j] = 2 * self.grid[i][j]
                    self.grid[i+1][j] = 0
                elif self.grid[i][j] == 0 and self.grid[i+1][j] != 0:
                    self.grid[i][j] = self.grid[i+1][j]
                    self.grid[i+1][j] = 0
        
        return [self.grid,self.anyChange()]

    def move_down(self)->list[list[int]]:
        self.updateChangeGrid()     # update the dummy grid to current grid
        for j in range(4):          # remove extra 0 spaces using queues
            q = deque()
            for i in range(3,-1,-1):
                if self.grid[i][j] != 0:
                    q.append(self.grid[i][j])
                    self.grid[i][j] = 0
            for i in range(3,-1,-1):
                if len(q) == 0:
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = q.popleft()
        for i in range(3,0,-1):      #addition loop
            for j in range(4):
                if self.grid[i][j] == self.grid[i-1][j]:
                    self.grid[i][j] = 2 * self.grid[i][j]
                    self.grid[i-1][j] = 0
                elif self.grid[i][j] == 0 and self.grid[i-1][j] != 0:
                    self.grid[i][j] = self.grid[i-1][j]
                    self.grid[i-1][j] = 0
        return [self.grid,self.anyChange()]

    def move_left(self)->list[list[int]]:
        self.updateChangeGrid()     # update the dummy grid to current grid
        for i in range(4):  # remove extra 0s
            q = deque()
            for j in range(4):
                if self.grid[i][j] != 0:
                    q.append(self.grid[i][j])
                    self.grid[i][j] = 0
            for j in range(4):
                if len(q) != 0:
                    self.grid[i][j] = q.popleft()
                else:
                    self.grid[i][j] = 0
        #printGrid(grid)
        for i in range(4):
            for j in range(3):
                if self.grid[i][j] == self.grid[i][j+1]:
                    self.grid[i][j] = 2*self.grid[i][j]
                    self.grid[i][j+1] = 0
                elif self.grid[i][j] == 0 and self.grid[i][j+1] != 0:
                    self.grid[i][j] = self.grid[i][j+1]
                    self.grid[i][j+1] = 0
        return [self.grid,self.anyChange()]

    def move_right(self)->list[list[int]]:
        self.updateChangeGrid()     # update the dummy grid to current grid
        for i in range(4):  # remove extra 0s
            q = deque()
            for j in range(3,-1,-1):
                if self.grid[i][j] != 0:
                    q.append(self.grid[i][j])
                    self.grid[i][j] = 0
            for j in range(3,-1,-1):
                if len(q) != 0:
                    self.grid[i][j] = q.popleft()
                else:
                    self.grid[i][j] = 0
        #printGrid(grid)
        for i in range(4):
            for j in range(3,0,-1):
                if self.grid[i][j] == self.grid[i][j-1]:
                    self.grid[i][j] = 2*self.grid[i][j]
                    self.grid[i][j-1] = 0
                elif self.grid[i][j] == 0 and self.grid[i][j-1] != 0:
                    self.grid[i][j] = self.grid[i][j-1]
                    self.grid[i][j-1] = 0
        return [self.grid,self.anyChange()]


if __name__ == "__main__":
    grid =  [[4,2,8,4],
                [2,0,2,2],
                [0,0,0,2],
                [0,0,2,0]]
    moveObj = move_class(grid)
    #grid = moveObj.defineGrid()
    moveObj.printGrid()
    grid,changeGrid = moveObj.move_right()
    moveObj.printGrid()
    print(changeGrid)