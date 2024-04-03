from collections import deque

class move_class:
    def __init__(self,grid):
        self.grid = grid

    def updateGrid(self,grid):
        self.grid = grid
    
    def printGrid(self)->list[list[int]]:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j],end ="")
                if j != len(self.grid[0]) - 1:
                    print(end=" | ")
            print()
        print("")

        
    def move_up(self)->list[list[int]]:
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
        
        return self.grid

    def move_down(self)->list[list[int]]:
        
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
        return self.grid

    def move_left(self)->list[list[int]]:
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
        return self.grid

    def move_right(self)->list[list[int]]:
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
        return self.grid


if __name__ == "__main__":
    grid =  [[4,2,8,4],
                [2,0,2,2],
                [0,0,0,2],
                [0,0,2,0]]
    moveClass = move_class(grid)
    grid = moveClass.defineGrid()
    moveClass.printGrid()
    grid = moveClass.move_right()
    moveClass.printGrid()