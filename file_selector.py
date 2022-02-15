############################
# Tutorial: Image Selector #
############################
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('File selector!')
root.iconbitmap('images/5_logo.ico')
root.geometry('400x400')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='images/',
        title='Select a File!', filetypes=(('jpg files','*.jpg'),('all files', '*.*')))#set file types of preference
    
    my_label = Label(root, text=root.filename)#directory of the selected file
    my_label.pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))#image file
    my_image_lable = Label(root, image=my_image)
    my_image_lable.pack()#print label image


my_btn = Button(root, text='Browse..', command=open)
my_btn.pack()

root.mainloop()