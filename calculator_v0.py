########################
# Tutotial: calculator #
########################
from tkinter import *


#create the window
root = Tk()
root.title('Calculator')#set title

#create an entry
entry_field = Entry(root, width=35, borderwidth=5)

#display buttons onto the screen(grid)
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#functions
def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(number))

def button_clear():
    entry_field.delete(0, END)

def button_equal():
    second_number = entry_field.get()
    entry_field.delete(0, END)
    if math == 'addition':
        entry_field.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        entry_field.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        entry_field.insert(0, f_num * int(second_number))
    if math == 'division':
        entry_field.insert(0, f_num / int(second_number))

def button_add():
    first_number = entry_field.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    entry_field.delete(0, END)

def button_subtract():
    first_number = entry_field.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry_field.delete(0, END)

def button_multiply():
    first_number = entry_field.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry_field.delete(0, END)

def button_divide():
    first_number = entry_field.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry_field.delete(0, END)


#create the buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))#button 1
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))#button 2
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))#button 3
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))#button 4
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))#button 5
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))#button 6
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))#button 7
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))#button 8
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))#button 9
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))#button 0
buttonAdd = Button(root, text='+', padx=39, pady=20, command=button_add)#button addition
buttonEqual = Button(root, text='=', padx=86, pady=20, command=button_equal)#button equal
buttonClear = Button(root, text='Clear', padx=77, pady=20, command=button_clear)#button clear
button_divide = Button(root, text='/', padx=40, pady=20, command=button_divide)#button divide
button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)#buttom subtract
button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)#button multiply


#put the buttons on the screen
#row 1
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
#row 2
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
#row 3
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
#row 4
button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
#row 5
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
#row 6
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


#==RUN==#
root.mainloop()