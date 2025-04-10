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

class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, window):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._top_left_point = Point(x1, y1)
        self._top_right_point = Point(x2, y1)
        self._bottom_right_point = Point(x2, y2)
        self._bottom_left_point = Point(x1, y2)
        self._center = Point(((x1 + x2) / 2), ((y1 + y2) / 2))
        self._win = window
    
    def draw(self, fill_color: str="black"):
        """Draws the cell if it is within the bounds of the canvas"""
        if self._win is None:
            return

        canvas_width = self._win._Window__canvas.winfo_width()
        canvas_height = self._win._Window__canvas.winfo_height()

        for point in [
            self._top_left_point,
            self._top_right_point,
            self._bottom_right_point,
            self._bottom_left_point
        ]:
            if not (0 <= point.x <= canvas_width and 0 <= point.y <= canvas_height):
                return

        if self.has_top_wall:
            top_wall = Line(self._top_left_point, self._top_right_point)
            self._win.draw_line(top_wall, fill_color)
        if self.has_right_wall:
            right_wall = Line(self._top_right_point, self._bottom_right_point)
            self._win.draw_line(right_wall, fill_color)
        if self.has_bottom_wall:
            bottom_wall = Line(self._bottom_right_point, self._bottom_left_point)
            self._win.draw_line(bottom_wall, fill_color)
        if self.has_left_wall:
            left_wall = Line(self._bottom_left_point, self._top_left_point)
            self._win.draw_line(left_wall, fill_color)
    
    def draw_move(self, to_cell, undo: bool=False):
        """Draws a line from the center of one cell to another"""
        center_line_color = {0: "red", 1: "gray"}[undo]
        center_line = Line(self._center, to_cell._center)
        self._win.draw_line(center_line, center_line_color)