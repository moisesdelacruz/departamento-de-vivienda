from Tkinter import *
from toolbar import Toolbar

class Main(object):

    def __init__(self, root):
        self.root = root
        self.root.title('Home')
        self.root.geometry("800x700+300+300")
        tool = Toolbar(self.root)
        self.root.mainloop()



if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()
