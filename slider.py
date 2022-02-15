###############################
# Tutorial: Sliders or Scales #
###############################
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('File selector!')
root.iconbitmap('images/5_logo.ico')
root.geometry('400x400')


def slide():
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))#set window dimensions to slider value x,y


#the lowest value is    from_    and the highest is     to
horizontal = Scale(root, from_=400, to=800, orient=HORIZONTAL, bg='light blue')#create a horizontal scale
horizontal.pack()

vertical = Scale(root, from_=400, to=800, fg='orange')#create a vertical scale
vertical.pack()

my_btn = Button(root, text='click me', command=slide)
my_btn.pack()

root.mainloop()