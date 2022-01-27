import tkinter as tk
from tkinter.constants import *
from const import *

###############################################################################

# Our main root container
root = tk.Tk()

# frame
frame_button = tk.Frame(
    root, relief=RIDGE, background=FRAME_BUTTON_COLOR,
    height=FRAME_BUTTON_HEIGHT, width=FRAME_BUTTON_WIDTH,
    borderwidth=FRAME_BUTTON_BORDERWIDTH
)
frame_menu = tk.Frame(
    root, relief=RIDGE, height=FRAME_MENU_HEIGHT, width=FRAME_MENU_WIDTH
)
frame_display = tk.Frame(
    root, relief=RIDGE, background=FRAME_DISPLAY_COLOR,
    height=FRAME_DISPLAY_HEIGHT, width=FRAME_DISPLAY_WIDTH,
    borderwidth=FRAME_DISPLAY_BORDERWIDTH
)


# Menu button
button_File = tk.Button(frame_menu, text="File")
button_Edit = tk.Button(frame_menu, text="Edit")
button_Help = tk.Button(frame_menu, text="Help")

# astction button
button_0 = tk.Button(frame_button, text='0')
button_1 = tk.Button(frame_button, text='1')
button_2 = tk.Button(frame_button, text='2')
button_3 = tk.Button(frame_button, text='3')
button_4 = tk.Button(frame_button, text='4')
button_5 = tk.Button(frame_button, text='5')
button_6 = tk.Button(frame_button, text='6')
button_7 = tk.Button(frame_button, text='7')
button_8 = tk.Button(frame_button, text='8')
button_9 = tk.Button(frame_button, text='9')


###############################################################################

def packall():
    # Pakc frame
    frame_menu.pack(side='top')
    frame_display.pack(side='top')
    frame_button.pack(side='top')

    # Pack Menu
    button_File.pack(side='left')
    button_Edit.pack(side='left')
    button_Help.pack(side='left')

    # Pack button
    """
    button_1.pack()
    button_2.pack()
    button_3.pack()
    button_4.pack()
    button_5.pack()
    button_6.pack()
    button_7.pack()
    button_8.pack()
    button_9.pack()
    """


def main():
    packall()
    root.title('Calculator')
    root.resizable(0, 0)
    root.mainloop()

###############################################################################


if __name__ == '__main__':
    main()
