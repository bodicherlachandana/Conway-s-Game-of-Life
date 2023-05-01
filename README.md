# Conway's Game of Life

Conway's game of life is a cellular automation created by John Conway. It is a zero player game, which means the evolution is determined by its initial state, no further input is required. The game is built on a grid of nine squares, every cell has 8 neighbouring cells


GAME RULES

1. If a cell is considered to be alive, if it is having two or three living cells as neighbours around it, it continues living.

2. If a cell is considered to be alive, if it is having less than two living cells around it, it is considerd to be dead.

3. If a cell is considered to be alive, if it is having more than three living cells as neighbours, due to overpopulation it is considered to be dead.

4. If a cell is considerd to be dead, if it is having two or three living cells as neighbours around it, it survives.


APPROACH

1. Initialize the cells in the grid.

2. At each time if simulation , for each cell in grid, updating value according to neighbours.
