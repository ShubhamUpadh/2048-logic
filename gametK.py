import tkinter as tk
from typing import List
import random
from move import move_class
from randomTile import generateRandom

cell_size = 80  # Define cell size
padding = 10  # Define padding

def generateRandomTile(grid: List[List[int]]) -> None:
    emptyCells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if emptyCells:
        randomCell = random.choice(emptyCells)
        randomCellValue = random.choices([2, 4], weights=[0.8, 0.2])[0]  # Access the first element of the choices list
        grid[randomCell[0]][randomCell[1]] = randomCellValue
    printGrid(grid)

def printGrid(grid: List[List[int]]) -> None:
    canvas.delete("all")
    for i in range(4):
        for j in range(4):
            x0 = j * cell_size + padding
            y0 = i * cell_size + padding
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill="lightgray", outline="black")
            canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(grid[i][j]), font=("Arial", 20, "bold"))

root = tk.Tk()
root.title("2048 Game")

title_label = tk.Label(root, text="2048 Game", font=("Arial", 20, "bold"))
title_label.pack()
canvas = tk.Canvas(root, width=4 * cell_size + 2 * padding, height=4 * cell_size + 2 * padding, bg="white")
canvas.pack()

def main():
    global firstMove
    if firstMove:
        grid = [ [0 for _ in range(4)] for _ in range(4) ]
        moveObj = move_class(grid)   # initialised the object using moveClass class
        genRandom = generateRandom(grid)
        grid = genRandom.generateRandomTileFirstChance()
        firstMove = not firstMove

    grid = moveObj.grid
    printGrid(grid)  # Print initial grid
    
    # Bind "Up" arrow key press event to moveUp function
    root.bind("<Up>", lambda event: moveObj.move_up())

    root.mainloop()

if __name__ == "__main__":
    firstMove = True
    main()