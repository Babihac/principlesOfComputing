"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
start_index = {UP:0, DOWN:3, LEFT:0, RIGHT:3}

def no_zero(i):
    if i != 0:
        return True
    return False
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    arr = filter(no_zero, line)
    diff = len(line) - len(arr)
    i = 0
    while i < diff:
        arr.append(0)
        i += 1
    for i in range(len(line)-1):
        if arr[i] == arr[i+1]:
            arr[i] *= 2
            arr[i+1] = 0
    arr = filter(no_zero, arr)
    diff = len(line) - len(arr)
    i = 0
    while i < diff:
        arr.append(0)
        i += 1
    return arr
def traverse_grid(grid, start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction
    
    Both start_cell is a tuple(row, col) denoting the
    starting cell
    
    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    res = []
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        res.append(grid[row][col])
    return res
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset
        self.has_change = False
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.grid_width)]
                    for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
    def update_line(self,line,start_cell, direction):
        arr = merge(line)
        for step in range(4):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            if self.grid[row][col] != arr[step]:
                self.grid[row][col] = arr[step]
                self.has_change = True


    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self.has_change = False
        if direction <=2:
            for i in range(self.grid_width):
                arr = traverse_grid(self.grid,[start_index[direction],i],OFFSETS[direction],self.grid_height)
                self.update_line(arr,[start_index[direction],i],OFFSETS[direction])
        else:
            for i in range(self.grid_width):
                arr = traverse_grid(self.grid,[i,start_index[direction]],OFFSETS[direction],self.grid_height)
                self.update_line(arr,[i,start_index[direction]],OFFSETS[direction])
        if self.has_change:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        row_index = random.randrange(self.grid_height)
        col_index = random.randrange(self.grid_width)
        while self.grid[row_index][col_index] != 0:
            row_index = random.randrange(self.grid_height)
            col_index = random.randrange(self.grid_width)
        num = random.randrange(10)
        if num == 0:
            self.set_tile(row_index, col_index,4)
        else:
             self.set_tile(row_index, col_index,2)
            

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
