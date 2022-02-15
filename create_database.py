from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('hello')
root.iconbitmap('')
root.geometry('400x400')

#databases
#create database or connect to one
conn = sqlite3.connect('address_book.db')#database name
#create cursor
c = conn.cursor()

#create table
c.execute('''CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )''')

#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()