from .maze_canvas import Window
from ariadne.core.cell import Point, Line, Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(50, 50, 100, 100, win)
    c1.has_right_wall = False
    c1.draw()

    c2 = Cell(100, 50, 150, 100, win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw()

    c1.draw_move(c2)

    c3 = Cell(100, 100, 150, 150, win)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw()

    c2.draw_move(c3)

    c4 = Cell(150, 100, 200, 150, win)
    c4.has_left_wall = False
    c4.draw()

    c3.draw_move(c4, True)

    win.wait_for_close()