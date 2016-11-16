try:
    import Tkinter as tk     ## Python 2.x
except ImportError:
    import tkinter as tk     ## Python 3.x
class DestroyTest():
    def __init__(self, top):
        self.top=top
        self.top.geometry("+10+10")
        self.frame=tk.Frame(self.top)
        self.frame.grid()
        test_label=tk.Label(self.frame, text="Label")
        test_label.grid(row=1, column=0)
        destroy_button=tk.Button(self.frame, text="Destroy Frame", \
                                 command=self.destroy)
        destroy_button.grid(row=10, column=0)
        exit_button=tk.Button(self.top, text="Exit", command=top.quit)
        exit_button.grid(row=10, column=0)
    def destroy(self):
        self.frame.destroy()
        self.new_toplevel=tk.Toplevel(self.top, takefocus=True)
        self.new_toplevel.geometry("+50+50")
        self.new_toplevel.grid()
        lbl=tk.Label(self.new_toplevel, text="New Toplevel")
        lbl.grid()
root=tk.Tk()
DT=DestroyTest(root)
root.mainloop()