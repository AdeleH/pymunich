#!/usr/bin/bash

import numpy as np
from IPython.display import display, clear_output, HTML
import time

class GameOfLife:
    ''' This class uses:
    - numpy library for the representation of the grid,
    - time for the simulation,
    - IPython for the visualization / interface.
    '''        
        
    def __init__(self, rows, cols):
        self.grid = np.random.random_integers(0, 1, size=(rows, cols))
        
    def isAlive(self, alive, neightbours):
        ''' Utility method '''
        if (neightbours == 3):
            return 1
        if (alive & (neightbours == 2)):
            return 1
        return 0
            
    def nextgen(self, cells):
    ''' It calculates the next iteration. '''
        res = cells*0 # copy of the array
        for row in range(cells.shape[0]):
            for col in range(cells.shape[1]):
                alive = cells[row,col] 
                neighbours = np.sum((cells[max(0,row-1):row+2,max(0, col-1):col+2]).flatten())
                res[row, col] = self.isAlive(alive, neighbours - alive)
        return res
    
    def custom(self, grid, oldGrid):
    ''' Display the grid. '''
        lightgray = ("<td style='border: 1px solid black; background: lightgray;"
                 "width: 1px; height: 1px'></td>")
        darkgray = ("<td style='border: 1px solid black; background: darkgrey;"
                 "width: 1px; height: 1px'></td>")
        black = ("<td style='border: 1px solid black; background: black;"
                 "width: 1px; height: 1px'></td>")
        white = ("<td style='border: 1px solid black; background: white;"
                 "width: 1px; height: 1px'></td>")
        table = ""
        for i in range(0, grid.shape[0]):
            row = ""
            for j in range(0, grid.shape[1]):
                if (grid[i][j] == 1) and (oldGrid[i][j] == 0):
                    row += darkgray
                elif (grid[i][j] == 0) and (oldGrid[i][j] == 1):
                    row += lightgray
                else:
                    row += black if grid[i][j] else white
            table += "<tr>{row}</tr>".format(row=row)    
        clear_output()
        display(HTML("<table>{table}</table>".format(table=table)))
        
    def play(self, iterations):
    ''' Animation '''
        arr = self.grid # initialization
        for i in range(0, iterations):
            tmp = self.nextgen(arr)
            self.custom(arr, tmp)
            arr = tmp
            time.sleep(.5)

game = GameOfLife(50, 50) # 50x50 grid
game.play(500) # let's play, n iterations
