import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")
# window.attributes('-type', 'dialog')

# Title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font="Calibri 24 bold")
title_label.pack()

# Input
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = "Convert")

entry.pack()
button.pack()
input_frame.pack()

# Run
window.mainloop()