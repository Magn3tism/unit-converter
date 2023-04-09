import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")
# window.attributes('-type', 'dialog')

# Title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font="Calibri 24 bold")
title_label.pack(pady  = 10)

# Input
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = "Convert")

entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack()

# Output
output_label = ttk.Label(master = window, text = "Output", font = "Calibri 24")
output_label.pack(pady = 10)

# Run
window.mainloop()