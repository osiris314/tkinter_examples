#####################################################
# Tutotial: Create a window with text(pack version) #
#####################################################
from tkinter import *

#create the window
root = Tk()
root.geometry('400x400')#set window dimensions

#create a label widget
myLabel = Label(root, text='Hello World!')

#display label onto the screen(pack)
myLabel.pack()

#==RUN==#
root.mainloop()