########################
# Tutorial: Drop Menus #
########################
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Drop menu!')
root.geometry('400x400')
root.iconbitmap('images/5_logo.ico')


def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()


options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

clicked = StringVar()#selected value
clicked.set(options[0])#set list option to first item

drop = OptionMenu(root, clicked, *options)#create drop menu  | WARNING before the list name dont forget the * symbol
drop.pack()

myButton = Button(root, text='Show selection', command=show)
myButton.pack()

root.mainloop()
