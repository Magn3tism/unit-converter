import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")
# window.attributes('-type', 'dialog')

# Title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font="Calibri 24")
title_label.pack()


# Run
window.mainloop()