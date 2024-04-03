class gameEndConditions:
    
    def __init__(self) -> None:
        self.maxTile = None
        self.allFilled = False
        self.gameWin = False
        self.gameConditionsDict = {
            100 : "You Win !!!!",
            200 : "You Lose !!!!",
            300 : "Continuation Code"
        }
    
    def maxTileValue(self,grid):
        self.maxTile = float("-inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.maxTile = max(self.maxTile,grid[i][j])
                if self.maxTile == 2048:
                    self.gameWin = True
                    break
    
    def allFilledValue(self,grid):
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    flag = True
                    break
        self.allFilled = not flag

    def executionLogic(self,grid):
        self.maxTileValue(grid)
        self.allFilledValue(grid)

        if self.gameWin:
            return 100  # code for winning the game
        if self.allFilled:
            return 200  # code for losing the game
        return 300      # code for continuing the game


    
