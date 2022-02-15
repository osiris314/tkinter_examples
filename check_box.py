########################
# Tutorial: Checkboxes #
########################
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('hello')
root.geometry('400x400')
root.iconbitmap('images/5_logo.ico')


def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()


var = StringVar()
#if you want the checkbox to return something different from 0
#for off and 1 for on, You instead write  |    var = StringVar()    |

c = Checkbutton(root, text='check this button!', variable=var)
c.deselect()
c.pack()
#if you want the checkbox to return something different from 0
#for off and 1 for on, You add into the options |   ,onvalue='someting', offvalue='something else'   |

myButton = Button(root, text='show selection', command=show)
myButton.pack()

root.mainloop()