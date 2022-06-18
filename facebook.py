from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Facebook')
root.minsize(width=500,height=300)
conn = sqlite3.connect('User.db')
conn = sqlite3.connect('User.db')
c = conn.cursor()



# c.execute("""CREATE TABLE User(
#     first_name text,
#     last_name text,
#     age text,
#     address text,
#     city text,
#     zipcode integer,
#     password text,
#     gender text


#     )""")
# print("Table created successfully")


def submit():
    conn = sqlite3.connect('User.db')
    c = conn.cursor()
    c.execute("INSERT INTO User VALUES (:f_name, :l_name, :age,:address,:city,:zipcode,:password,:gender)", {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'age': age.get(),
        'address': address.get(),
        'city': city.get(),
        'zipcode': zipcode.get(),
        'password': password.get(),
        'gender': gender.get()
    })

    messagebox.showinfo("Users", "Inserted Successfully")
    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect('User.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM User")
    records = c.fetchall()
    print(records)
    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect('User.db')
    c = conn.cursor()
    c.execute("DELETE from User WHERE oid = " + delete_box.get())
    print('Deleted Successfully')
    delete_box.delete(0, END)

    c.execute("SELECT *,oid from User")
    records = c.fetchall()
    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + '\t' + str(record[7]) + "\n"
    conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('User.db')
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("""UPDATE User SET
        first_name=:first,
        last_name=:last,
        age=:age,
        address=:address,
        city=:city,
        zipcode=:zipcode,
        password=:password,
        gender=:gender
        WHERE oid = :oid""",

        {'first':f_name_editor.get(),
         'last':l_name_editor.get(),
         'age':age_editor.get(),
         'address':address_editor.get(),
         'city':city_editor.get(),
         'zipcode':zipcode_editor.get(),
         'password':password_editor.get(),
         'gender':gender_editor.get(),
         'oid':record_id
                 }
    )

    conn.commit()
    conn.close()
    editor.destroy()




def edit():
    global editor

    editor = Toplevel()
    editor.title('Update Data')
    editor.geometry('300x480')
    conn = sqlite3.connect('User.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM User WHERE oid = " + record_id)
    records = c.fetchall()

    # creating global variable for all text boxes
    global f_name_editor
    global l_name_editor
    global age_editor
    global address_editor
    global city_editor
    global zipcode_editor
    global password_editor
    global gender_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    age_editor = Entry(editor, width=30)
    age_editor.grid(row=2, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=3, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    password_editor=Entry(editor,width=30)
    password_editor.grid(row=6,column=1)

    gender_editor=Entry(editor,width=30)
    gender_editor.grid(row=7,column=1)

    # creat text labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    age_label = Label(editor, text="Address")
    age_label.grid(row=2, column=0)

    address_label = Label(editor, text="City")
    address_label.grid(row=3, column=0)

    city_label = Label(editor, text="State")
    city_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zip Code")
    zipcode_label.grid(row=5, column=0)

    password_label=Label(editor,text='password')
    password_label.grid(row=6,column=0)

    gender_label=Label(editor,text='gender')
    gender_label.grid(row=7,column=0)


    # loop through the results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        age_editor.insert(0,record[2])
        address_editor.insert(0,record[3])
        city_editor.insert(0,record[4])
        zipcode_editor.insert(0, record[5])
        password_editor.insert(0,record[6])
        password_editor.insert(0,record[7])

    update_btn = Button(editor, text="Update",command=update)
    update_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=30)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=30)

age = Entry(root, width=30)
age.grid(row=2, column=1, padx=30)

address= Entry(root, width=30)
address.grid(row=3, column=1, padx=30)

city = Entry(root, width=30)
city.grid(row=4, column=1, padx=30)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=30)

password=Entry(root,width=30)
password.grid(row=6,column=1,padx=30)

gender=Entry(root,width=30)
gender.grid(row=7,column=1,padx=30)

delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1, pady=5)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

age_label = Label(root, text="age")
age_label.grid(row=2, column=0)

address_label = Label(root, text="address")
address_label.grid(row=3, column=0)

city_label = Label(root, text="City")
city_label.grid(row=4, column=0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)

password_label=Label(root,text='password')
password_label.grid(row=6,column=0)

gender_label=Label(root,text='gender')
gender_label.grid(row=7,column=0)

submit_btn = Button(root,bg='silver', text="Add Records", command=submit)
submit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root,bg='silver', text="Show Records", command=query)
query_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

delete_label = Label(root, text="Delete ID")
delete_label.grid(row=8, column=0, pady=5)

delete_btn = Button(root,bg='silver', text="DELETE", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

edit_btn = Button(root,bg='silver', text="EDIT", command=edit)
edit_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=120)




conn.commit()
conn.close()
root.mainloop()
