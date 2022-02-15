########################
# Tutorial: New Window #
########################
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('First Window!')
root.iconbitmap('images/5_logo.ico')
root.geometry('400x400')

def open():
    global my_img
    top = Toplevel()
    top.title('Second Window!')
    top.iconbitmap('images/5_logo.ico')

    my_img = ImageTk.PhotoImage(Image.open('images/6_animal_3.jpg'))
    my_label = Label(top, image=my_img)#set label to top instead of root window
    my_label.pack()

    exit_top_window = Button(top, text='Exit Window', command=top.destroy)#close second window only
    exit_top_window.pack()

second_page = Button(root, text='open second window', command=open)#open sencond window
second_page.pack()

root.mainloop()