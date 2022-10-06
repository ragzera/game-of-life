import numpy as np
import matplotlib.pyplot as plt

GRID_ROWS = 50
GRID_COLS = 100

life_grid = np.zeros((GRID_ROWS, GRID_COLS), dtype=np.int8)

life_grid[0, 0] = 1
life_grid[0, 1] = 1
life_grid[5, 4] = 1
life_grid[6, 5] = 1

def step(grid):
    # Iterate over the grid, and update the grid
    # according to the rules of the game of life.
    # For now, we'll just return the grid as it is.
    out_grid = np.zeros((GRID_ROWS, GRID_COLS), dtype=np.int8)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                out_grid[i, np.mod(j+1,grid.shape[1]) ]  = 1

    return out_grid


while True:
    plt.imshow(life_grid, cmap='gray')
    plt.show()
    # time.sleep(0.5)
    life_grid = step(life_grid)
    plt.cla()