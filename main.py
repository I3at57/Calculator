import tkinter as tk
from tkinter.constants import *
from const import *
import re

############################################################################

MEMORY = ""

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
    command=lambda: [
        update_memory('1'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_2 = tk.Button(
    frame_pad1, text='2', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('2'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_3 = tk.Button(
    frame_pad1, text='3', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('3'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_4 = tk.Button(
    frame_pad1, text='4', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('4'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_5 = tk.Button(
    frame_pad1, text='5', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('5'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_6 = tk.Button(
    frame_pad1, text='6', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('6'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_7 = tk.Button(
    frame_pad1, text='7', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('7'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_8 = tk.Button(
    frame_pad1, text='8', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('8'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_9 = tk.Button(
    frame_pad1, text='9', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('9'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_0 = tk.Button(
    frame_pad1, text='0', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('0'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_dot = tk.Button(
    frame_pad1, text='.', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('.'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_del = tk.Button(
    frame_pad1, text='<', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('D'),
        textVarSee.set(MEMORY)
    ]
)

# Define button pad2
button_pad_plus = tk.Button(
    frame_pad2, text='+', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('+'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_minus = tk.Button(
    frame_pad2, text='-', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('-'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_div = tk.Button(
    frame_pad2, text='/', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('/'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_mul = tk.Button(
    frame_pad2, text='x', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('x'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_egal = tk.Button(
    frame_pad2, text='=', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        computation(),
        textVarSee.set(MEMORY),
        update_memory('E')
    ]
)
button_pad_erase = tk.Button(
    frame_pad2, text='CE', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('E'),
        textVarSee.set(MEMORY)
    ]
)
button_pad_lparent = tk.Button(
    frame_pad2, text='(', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory('('),
        textVarSee.set(MEMORY)
    ]
)
button_pad_rparent = tk.Button(
    frame_pad2, text=')', height=3, width=5, background="#282c34",
    foreground="white", font="Helvetica 15",
    command=lambda: [
        update_memory(')'),
        textVarSee.set(MEMORY)
    ]
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


def solve_one_operation(phrase):
    """
    Solve a one operation from a string such as : '4.25*9'
    """

    if '+' in phrase:
        operator = '+'
        variables = phrase.split(operator)
        return(str(float(variables[0]) + float(variables[1])))
    elif '-' in phrase:
        operator = '-'
        variables = phrase.split(operator)
        return(str(float(variables[0]) - float(variables[1])))
    elif 'x' in phrase:
        operator = 'x'
        variables = phrase.split(operator)
        return(str(float(variables[0]) * float(variables[1])))
    elif '/' in phrase:
        operator = '/'
        variables = phrase.split(operator)
        return(str(float(variables[0]) / float(variables[1])))
    else:
        return 1


def computation():
    """
    Take MEMORY and compute a result to put in MEMORY
    """

    global MEMORY

    # values traitment
    data = re.sub('(?P<val>[0-9.])\\(', '\\g<val>x(', MEMORY)
    data = re.sub('\\)(?P<val>[0-9])', ')x\\g<val>', data)
    data = re.sub('\\)\\(', ')x(', data)
    data = re.sub('^-', '0-', data)
    if data.count('(') + data.count(')') == 2:
        data = re.sub('^\\((?P<val>.*)\\)$', '\\g<val>', data)
    print(MEMORY, 'MEMORY')
    print(data, 'data')

    # Check test
    if data.count('(') != data.count(')'):  # Bad closing parenthesis
        MEMORY = 'ERROR'
        return 1
    else:
        numbers = re.findall('[0-9.]+', data)
        if numbers == []:   # No numbers enter
            MEMORY = ''
            return 1
        else:
            for i in numbers:
                if i.count('.') > 1:    # Some number with double dot
                    MEMORY = 'ERROR'
                    return 1
        ddo = re.findall('[\\/x\\-\\+]{2}', data)
        if ddo != []:   # Consecutive operator
            MEMORY = 'ERROR'
            return 1
        nbrOperator = data.count('+') + data.count('-') + \
            data.count('x') + data.count('/')
        if nbrOperator == 0:    # No operator
            MEMORY = data
            return 1

    compt = 1
    while re.fullmatch('-?[0-9.]+', data) is None or compt == 1:
        compt = 0
        print(data.count('(') + data.count(')'))
        # Réduit les multiplications
        operation = re.findall('[0-9.]+x[0-9.]+', data)
        while operation != []:
            for opp in operation:
                res = solve_one_operation(opp)
                data = re.sub(opp, res, data)
            operation = re.findall('[0-9.]+x[0-9.]+', data)

        # Réduit les divisions
        operation = re.findall('[0-9.]+/[0-9.]+', data)
        while operation != []:
            for opp in operation:
                res = solve_one_operation(opp)
                data = re.sub(opp, res, data)
            operation = re.findall('[0-9.]+/[0-9.]+', data)

        # Réduit les soustractions
        operation = re.findall('[0-9.]+-[0-9.]+', data)
        while operation != []:
            for opp in operation:
                res = solve_one_operation(opp)
                data = re.sub(opp, res, data)
            operation = re.findall('[0-9.]+-[0-9.]+', data)

        # Réduit les additions
        operation = re.findall("[0-9.]+\\+[0-9.]+", data)
        while operation != []:
            for opp in operation:
                res = solve_one_operation(opp)
                opp = re.sub('\\+', '\\\\+', opp)
                data = re.sub(opp, res, data)
            operation = re.findall("[0-9.]+\\+[0-9.]+", data)

        # Gère les cas de 3(-2)
        data = re.sub(
            '(?P<val1>[0-9.]+)x\\(-(?P<val2>[0-9.]+)\\)',
            '0-\\g<val2>x\\g<val1>',
            data
        )

        # gère les cas de (2.36)
        data = re.sub('\\((?P<val>[0-9.]+)\\)', '\\g<val>', data)

    print(data, 'FInal')

    MEMORY = data


def update_memory(ele):
    """
    Change the value inside the MEMORY array
    """
    global MEMORY   # get the global value of MEMORY

    # Erase the Memory
    if ele == 'E':
        MEMORY = ""
    elif ele == 'D':
        MEMORY = MEMORY[:-1]
    else:
        MEMORY = MEMORY + ele


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
    button_pad_del.grid(row=3, column=0)

    button_pad_plus.grid(row=0, column=3)
    button_pad_minus.grid(row=1, column=3)
    button_pad_mul.grid(row=2, column=3)
    button_pad_div.grid(row=3, column=3)

    button_pad_erase.grid(row=0, column=4)
    button_pad_lparent.grid(row=1, column=4)
    button_pad_rparent.grid(row=2, column=4)
    button_pad_egal.grid(row=3, column=4)

    label_display.pack(side='right', fill='both')

    return 0

############################################################################


if __name__ == '__main__':
    packall()
    root.resizable(0, 0)
    root.mainloop()
