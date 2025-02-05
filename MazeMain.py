from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        # Fenetre Principale
        self.__root = Tk()
        self.__root.title("My Tkinter Window")
        
        # Creation d'un Canevas
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        
        # Condition de la boucle
        self.__running = False
        
        # Capturer l'evenement de fermeture de la fenetre
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """Maj de l'écran"""
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """Tant qu'on a pas fermé on affiche"""
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        """Si on ferme, on arrete"""
        self.__running = False

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()