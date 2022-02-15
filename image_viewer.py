########################
#Tutorial: Image Viewer#
########################
from tkinter import *
from PIL import ImageTk,Image


#create the window
root = Tk()
root.title('Images')#set title
root.iconbitmap('images/5_logo.ico')#set icon

#define the images
my_img1 = ImageTk.PhotoImage(Image.open('images/6_animal_1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/6_animal_2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/6_animal_3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/6_animal_4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('images/6_animal_5.jpg'))

#create an image list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

#define the label
my_label = Label(image=my_img1)
#display label onto the screen(grid)
my_label.grid(row=0, column=0, columnspan=3)

#functions
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>>', command=lambda : forward(image_number+1))
    button_back = Button(root, text='<<<', command=lambda : back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text='>>>', state=DISABLED)
    #label
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #update status bar
    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>>', command=lambda : forward(image_number+1))
    button_back = Button(root, text='<<<', command=lambda : back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text='<<<', state=DISABLED)   

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #update status bar
    status = Label(root, text='Image ' + str(image_number) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


#create buttons
button_back = Button(root, text='<<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>>', command=lambda:forward(2))

#display buttons onto the screen(grid)
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#==RUN==#
root.mainloop()