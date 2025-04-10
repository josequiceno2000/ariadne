from ariadne.ui.maze_canvas import Window
from ariadne.core.cell import Point, Line, Cell
from ariadne.core.maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(100, 100, 10, 20, 40, 20, win)

    win.wait_for_close()