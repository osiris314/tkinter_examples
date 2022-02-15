###################
#Tutorial: Images #
###################
from tkinter import *
from PIL import ImageTk,Image


#create the window
root = Tk()
root.title('Images')#set title
root.iconbitmap('images/5_logo.ico')#set icon
root.geometry('400x400')#set window dimensions

#define the image
my_img = ImageTk.PhotoImage(Image.open('images/5_dog.jpg'))
#define the label
my_label = Label(image=my_img)
#display label onto the screen(pack)
my_label.pack()

#create the exit button
button_exit = Button(root, text='Exit', command=root.quit)
#display exit_button onto the screen(pack)
button_exit.pack()


#==RUN==#
root.mainloop()