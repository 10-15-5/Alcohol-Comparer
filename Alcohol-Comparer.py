from tkinter import *
import tkinter.messagebox as tm

root = Tk()


def welcomescreen():
    root.title('Welcome!')
    fr = Frame(root)

    message = "Welcome to the alcohol comparer!\nThis program is still under construction but please" \
              " enjoy it in it's current state.\nAny feedback is appreciated."

    Label(root, text=message).pack()
    Button(fr, text='Quit', command=root.quit).grid(row=3)
    Button(fr, text='Go', command=choose).grid(row=3, column=1)

    fr.pack()
    fr.mainloop()


def choose():
    t = Toplevel(root)
    t.transient(root)
    t.title('Please Choose a Comparison')

    Button(t, text='Can - Can', command=can_to_can).pack()
    Button(t, text='Can - Bottle').pack()
    Button(t, text='Bottle - Bottle').pack()


def can_to_can():
    t = Toplevel(root)
    t.transient(root)
    t.title('Alcohol Comparer')

    global alcohol1
    global amount1
    global price1
    global content1
    global alcohol2
    global amount2
    global price2
    global content2

    fr1 = Frame(t)
    fr2 = Frame(t)
    alcohol1 = StringVar(fr1)
    amount1 = IntVar(fr1)
    price1 = DoubleVar(fr1)
    content1 = DoubleVar(fr1)
    alcohol2 = StringVar(fr2)
    amount2 = IntVar(fr2)
    price2 = DoubleVar(fr2)
    content2 = DoubleVar(fr2)

    Label(fr1, text='Alcohol Brand').grid()
    Entry(fr1, width=15, textvariable=alcohol1).grid(row=0, column=1)

    Label(fr1, text='Amount of Cans').grid(row=1)
    Entry(fr1, width=5, textvariable=amount1).grid(row=1, column=1)

    Label(fr1, text='Price of Cans').grid(row=2)
    Entry(fr1, width=5, textvariable=price1).grid(row=2, column=1)

    Label(fr1, text='Alcohol Content').grid(row=3)
    Entry(fr1, width=5, textvariable=content1).grid(row=3, column=1)

    Label(fr1, text='Alcohol Brand').grid(row=0, column=3)
    Entry(fr1, width=15, textvariable=alcohol2).grid(row=0, column=4)

    Label(fr1, text='Amount of Cans').grid(row=1, column=3)
    Entry(fr1, width=5, textvariable=amount2).grid(row=1, column=4)

    Label(fr1, text='Price of Cans').grid(row=2, column=3)
    Entry(fr1, width=5, textvariable=price2).grid(row=2, column=4)

    Label(fr1, text='Alcohol Content').grid(row=3, column=3)
    Entry(fr1, width=5, textvariable=content2).grid(row=3, column=4)

    Button(fr1, text='Quit', command=root.quit).grid(row=4, column=1)
    Button(fr1, text='Calculate', command=calculate).grid(row=4, column=3)

    fr1.pack()


def bottle_to_bottle():
    print('hello')


def calculate():
    priceperunit1 = price1.get() / amount1.get()
    priceperunit2 = price2.get() / amount2.get()

    contentpereuro1 = round(content1.get() / priceperunit1, 2)
    contentpereuro2 = round(content2.get() / priceperunit2, 2)

    if contentpereuro1 > contentpereuro2:
        tm.showinfo('Result', alcohol1.get() + ' is better value than ' + alcohol2.get())
    else:
        tm.showinfo('Result', alcohol2.get() + ' is better value than ' + alcohol1.get())


welcomescreen()
