# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:56:03 2020

@author: jfarm
"""

from tkinter import Tk, Entry, Label, Button
from tkinter.font import Font

def main():
    wn = Tk()
    wn.title("Calculator")
    
    fontStyle = Font(family='Courier', size=20)
    
    entryExp = Entry(master=wn, width=30, font=fontStyle)
    labelEq = Label(master=wn, font=fontStyle, text=" = ")
    labelAns = Label(master=wn, text="NULL", font=fontStyle)
    buttonCalc = Button(master=wn, text="Calculate", font=fontStyle, 
                        command=lambda :  calculate(entryExp, labelAns))
    
    entryExp.grid(row=0, column=0)
    labelEq.grid(row=0, column=1)
    labelAns.grid(row=0, column=2)
    buttonCalc.grid(row=1, column=0)
    
    wn.mainloop()

def calculate(exp, labelAns):
    '''Evaluate the expression in the entry field.
        Update the result label with the result.'''
    e = exp.get()
    result = eval(e)
    labelAns['text'] = result
    
if __name__ == "__main__":
    main()