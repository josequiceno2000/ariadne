from ariadne.core.cell import Point, Line, Cell
from ariadne.ui.maze_canvas import Window
import time

class Maze:
    def __init__(
            self,
            x1: int,
            y1: int,
            num_rows: int,
            num_cols: int,
            cell_size_x: int,
            cell_size_y: int,
            win: Window,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        
    
    def _create_cells(self):
        self._cells = []
        col_num = 1
        for i in range(self.num_cols):
            cell_column = []
            row_num = 1
            for j in range (self.num_rows):
                next_cell = Cell(
                    self.x1 + (self.cell_size_x * (col_num - 1)), 
                    self.y1 + (self.cell_size_y * (row_num - 1)), 
                    self.x1 + (self.cell_size_x * col_num), 
                    self.y1 + (self.cell_size_y * row_num), 
                    self._win)
                cell_column.append(next_cell)
                row_num += 1
            self._cells.append(cell_column)
            col_num += 1
        
        for cell_column in self._cells:
            for cell in cell_column:
                self._draw_cell(cell)
    
    def _draw_cell(self, cell: Cell):
        cell.draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.04)