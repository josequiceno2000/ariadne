from .maze_canvas import Point, Line, Window, Cell

def main():
    window = Window(800, 600)
    
    cell = Cell(50, 50, 300, 400, window)
    cell.draw("red")

    cell2 = Cell(500, 40, 250, 300, window)
    cell2.draw("blue")

    cell.draw_move(cell2, True)

    window.wait_for_close()