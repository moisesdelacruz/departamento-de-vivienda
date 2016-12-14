import Tkinter as tk
import ttk

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="#CCC")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = ttk.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=10, style='Grey10.TLabel')
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)