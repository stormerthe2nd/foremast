from database import users, users2
from tkinter import Tk, Label, Button, Entry, END, Text
import sqlite3

color = 'dark olive green'
root = Tk()
root.configure(background=color)
root.geometry("360x280")
root.title("Login Box")


# bank account box
def login_press(event):
    global name, rp, pas, users2
    name = aentry.get()
    pas = bentry.get()
    rp = users.get(name)
    bal = users2.get(name)
    if pas == rp and name in users:
        root.destroy()
        root2 = Tk()
        transaction = 'neutral'
        ly = 'gold3'
        root2.configure(background=ly)
        root2.geometry("482x380")
        root2.title("Red Dead Redemption Bank")

        def empty(x, y):
            Label(root2, text='123456789', fg=ly, bg=ly).grid(row=x, column=y)

        def press_deposit(event):
            nonlocal bal, transaction
            global d_amt, rp
            tb.delete(1.0, END)
            d_amt = entry1.get()
            if d_amt == '' or d_amt is None:
                tb.insert(END, f'Please Specify Amount\n')
            else:
                transaction = 'deposited'
                d_amt = int(d_amt)
                bal = bal + d_amt
                tb.insert(END, f'Rs_{d_amt} is Deposited in your Account\n')
                con = sqlite3.connect('login.db')
                cur = con.cursor()
                cur.execute("UPDATE emp SET bal = ? WHERE name = ? ",
                            (bal, name))
                con.commit()
                con.close()
            entry1.delete(0, END)

        def press_withdraw(event):
            nonlocal bal, transaction
            global w_amt
            tb.delete(1.0, END)
            w_amt = entry2.get()
            if w_amt == '' or w_amt is None:
                tb.insert(END, f'Please Specify Amount\n')
            else:

                w_amt = int(w_amt)
                if bal < w_amt:
                    transaction = 'neutral'
                    tb.insert(END, f'Transaction Denied\n')
                    tb.insert(END, f'You have only Rs_{bal} in your Account')
                else:
                    transaction = 'withdrawn'
                    bal = bal - w_amt
                    tb.insert(END,
                              f'Rs_{w_amt} is Withdrawn from your Account')
                    con = sqlite3.connect('login.db')
                    cur = con.cursor()
                    cur.execute("UPDATE emp SET bal = ? WHERE name = ? ",
                                (bal, name))
                    con.commit()
                    con.close()
            entry2.delete(0, END)

        def press_checkbal(event):
            nonlocal bal
            tb.delete(1.0, END)
            tb.insert(END, f'You have Rs_{bal} is your Account\n')

        def press_lt(event):
            nonlocal bal, transaction
            global d_amt, w_amt
            tb.delete(1.0, END)
            if transaction == 'deposited':
                tb.insert(END, f'You Deposited Rs_{d_amt} is your Account')
            elif transaction == 'withdrawn':
                tb.insert(END, f'You Withdrawn Rs_{w_amt} is your Account')
            else:
                tb.insert(END, f'Please make a transation')

        def press_close(event):
            root2.destroy()

        empty(1, 0)
        Label(root2, text='Welcome to Red Dead Redemption Bank',
              font=("Helvetica", "14"), bg=ly
              ).grid(row=0, column=2, columnspan=3)
        Label(root2, text='Deposit Amount', font=("Times", "12"),
              bg=ly).grid(row=2, column=2, sticky='w')
        entry1 = Entry(root2, bg='misty rose3')
        entry1.grid(row=2, column=3, sticky='w')
        empty(3, 0)
        Label(root2, text='Withdraw Amount', font=("Times", "12"),
              bg=ly).grid(row=4, column=2, sticky='w')
        entry2 = Entry(root2, bg='misty rose3')
        entry2.grid(row=4, column=3, sticky='w')
        d_button = Button(root2, text='Deposit', bg='sky blue')
        d_button.grid(row=2, column=4)
        w_button = Button(root2, text='Withdraw', bg='sky blue')
        w_button.grid(row=4, column=4)
        empty(5, 0)
        empty(6, 0)
        c_button = Button(root2, text='Check Balance', bg='sky blue')
        c_button.grid(row=7, column=2)
        lt_button = Button(root2, text='Last Transaction', bg='sky blue')
        lt_button.grid(row=7, column=3)
        close_button = Button(root2, text='Close', bg='sky blue')
        close_button.grid(row=7, column=4)
        empty(8, 0)
        tb = Text(root2, height=5, width=40, font=("Times", "12"), bg='plum1')
        tb.grid(row=9, column=1, columnspan=4)
        w_button.bind('<Button>', press_withdraw)
        d_button.bind('<Button>', press_deposit)
        c_button.bind('<Button>', press_checkbal)
        lt_button.bind('<Button>', press_lt)
        close_button.bind('<Button>', press_close)
        root2.resizable(0, 0)

    else:
        Label(root, text='Incorrect Please Try Again', fg='red',
              font=("Helvetica", "10"),
              bg=color).place(x=100, y=90)
        aentry.delete(0, END)
        bentry.delete(0, END)


# the create a new account Box
def press_create(event):
    global color
    root.destroy()
    root3 = Tk()
    root3.configure(background=color)
    root3.geometry("360x220")
    root3.title("Register")

    def press_create2(event):
        name2 = centry.get()
        pass2 = dentry.get()
        if name2 not in users2:
            name2 = str(name2)
            pass2 = int(pass2)
            con = sqlite3.connect('login.db')
            cur = con.cursor()
            pass3 = str(pass2)
            cur.execute("INSERT INTO emp VALUES (?,?,?)", (name2, pass3, 0))
            con.commit()
            con.close()
            centry.delete(0, END)
            dentry.delete(0, END)
            Label(root3, text='''Account Created Successfully please
Close the Application and Start again''',
                  fg='green2', font=("Helvetica", "10", "bold"),
                  bg=color).place(x=60, y=175)
        else:
            txt = '''User Already Exists, Please try a
different Username'''
            Label(root3, text=txt,
                  fg='red3', font=("Helvetica", "10", "bold"),
                  bg=color).place(x=70, y=175)

    Label(root3, text="Please provide a Username and a Password", fg='azure',
          font=("Helvetica", "10", "bold italic"),
          bg=color).place(x=45, y=8)
    Label(root3, text="Name", fg='azure',
          font=("Helvetica", "10", "bold italic"),
          bg=color).place(x=70, y=40)
    centry = Entry(root3, bg='misty rose', fg='black')
    centry.place(x=150, y=40)
    Label(root3, text="Pin", fg='azure',
          font=("Helvetica", "10", "bold italic"),
          bg=color).place(x=70, y=80)
    dentry = Entry(root3, bg='misty rose', fg='black')
    dentry.place(x=150, y=80)
    Label(root3,
          text='Create a unique Username and use Numbers for pin',
          fg='azure', font=("Helvetica", "10", "bold"),
          bg=color).place(x=7, y=110)

    button3 = Button(root3, text='Create', fg='black', bg='burlywood3')
    button3.place(x=160, y=148)
    button3.bind("<Button>", press_create2)
    root3.resizable(0, 0)


# delete an account box
def press_delete(event):
    global color
    root.destroy()
    root4 = Tk()
    root4.title('Delete Account')
    root4.configure(background=color)
    root4.geometry("360x220")

    def press_delete2(event):
        name3 = eentry.get()
        pin3 = fentry.get()
        rp = users.get(name3)
        if name3 in users and pin3 == rp:
            con = sqlite3.connect('login.db')
            cur = con.cursor()
            cur.execute("DELETE FROM emp WHERE name = ?", (name3,))
            con.commit()
            con.close()
            txt2 = '''Account Deleted Successfully
Please restart Application'''
            Label(root4, text=txt2,
                  fg='green2', font=("Helvetica", "10", "bold"),
                  bg=color).place(x=85, y=175)

        else:
            Label(root4, text='Please Try Again',
                  fg='red3', font=("Helvetica", "10", "bold"),
                  bg=color).place(x=125, y=175)
        eentry.delete(0, END)
        fentry.delete(0, END)

    Label(root4, text="Please Enter Name and Pin to Specify your Account",
          fg='azure', font=("Helvetica", "10", "bold italic"),
          bg=color).place(x=18, y=8)
    Label(root4, text="Enter Name", fg='azure',
          font=("Helvetica", "10", "bold italic"),
          bg=color).place(x=65, y=50)
    Label(root4, text="Enter Pin", fg='azure',
          font=("Helvetica", "10", "bold italic"),
          bg=color).place(x=70, y=80)
    eentry = Entry(root4, bg='misty rose', fg='black')
    eentry.place(x=160, y=50)
    fentry = Entry(root4, bg='misty rose', fg='black')
    fentry.place(x=160, y=80)
    button4 = Button(root4, text='Delete', fg='black', bg='burlywood3')
    button4.place(x=160, y=148)
    button4.bind("<Button>", press_delete2)
    root4.resizable(0, 0)


# the login Box
Label(root, text="Welcome to Red Dead Redemption Bank", fg='khaki',
      font=("Helvetica", "10", "bold italic"),
      bg=color).place(x=50, y=1)
Label(root, text="Name", fg='azure',
      font=("Helvetica", "10", "bold italic"),
      bg=color).place(x=80, y=30)

aentry = Entry(root, bg='misty rose', fg='black')
aentry.place(x=140, y=30)
Label(root, text="Pin", fg='azure',
      font=("Helvetica", "10", "bold italic"),
      bg=color).place(x=80, y=70)
bentry = Entry(root, bg='misty rose', fg='black')
bentry.place(x=140, y=70)
button1 = Button(root, text='Login ', bg='burlywood3', fg='black')
button2 = Button(root, text='Create', fg='black', bg='burlywood3')
button3 = Button(root, text='Delete', fg='black', bg='burlywood3')
Label(root, text='Press Create to create a new Account',
      font=("Helvetica", "10", "bold italic"),
      fg='azure', bg=color).place(x=58, y=160)
Label(root, text='Press Delete to an existing Account',
      font=("Helvetica", "10", "bold italic"),
      fg='azure', bg=color).place(x=65, y=222)
button1.bind("<Button>", login_press)
button2.bind("<Button>", press_create)
button3.bind("<Button>", press_delete)
button1.place(x=156, y=120)
button2.place(x=155, y=185)
button3.place(x=156, y=245)
root.resizable(0, 0)
root.mainloop()
