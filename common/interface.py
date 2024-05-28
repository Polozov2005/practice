import tkinter as tk
from tkinter import ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.title("")
root.geometry("1600x900")
root.resizable(False, False)

# Задание темы
root.tk.call("source", "common/azure.tcl")
root.tk.call("set_theme", "dark")

for index in [0, 1]:
    root.columnconfigure(index=index, weight=1)
root.rowconfigure(index=0, weight=1)

graph_frame = ttk.LabelFrame(root, text="График функции u(t)", padding=(20, 10))
graph_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew"
)

graph_checkbutton = ttk.Checkbutton(
    graph_frame, text="Unchecked", variable=None
)
graph_checkbutton.grid(row=0, column=0, padx=0, pady=0)



widgets_frame = ttk.LabelFrame(root, text="Widgets", padding=(20, 10))
widgets_frame.grid(
    row=0, column=1, padx=10, pady=(20, 10), sticky="nsew"
)




root.update()
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

root.mainloop()