from tkinter import Tk, BOTH, Canvas

# --- Window Class ---
class Window:
    def __init__(self, width, height):
        # Create root widget and set window title
        self.__root = Tk()
        self.__root.title("Tkinter Window")
        
        # Create and pack the Canvas widget
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        
        # Flag to indicate whether the window is running
        self.__running = False
        
        # Bind the window close event to the close() method
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Redraw the window by processing pending tasks and updating the display."""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Run a loop that continues until the window is closed."""
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        """Set running to False to exit the main loop and close the window."""
        self.__running = False

    def draw_line(self, line, fill_color):
        """Call the given line's draw() method to draw it on the canvas."""
        line.draw(self.__canvas, fill_color)


# --- Point Class ---
class Point:
    def __init__(self, x, y):
        # x and y are public data members
        self.x = x
        self.y = y


# --- Line Class ---
class Line:
    def __init__(self, p1, p2):
        # Save the two endpoints as data members
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        """Draw the line on the given canvas with the specified fill color."""
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y,
                             fill=fill_color, width=2)


# --- Main Function to Test the Classes ---
def main():
    # Create a window of size 800x600 pixels
    win = Window(800, 600)
    
    # Define four points forming a square
    p1 = Point(100, 100)
    p2 = Point(300, 100)
    p3 = Point(300, 300)
    p4 = Point(100, 300)
    
    # Create lines connecting the points in order
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)
    
    # Draw the lines with different colors using Window.draw_line()
    win.draw_line(line1, "red")
    win.draw_line(line2, "green")
    win.draw_line(line3, "blue")
    win.draw_line(line4, "black")
    
    # Wait for the window to be closed
    win.wait_for_close()

if __name__ == "__main__":
    main()