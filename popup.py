####################
# Tutorial: Popups #
####################
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('popups')
root.geometry('400x400')

#OPTIONS:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion('this is my popup!', "hello world!")
    if response == 'yes':
        Label(root, text='You Clicked Yes!').pack()
    else:
        Label(root, text='You Clicked No!').pack()

Button(root, text='popop', command=popup).pack()

root.mainloop()