
from tkinter import *
import sqlite3
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


root = Tk()
root.title("Contact System")
root.geometry("700x400+0+0")
root.resizable(0, 0)
root.config(bg="dark gray")

# VARIABLES
f_name = StringVar()
m_name = StringVar()
l_name = StringVar()
age = StringVar()
home_address = StringVar()
phone_number = StringVar()
gender = StringVar()
religion = StringVar()
nationality = StringVar()

# METHODS
def Exit():
    wayOut = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def Reset():
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")
    religion.set("")
    nationality.set("")

def Database():
    conn = sqlite3.connect("contactdb.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `contactable` (id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, first_name TEXT, middle_name TEXT, last_name TEXT, gender TEXT, age TEXT, home_address TEXT, phone_number TEXT, religion TEXT, nationality TEXT)")
    cursor.execute("SELECT * FROM `contactable` ORDER BY `last_name` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Submit():
    if f_name.get() == "" or m_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or home_address.get() == "" or phone_number.get() == "" or religion.get() == "" or nationality.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contactdb.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO `contactable` (first_name, middle_name, last_name, gender, age, home_address, phone_number, religion, nationality) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()), str(home_address.get()),
            int(phone_number.get()), str(religion.get()), str(nationality.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `contactable` ORDER BY `last_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")
        religion.set("")
        nationality.set("")


def Update():
    if gender.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contactdb.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE `contactable` SET `first_name` = ?, `middle_name` = ? , `last_name` = ?, `gender` =?, `age` = ?,  `home_address` = ?, `phone_number` = ?, `religion` = ?, `nationality` = ? WHERE `id` = ?",
            (str(f_name.get()), str(m_name.get()),  str(l_name.get()), str(gender.get()), int(age.get()), str(home_address.get()),
            str(phone_number.get()), str(religion.get()), str(nationality.get()), int(id)))
        conn.commit()
        cursor.execute("SELECT * FROM `contactable` ORDER BY `last_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")
        religion.set("")
        nationality.set("")

def UpdateContactWindow(event):
    global id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    id = selecteditem[0]
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")
    religion.set("")
    nationality.set("")

    f_name.set(selecteditem[1])
    m_name.set(selecteditem[2])
    l_name.set(selecteditem[3])

    age.set(selecteditem[5])
    home_address.set(selecteditem[6])
    phone_number.set(selecteditem[7])
    religion.set(selecteditem[8])
    nationality.set(selecteditem[9])

    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact Details")
    UpdateWindow.geometry("500x520+0+0")
    UpdateWindow.config(bg="dark gray")
    UpdateWindow.resizable(0, 0)
    if 'NewWindow' in globals():
        NewWindow.destroy()

    # FRAMES
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)
    Transgender = Radiobutton(RadioGroup, text="Transgender", variable=gender, value="Transgender", font=('arial', 14)).pack(side=LEFT)
    # LABELS
    lbl_title = Label(FormTitle, text="Updating Contacts", bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 14, "bold"), pady=3)
    lbl_title.pack(fill=X)
    lbl_FirstName = Label(ContactForm, text="First Name", font=('arial', 14), bd=5)
    lbl_FirstName.grid(row=0, sticky=W)

    lbl_MiddleName = Label(ContactForm, text="Middle Name", font=('arial', 14), bd=5)
    lbl_MiddleName.grid(row=1, sticky=W)

    lbl_LastName = Label(ContactForm, text="Last Name", font=('arial', 14), bd=5)
    lbl_LastName.grid(row=2, sticky=W)

    lbl_Gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_Gender.grid(row=3, sticky=W)

    lbl_Age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_Age.grid(row=4, sticky=W)

    lbl_HomeAddress = Label(ContactForm, text=" Home Address", font=('arial', 14), bd=5)
    lbl_HomeAddress.grid(row=5, sticky=W)

    lbl_PhoneNumber = Label(ContactForm, text="Phone Number", font=('arial', 14), bd=5)
    lbl_PhoneNumber.grid(row=6, sticky=W)

    lbl_Religion = Label(ContactForm, text="Religion", font=('arial', 14), bd=5)
    lbl_Religion.grid(row=7, sticky=W)

    lbl_Nationality = Label(ContactForm, text="Nationality", font=('arial', 14), bd=5)
    lbl_Nationality.grid(row=8, sticky=W)

    # TEXT ENTRY
    FirstName = Entry(ContactForm, textvariable=f_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    MiddleName = Entry(ContactForm, textvariable=m_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    MiddleName.grid(row=1, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    LastName.grid(row=2, column=1)

    RadioGroup.grid(row=3, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Age.grid(row=4, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    HomeAddress.grid(row=5, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    PhoneNumber.grid(row=6, column=1)

    Religion = Entry(ContactForm, textvariable=religion, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Religion.grid(row=7, column=1)

    Nationality = Entry(ContactForm, textvariable=nationality, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    Nationality.grid(row=8, column=1)
    # ==================BUTTONS==============================
    ButtonUpdatContact = Button(ContactForm, text='Update', bd=10, font=('arial', 12, 'bold'), relief="ridge", fg="white",
                              bg="blue", command=Update)
    ButtonUpdatContact.grid(row=9, columnspan=2, pady=10)



def Delete():
    if not tree.selection():
        result = tkMessageBox.showwarning('', 'Please Select in the Table First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete This Record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("contactdb.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `contactable` WHERE `id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def AddNewContact():
    global NewWindow
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")
    religion.set("")
    nationality.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact Details")
    NewWindow.resizable(0, 0)
    NewWindow.geometry("500x520+0+0")
    NewWindow.config(bg="dark gray")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    # ===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)
    Transgender = Radiobutton(RadioGroup, text="Transgender", variable=gender, value="Transgender", font=('arial', 14)).pack(side=LEFT)
    # ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Contacts",  bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 14, "bold"), pady=3)
    lbl_title.pack(fill=X)
    lbl_FirstName = Label(ContactForm, text="First Name", font=('arial', 14), bd=5)
    lbl_FirstName.grid(row=0, sticky=W)

    lbl_MiddleName = Label(ContactForm, text="Middle Name", font=('arial', 14), bd=5)
    lbl_MiddleName.grid(row=1, sticky=W)

    lbl_LastName = Label(ContactForm, text="Last Name", font=('arial', 14), bd=5)
    lbl_LastName.grid(row=2, sticky=W)

    lbl_Gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_Gender.grid(row=3, sticky=W)

    lbl_Age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_Age.grid(row=4, sticky=W)

    lbl_HomeAddress = Label(ContactForm, text=" Home Address", font=('arial', 14), bd=5)
    lbl_HomeAddress.grid(row=5, sticky=W)

    lbl_PhoneNumber = Label(ContactForm, text="Phone Number", font=('arial', 14), bd=5)
    lbl_PhoneNumber.grid(row=6, sticky=W)

    lbl_Religion = Label(ContactForm, text="Religion", font=('arial', 14), bd=5)
    lbl_Religion.grid(row=7, sticky=W)

    lbl_Nationality = Label(ContactForm, text="Nationality", font=('arial', 14), bd=5)
    lbl_Nationality.grid(row=8, sticky=W)

    # ===================ENTRY===============================
    FirstName = Entry(ContactForm, textvariable=f_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    MiddleName = Entry(ContactForm, textvariable=m_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    MiddleName.grid(row=1, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    LastName.grid(row=2, column=1)

    RadioGroup.grid(row=3, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Age.grid(row=4, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    HomeAddress.grid(row=5, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    PhoneNumber.grid(row=6, column=1)

    Religion = Entry(ContactForm, textvariable=religion, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Religion.grid(row=7, column=1)

    Nationality = Entry(ContactForm, textvariable=nationality, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Nationality.grid(row=8, column=1)

    # ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Save',  bd=10, font=('arial', 12, 'bold'), relief="ridge", fg="white",
                   bg="blue", command=Submit)
    ButtonAddContact.grid(row=9, columnspan=2, pady=10)


# ============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500, bg="dark gray")
Mid.pack(side=BOTTOM)
f1 = Frame(root, width=6, height=8, bd=8, bg="dark gray")
f1.pack(side=BOTTOM)
flb = Frame(f1, width=6, height=8, bd=8, bg="blue")
flb.pack(side=BOTTOM)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="dark gray")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

# LABELS
lbl_title = Label(Top,  text="Contact Management System", bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 36, "bold"), pady=3)
lbl_title.pack(fill=X)


# BUTTONS
ButtonAdd = Button(flb, text='Add New Contact',  bd=8, font=('arial', 12, 'bold'), relief="groove", fg="black",
                   bg="dark gray", command=AddNewContact).grid(row=0, column=0, ipadx=20, padx=30)

ButtonDelete = Button(flb, text='Delete', bd=8, font=('arial', 12, 'bold'), relief="groove",  command=Delete,
                  fg="black", bg="dark gray").grid(row=0, column=1, ipadx=20)

ButtonExit = Button(flb, text='Exit System', bd=8, font=('arial', 12, 'bold'), relief="groove",  command=Exit,
                 fg="black", bg="dark gray").grid(row=0, column=2, ipadx=20, padx=30)

# TABLES
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Id", "First Name", "Middle Name", "Last Name", "Gender", "Age", "Home Address", "Phone Number", "Religion", "Nationality"),
                    height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=W)
tree.heading('First Name', text="First Name", anchor=W)
tree.heading('Middle Name', text="Middle Name", anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Home Address', text="Home Address", anchor=W)
tree.heading('Phone Number', text="phone Number", anchor=W)
tree.heading('Religion', text="Religion", anchor=W)
tree.heading('Nationality', text="Nationality", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=30)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', UpdateContactWindow)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()

