import subprocess, sys
import os
import Tkinter as tk
from tkinter import *
import tkinter
import tkinter.messagebox

root = Tk()

def choose(arg):
    if arg == 1:
        tkinter.messagebox.showinfo("button 1", "button 1")
	img.show() 
    elif arg == 2:
        tkinter.messagebox.showinfo("button 2", "button 2")
    elif arg == 3:
        tkinter.messagebox.showinfo("button 3", "button 3")
    elif arg == 4:
        tkinter.messagebox.showinfo("button 4", "button 4")
    elif arg == 5:
        tkinter.messagebox.showinfo("button 5", "button 5")
    elif arg == 6:
        tkinter.messagebox.showinfo("button 6", "button 6")
    elif arg == 7:
        tkinter.messagebox.showinfo("button 7", "button 7")
    elif arg == 8:
         root.quit()


b1 = Button(root, text="Button 1", height = 2, width = 25, command=lambda: choose(1))
b1.pack()
b2 = Button(root, text="Button 2", height = 2, width = 25, command=lambda: choose(2))
b2.pack()
b3 = Button(root, text="Button 3", height = 2, width = 25, command=lambda: choose(3))
b3.pack()
b4 = Button(root, text="Button 4", height = 2, width = 25, command=lambda: choose(4))
b4.pack()
b5 = Button(root, text="Button 5", height = 2, width = 25, command=lambda: choose(5))
b5.pack()
b6 = Button(root, text="Button 6", height = 2, width = 25, command=lambda: choose(6))
b6.pack()
b7 = Button(root, text="Button 7", height = 2, width = 25, command=lambda: choose(7))
b7.pack()
b8 = Button(root, text="EXIT", height = 2, width = 25, command=lambda: choose(8))
b8.pack()

root.mainloop()

