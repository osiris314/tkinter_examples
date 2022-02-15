from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to code')
#root.iconbitmap('images/5_logo.ico')
root.geometry('400x400')


frame = LabelFrame(root, padx=50, pady=50)#title: text='type text here'
frame.pack(padx=10, pady=10)

b = Button(frame, text='Dont Click Here!')
b2 = Button(frame, text='...or here!')
b.grid(row=0,column=0)
b2.grid(row=1,column=1)






root.mainloop()