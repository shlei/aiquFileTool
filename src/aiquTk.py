from tkinter import *

from tkinter import W as Left
from tkinter import E as Right

def mkTk(title, width, height):
    master = Tk()
    master.title(title)
    master.grid(baseWidth=1, baseHeight=1, widthInc=width, heightInc=height)

    return master


def mkButton(master, name, row, column, fun, *funArgs):
    mybutton = Button(master, text=name, command=lambda: fun(*funArgs), width=10)
    mybutton.grid(row=row, column=column, pady=4, padx=15)

    return mybutton


def mkLable(master, text, row, column, sticky=Right, val=None):
    mylabel = Label(master, text=text, textvariable=val)
    mylabel.grid(row=row, column=column, sticky=sticky, pady=4, padx=10)

    return mylabel


def mkEntry(master, var, size, row, column, columnspan):
    myentry = Entry(master, textvariable=var, width=size)
    myentry.grid(row=row, column=column, columnspan=columnspan, pady=4, padx=10)

    return myentry


def mkCkButton(master, text, var, row, column, isSelect):
    myCkButton = Checkbutton(master, text=text, variable=var)
    myCkButton.grid(row=row, column=column, sticky=Left, pady=4, padx=15)
    if isSelect: myCkButton.select()

    return myCkButton

from tkinter import scrolledtext
def mkScrollText(master, width, height, row, column, columnspan, rowspan=1):
    myscrtxt = scrolledtext.ScrolledText(master, width=width, height=height, bg='SkyBlue')
    myscrtxt.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

    return myscrtxt


def mkFrame(master, width, height, row, column, bg=None, columnspan=1, rowspan=1, sticky=Left):
    myFrame = Frame(master, width=width, height=height, bg=bg, bd=1, relief=SUNKEN)
    myFrame.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky=Left, pady=5, padx=5)

    return myFrame