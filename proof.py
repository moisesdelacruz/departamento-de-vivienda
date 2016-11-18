import Tkinter as tk

root = tk.Tk()
f = tk.Frame(root, width=1000, height=100, bg="blue")
f.pack(fill=tk.X, expand=True)
f.pack_propagate(0)
l = tk.Label(f, text="hi", width=10, bg="red", fg="white")
l.pack()

root.mainloop()