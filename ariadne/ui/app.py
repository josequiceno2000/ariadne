from .maze_canvas import Point, Line, Window, Cell

def main():
    window = Window(800, 600)
    
    cell = Cell(30, 50, 300, 350, window)
    cell.draw("blue")

    cell2 = Cell(10, 400, 600, 210, window)
    cell2.draw("orange")

    window.wait_for_close()