import tkinter as tk
from tkinter.constants import *
from const import *

###############################################################################

root = tk.Tk()

frame_display = tk.Frame(
    root, background="#282c34", height=100, width=500, borderwidth=5,
    relief=RIDGE
)
frame_button = tk.Frame(
    root, background="#282c34", height=500, width=500, borderwidth=5,
    relief=RIDGE
)
frame_button_pad = tk.Frame(
    frame_button, background="#282c34", height=500, width=350
)
frame_button_action = tk.Frame(
    frame_button, background="#282c34", height=500, width=150
)

button_pad_1 = tk.Button(
    frame_button_pad, text='1', height=5, width=5
)


def packall():
    frame_display.pack()
    frame_button.pack()
    frame_button_pad.pack(side='left')
    frame_button_action.pack(side='left')

    button_pad_1.pack()


if __name__ == '__main__':
    packall()
    root.geometry("510x610")
    root.re
    root.mainloop()
