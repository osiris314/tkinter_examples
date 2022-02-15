from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Employes')
root.iconbitmap('images/5_logo.ico')
root.geometry('400x400')

#databases
#create database or connect to one
conn = sqlite3.connect('employes.db')#database name
#create cursor
c = conn.cursor()

#reate submit function for database
def submit():
    #create database or connect to one
    conn = sqlite3.connect('employes.db')#database name
    #create cursor
    c = conn.cursor()

    #insert into table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })
            
    #commit changes
    conn.commit()
    #close connection
    conn.close()

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


#create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Edit')
    editor.iconbitmap('images/5_logo.ico')
    editor.geometry('400x400')
    #create database or connect to one
    conn = sqlite3.connect('employes.db')#database name
    #create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    #query the database
    c.execute('SELECT * FROM addresses WHERE oid = ' + record_id)
    records = c.fetchall()   

    #create global variables
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    #create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    #create text box labels
    f_name_label = Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    #loop thru rsults
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5]) 

    #create an update button
    edit_btn = Button(editor, text='Save Record', command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)



def update():
    #create database or connect to one
    conn = sqlite3.connect('employes.db')#database name
    #create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute('''UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid''',
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })

    #commit changes
    conn.commit()
    #close connection
    conn.close()


#create function to delete a record
def delete():
    #create database or connect to one
    conn = sqlite3.connect('employes.db')#database name
    #create cursor
    c = conn.cursor()
   
    #delete a record
    c.execute('DELETE from addresses WHERE oid = ' + delete_box.get())

    #commit changes
    conn.commit()
    #close connection
    conn.close()


#create query function
def query():
    #create database or connect to one
    conn = sqlite3.connect('employes.db')#database name
    #create cursor
    c = conn.cursor()

    #query the database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()
    #print(records)

    #loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    #commit changes
    conn.commit()
    #close connection
    conn.close()


#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#create text box labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text='ID Number')
delete_box_label.grid(row=9, column=0, pady=5)

#create submit button
submit_btn = Button(root, text='Add Record To Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

#create a Query button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create a delet button

delete_btn = Button(root, text='Delete Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#create an update button
edit_btn = Button(root, text='Edit Record', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


#commit changes
conn.commit()
#close connection
conn.close()

root.mainloop()