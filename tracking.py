#!/usr/bin/env python
import tracker
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, Text
import os



root = tk.Tk()
root.resizable(width=False, height=False)
canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")


part_Entry = tk.Entry(root)
part_label = tk.Label(root, text="part name", bg="gray")

price_Entry = tk.Entry(root)
price_label = tk.Label(root, text="Price", bg="gray")

URL_Entry = tk.Entry(root)
URL_label = tk.Label(root, text="URL", bg="gray")

part_label.place(relx=.1, rely=.2)
part_Entry.place(width=200, relx=.3, rely=.2)

price_label.place(relx=.1, rely=.3)
price_Entry.place(width=200, relx=.3, rely=.3)

URL_label.place(relx=.1, rely=.4)
URL_Entry.place(width=200, relx=.3, rely=.4)

def track():
    try:
        while (True):
            tracker.amazon_tracker(part_Entry.get(), int(price_Entry.get()), URL_Entry.get())
            time.sleep(21600)
    except:
        messagebox.showinfo("error", "Please try again")

button = tk.Button(root, text='Enter', command=track, pady=5 )
button.place(relx=.5, rely=.6)

canvas.pack()

root.mainloop()




