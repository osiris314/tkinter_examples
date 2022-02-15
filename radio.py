from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('e-food')
#root.iconbitmap('images/5_logo.ico')
root.geometry('400x400')

#create title label
title = Label(root, text='Toppings:')
#display title onto the screen
title.pack()

#list with available toppings
TOPPINGS = [
    ('pepperoni','pepperoni'),
    ('cheese','cheese'),
    ('mushrooms','mushrooms'),
    ('onion','onion'),
]


pizza = StringVar()
pizza.set('pepperoni')

#loop
for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

#functions
def clicked(value):
    my_Label = Label(root, text=value)
    my_Label.pack()


myButton = Button(root, text='Add', command=lambda: clicked(pizza.get()))
myButton.pack()

#==RUN==#
mainloop()