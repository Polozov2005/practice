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
for index in [0, 1, 2]:
    root.rowconfigure(index=index, weight=1)

graph_frame = ttk.LabelFrame(root, text="График функции u(t)", padding=(20, 10))
graph_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew", rowspan=3
)

conditions_frame = ttk.LabelFrame(root, text="Начальные условия", padding=(20, 10))
conditions_frame.grid(
    row=0, column=1, padx=10, pady=(20, 10), sticky="nsew"
)
for index in range(5):
    conditions_frame.rowconfigure(index=index, weight=1)


solve_frame = ttk.LabelFrame(root, text="Решить", padding=(20, 10))
solve_frame.grid(
    row=1, column=1, padx=10, pady=(20, 10), sticky="nsew"
)

answer_frame = ttk.LabelFrame(root, text="Ответ", padding=(20, 10))
answer_frame.grid(
    row=2, column=1, padx=10, pady=(20, 10), sticky="nsew"
)



equation_u_frame = ttk.Frame(conditions_frame)
equation_u_frame.grid(
    row=0, column=0, padx=10, pady=(20, 10), sticky="nsew"
)
equation_u_label = ttk.Label(equation_u_frame, text ="u(t) = sincos schkibididopeeyes")
equation_u_label.grid(
    row=0, column=0, sticky='nsew'
)

equation_U_frame = ttk.Frame(conditions_frame)
equation_U_frame.grid(
    row=1, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
equation_U_label = ttk.Label(equation_U_frame, text ="U = integral(U_0foisdjfsjdfl)")
equation_U_label.grid(
    row=0, column=0, sticky='nsew'
)

f_frame = ttk.Frame(conditions_frame)
f_frame.grid(
    row=2, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
f_label = ttk.Label(f_frame, text="f = ")
f_label.grid(
    row=0, column=0, sticky='nsew'
)
f_entry = ttk.Entry(f_frame)
f_entry.grid(
    row=0, column=1, sticky='nsew'
)
f_unit_label = ttk.Label(f_frame, text="Гц")
f_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

U_frame = ttk.Frame(conditions_frame)
U_frame.grid(
    row=3, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
U_label = ttk.Label(U_frame, text="U = ")
U_label.grid(
    row=0, column=0, sticky='nsew'
)
U_entry = ttk.Entry(U_frame)
U_entry.grid(
    row=0, column=1, sticky='nsew'
)
U_unit_label = ttk.Label(U_frame, text="В")
U_unit_label.grid(
    row=0, column=2, sticky='nsew'
)

optionmenu_frame = ttk.Frame(conditions_frame)
optionmenu_frame.grid(
    row=4, column=0, padx=10, pady=(20, 10), sticky='nsew'
)
optionmenu_list = ["", "Решение встроенной функцией", "Решение реализованной функцией"]
optionmenu_var = tk.StringVar(value=optionmenu_list[1])
optionmenu = ttk.OptionMenu(
    optionmenu_frame, optionmenu_var, *optionmenu_list
)
optionmenu.grid(
    row=0, column=0, sticky='nsew'
)

root.update()
x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

root.mainloop()