import tkinter as tk
import ttkbootstrap as ttk

convertVar = 1

def convert():
    if convertVar:
        mile_input = entry_int.get()
        km_output = mile_input * 1.61
        output_string.set(str(round(km_output, 2)) + " km")
    else:
        km_input = entry_int.get()
        miles_output = km_input / 1.61
        output_string.set(str(round(miles_output, 2)) + " miles")


def set():
    title_string.set("Miles to Kilometers")
    text_string.set("Miles")

def flip():
    global convertVar

    if convertVar:
        title_string.set("Kilometers to Miles")
        text_string.set("Kilometers")
        output_string.set("0 miles")
    else:
        title_string.set("Miles to Kilometers")
        text_string.set("Miles")
        output_string.set("0 km")
    
    convertVar = 0 if convertVar else 1

# Window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("400x200")

# Title
title_string = tk.StringVar()
title_label = ttk.Label(
    master = window, 
    font="Calibri 24 bold", 
    textvariable = title_string)
title_label.pack(pady  = 10)

# Input
input_frame = ttk.Frame(master = window)

text_string = tk.StringVar()
text_label = ttk.Label(master = input_frame, textvariable = text_string )

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = "Convert", command = convert)

text_label.pack(side = "left")
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack()

# Output
output_string = tk.StringVar()
output_string.set("0 km")
output_label = ttk.Label(
    master = window, 
    text = "Output", 
    font = "Calibri 24", 
    textvariable = output_string)
output_label.pack(pady = 10)


# Flip
flip_button = ttk.Button(master = window, text = "Flip", command = flip)
flip_button.pack(pady = 10)

# Run
set()
window.mainloop()