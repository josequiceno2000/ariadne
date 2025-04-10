from ariadne.core.cell import Cell
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
        self._cells = []
        self._win = win
        self._create_cells()
        self._draw()
        
    
    def _create_cells(self):
        for col in range(self.num_cols):
            cell_column = []
            for row in range (self.num_rows):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell_column.append(Cell(x1, y1, x2, y2, self._win))
            self._cells.append(cell_column)
        
    def _draw(self):
        for cell_column in self._cells:
            for cell in cell_column:
                cell.draw()
                self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.04)