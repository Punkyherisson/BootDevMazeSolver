from tkinter import Tk, BOTH, Canvas

# --- Window Class ---
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Window")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
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
        self.__canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)

# --- Cell Class ---
class Cell:
    def __init__(self, win):
        # All walls exist by default (public members)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        # Boundaries for the cell on the canvas (set during draw)
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        # Reference to the Window (or canvas) to draw on
        self._win = win

    def draw(self, x1, y1, x2, y2):
        """Draw the cell's walls on the canvas using given coordinates."""
        self._x1, self._y1, self._x2, self._y2 = x1, y1, x2, y2
        # Draw left wall
        if self.has_left_wall:
            self._win.draw_line(x1, y1, x1, y2)
        # Draw top wall
        if self.has_top_wall:
            self._win.draw_line(x1, y1, x2, y1)
        # Draw right wall
        if self.has_right_wall:
            self._win.draw_line(x2, y1, x2, y2)
        # Draw bottom wall
        if self.has_bottom_wall:
            self._win.draw_line(x1, y2, x2, y2)

    def draw_move(self, to_cell, undo=False):
        """
        Draw a line connecting the centers of this cell and 'to_cell'.
        If undo is False, draw in red; if True, draw in gray.
        """
        # Compute center coordinates of self
        cx1 = (self._x1 + self._x2) / 2
        cy1 = (self._y1 + self._y2) / 2
        # Compute center coordinates of to_cell
        cx2 = (to_cell._x1 + to_cell._x2) / 2
        cy2 = (to_cell._y1 + to_cell._y2) / 2
        # Choose color based on undo flag
        color = "red" if not undo else "gray"
        # Draw a line connecting the centers with a width of 2 pixels
        self._win.draw_line(cx1, cy1, cx2, cy2, fill=color, width=2)

# --- Main Function for Testing ---
def main():
    win = Window(800, 600)
    cell_size = 100

    # Create two cells and draw them at different positions.
    # Cell A at (50, 50) to (150, 150)
    cellA = Cell(win)
    cellA.draw(50, 50, 50 + cell_size, 50 + cell_size)

    # Cell B at (250, 200) to (350, 300)
    cellB = Cell(win)
    cellB.draw(250, 200, 250 + cell_size, 200 + cell_size)

    # Draw a "move" from cellA to cellB (red line)
    cellA.draw_move(cellB, undo=False)
    # For demonstration, draw an "undo move" (gray line) back from cellB to cellA
    cellB.draw_move(cellA, undo=True)

    win.wait_for_close()

if __name__ == "__main__":
    main()