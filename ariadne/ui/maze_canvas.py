from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Ariadne")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        """Redraws window while running"""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Sets root to run and redraws while running"""
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        """Closes the window"""
        self.__running = False


