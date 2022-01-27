import tkinter as tk
from tkinter.constants import *
from const import *

############################################################################

DISPLAY = []

############################################################################

# Define the main window of the app
root = tk.Tk()

# Define all frame
frame_display = tk.Frame(
    root, background="#282c34", height=200, width=500, borderwidth=5,
    relief=RIDGE
)
frame_button = tk.Frame(
    root, background="#282c34", height=500, width=500, borderwidth=5,
    relief=RIDGE
)
frame_pad1 = tk.Frame(
    frame_button, background="#282c34", borderwidth=2, relief=RIDGE
)
frame_pad2 = tk.Frame(
    frame_button, background="#282c34", borderwidth=2, relief=RIDGE
)

# Define button pad 1
button_pad_1 = tk.Button(
    frame_pad1, text='1', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('1')
)
button_pad_2 = tk.Button(
    frame_pad1, text='2', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('2')
)
button_pad_3 = tk.Button(
    frame_pad1, text='3', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('3')
)
button_pad_4 = tk.Button(
    frame_pad1, text='4', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('4')
)
button_pad_5 = tk.Button(
    frame_pad1, text='5', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('5')
)
button_pad_6 = tk.Button(
    frame_pad1, text='6', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('6')
)
button_pad_7 = tk.Button(
    frame_pad1, text='7', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('7')
)
button_pad_8 = tk.Button(
    frame_pad1, text='8', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('8')
)
button_pad_9 = tk.Button(
    frame_pad1, text='9', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('9')
)
button_pad_0 = tk.Button(
    frame_pad1, text='0', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('0')
)
button_pad_dot = tk.Button(
    frame_pad1, text='.', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('.')
)

# Define button pad2
button_pad_plus = tk.Button(
    frame_pad2, text='+', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('+')
)
button_pad_minus = tk.Button(
    frame_pad2, text='-', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('-')
)
button_pad_div = tk.Button(
    frame_pad2, text='/', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('/')
)
button_pad_mul = tk.Button(
    frame_pad2, text='x', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display('*')
)
button_pad_egal = tk.Button(
    frame_pad2, text='=', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display(mod='A')
)
button_pad_erase = tk.Button(
    frame_pad2, text='CE', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: update_display(mod='E')
)

# Define le Label
textVarSee = tk.StringVar()
textVarSee.set('')
label_display = tk.Label(
    frame_display,
    textvariable=textVarSee,
    font="Helvetica 15", background="#282c34", foreground="white"
)

############################################################################


def update_display(ele='', mod='W'):
    """
    Update the DISPLAY array and the current display of the app
    """

    global DISPLAY

    # to errase
    if mod == 'E':
        DISPLAY = []
        textVarSee.set('')
        return 0
    # to add element
    elif mod == 'W':
        DISPLAY.append(str(ele))    # add the element to the display array
        chaine = ""
        for i in DISPLAY:
            chaine = chaine + i
        textVarSee.set(chaine)
        return 0
    # to du the calculation
    elif mod == 'A':
        # get the string
        chaine = ""
        for i in DISPLAY:
            chaine = chaine + i

        if '+' in chaine:
            delimiter = '+'
            numbers = chaine.split(sep=delimiter)
            chaine = str(float(numbers[0]) + float(numbers[1]))
            textVarSee.set(chaine)
            DISPLAY = []
        elif '-' in chaine:
            delimiter = '-'
            numbers = chaine.split(sep=delimiter)
            chaine = str(float(numbers[0]) - float(numbers[1]))
            textVarSee.set(chaine)
            DISPLAY = []
        elif '/' in chaine:
            delimiter = '/'
            numbers = chaine.split(sep=delimiter)
            chaine = str(float(numbers[0]) / float(numbers[1]))
            textVarSee.set(chaine)
            DISPLAY = []
        elif '*' in chaine:
            delimiter = '*'
            numbers = chaine.split(sep=delimiter)
            chaine = str(float(numbers[0]) * float(numbers[1]))
            textVarSee.set(chaine)
            DISPLAY = []
        else:
            textVarSee.set(chaine)
            DISPLAY = []
        return 0
    else:
        return 1


def packall():
    """
    Pack all the element as the startup state
    """
    frame_display.pack(side='top', fill='both')
    frame_button.pack(side='top', fill='both')
    frame_pad1.pack(side='left')
    frame_pad2.pack(side='left')

    button_pad_1.grid(row=2, column=0)
    button_pad_2.grid(row=2, column=1)
    button_pad_3.grid(row=2, column=2)
    button_pad_4.grid(row=1, column=0)
    button_pad_5.grid(row=1, column=1)
    button_pad_6.grid(row=1, column=2)
    button_pad_7.grid(row=0, column=0)
    button_pad_8.grid(row=0, column=1)
    button_pad_9.grid(row=0, column=2)
    button_pad_0.grid(row=3, column=1)

    button_pad_dot.grid(row=3, column=2)

    button_pad_plus.grid(row=0, column=3)
    button_pad_minus.grid(row=1, column=3)
    button_pad_mul.grid(row=2, column=3)
    button_pad_div.grid(row=3, column=3)

    button_pad_erase.grid(row=0, column=4)
    button_pad_egal.grid(row=3, column=4)

    label_display.pack(side='right', fill='both')

    return 0

############################################################################


if __name__ == '__main__':
    packall()
    root.resizable(0, 0)
    root.mainloop()
