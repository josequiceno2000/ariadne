from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas: Canvas, fill_color: str="black"):
        """Draws itself on the canvas"""
        canvas.create_line(
            self.point1.x, 
            self.point1.y, 
            self.point2.x, 
            self.point2.y, 
            fill=fill_color, 
            width=2
        )

class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Ariadne")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line: Line, fill_color: str="black"):
        """Draws a line on the canvas"""
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        """Sets root to run and redraws while running"""
        self.__running = True
        while self.__running:
            self.redraw()
    
    def redraw(self):
        """Redraws window while running"""
        self.__root.update_idletasks()
        self.__root.update()
    
    def close(self):
        """Closes the window"""
        self.__running = False



