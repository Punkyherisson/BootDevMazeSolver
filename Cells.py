from tkinter import Tk, BOTH, Canvas

# --- Window Class ---
class Window:
    def __init__(self, width, height):
        # Create the main window (root widget) and set its title.
        self.__root = Tk()
        self.__root.title("Maze Window")
        
        # Create and pack a canvas to draw on.
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        
        # Running flag for the main loop.
        self.__running = False
        
        # Bind the close event.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, x1, y1, x2, y2, fill="black", width=2):
        """Helper method to draw a line on the canvas."""
        self.__canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)


# --- Cell Class ---
class Cell:
    def __init__(self, win):
        # By default, all walls exist.
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        # Placeholders for the cell's coordinate boundaries.
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        
        # Reference to the window so the cell can draw itself.
        self._win = win

    def draw(self, x1, y1, x2, y2):
        """Draw the cell on the canvas using the provided coordinates."""
        # Save coordinates.
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2
        
        # Draw left wall.
        if self.has_left_wall:
            self._win.draw_line(x1, y1, x1, y2)
        # Draw top wall.
        if self.has_top_wall:
            self._win.draw_line(x1, y1, x2, y1)
        # Draw right wall.
        if self.has_right_wall:
            self._win.draw_line(x2, y1, x2, y2)
        # Draw bottom wall.
        if self.has_bottom_wall:
            self._win.draw_line(x1, y2, x2, y2)


# --- Main Function for Testing ---
def main():
    # Create a window of 800x600 pixels.
    win = Window(800, 600)
    
    # Define a cell size for drawing (e.g., 100x100 pixels).
    cell_size = 100
    
    # Create and draw several cells with various wall configurations.
    # Cell 1: Default cell (all walls present)
    cell1 = Cell(win)
    cell1.draw(50, 50, 50 + cell_size, 50 + cell_size)
    
    # Cell 2: Remove the bottom wall.
    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell2.draw(200, 50, 200 + cell_size, 50 + cell_size)
    
    # Cell 3: Remove left and top walls.
    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.has_top_wall = False
    cell3.draw(50, 200, 50 + cell_size, 200 + cell_size)
    
    # Cell 4: Remove all walls.
    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.has_top_wall = False
    cell4.has_right_wall = False
    cell4.has_bottom_wall = False
    cell4.draw(200, 200, 200 + cell_size, 200 + cell_size)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()