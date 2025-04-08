from .maze_canvas import Window, Point, Line

def main():
    window = Window(800, 600)
    point1 = Point(40, 60)
    point2 = Point(400, 500)
    line = Line(point1, point2)
    window.draw_line(line, fill_color="pink")
    window.wait_for_close()