######################################
# Tutotial: Create buttons different #
######################################
from tkinter import *

#create the window
root = Tk()
root.geometry('400x400')#set window dimensions

#Functions
def myClick():
    myLabel = Label(root, text='You clicked a button!!')
    myLabel.pack()


#create button widgets
myNormalButton = Button(root, text='normal')#normal with letters(text)
myRedAndWhiteButton = Button(root, text='white letters / red background', fg='white', bg='red')#white letters(fg) & red background(bg)
myDisabledButton = Button(root, text='disabled', state=DISABLED)#disabled(state)
myLenghtButton = Button(root, text='100 lenght', padx=100)#lenght 70px(padx)
myHeightButton = Button(root, text='20 height', pady=20)#height 20px(pady)
myHeightLenghtButton = Button(root, text='30 lenght / 20 height', padx=30, pady=20)#30 lenght & 20 height
myClickButton = Button(root, text='click me!', command=myClick)#call a function button(command)

#display buttons onto the screen(pack)
myNormalButton.pack()
myRedAndWhiteButton.pack()
myDisabledButton.pack()
myLenghtButton.pack()
myHeightButton.pack()
myHeightLenghtButton.pack()
myClickButton.pack()


#==RUN==#
root.mainloop()