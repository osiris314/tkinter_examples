#####################################################
# Tutorial: Create a window with text(grid version) #
#####################################################
from tkinter import *

#create the window
root = Tk()
root.geometry('400x400')#set window dimensions

#create a label widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My name is Evan')

#display label onto the screen(grid)
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

#==RUN==#
root.mainloop()