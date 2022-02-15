#########################
# Tutorial: Input boxes #
#########################
from tkinter import *

#create the window
root = Tk()
root.geometry('400x400')#set window dimensions

#Functions
def myClick():
    hello = "Hello " + myEnterNameEntry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


#create entry widgets
myNormalEntry = Entry(root)#normal entry
myDisabledEntry = Entry(root, state=DISABLED)#disabled entry(state)
myWidthEntry = Entry(root, width=50)#width 50 entry(width)
myOrangeAndLightBlueEntry = Entry(root, fg='orange', bg='light blue')#orange letters(fg) & light-blue background(bg)
myBorderWidthEntry = Entry(root, borderwidth=5)#border width 5(borderwidth)
myEnterNameEntry = Entry(root)#enter name entry

#insert default text for entries
myNormalEntry.insert(0, 'Normal Entry')
myWidthEntry.insert(0, 'Width 50')
myOrangeAndLightBlueEntry.insert(0,'Orange & Light-Blue')
myBorderWidthEntry.insert(0, 'Border-Width 5')
myEnterNameEntry.insert(0, 'Enter Name Here...')

#display entries onto the screen(pack)
myNormalEntry.pack()
myDisabledEntry.pack()
myWidthEntry.pack()
myOrangeAndLightBlueEntry.pack()
myBorderWidthEntry.pack()
myEnterNameEntry.pack()


#create button widget
submitButton = Button(root, text='Submit Your Name', command=myClick)

#display button onto the screen(pack)
submitButton.pack()


#==RUN==#
root.mainloop()