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

    Button(t, text='Can - Can', command=can_to_can).pack(expand=YES, fill=BOTH)
    Button(t, text='Can - Bottle').pack(expand=YES, fill=BOTH)
    Button(t, text='Bottle - Bottle', command=bottle_to_bottle).pack(expand=YES, fill=BOTH)


def can_to_can():
    t = Toplevel(root)
    t.transient(root)
    t.title('Can to Can Comparison')

    global cantocan
    global brandofcan1
    global amountofcans1
    global priceofcans1
    global contentofcans1
    global brandofcan2
    global amountofcans2
    global priceofcans2
    global contentofcans2

    fr1 = Frame(t)
    fr2 = Frame(t)
    cantocan = True
    brandofcan1 = StringVar(fr1)
    amountofcans1 = IntVar(fr1)
    priceofcans1 = DoubleVar(fr1)
    contentofcans1 = DoubleVar(fr1)
    brandofcan2 = StringVar(fr2)
    amountofcans2 = IntVar(fr2)
    priceofcans2 = DoubleVar(fr2)
    contentofcans2 = DoubleVar(fr2)

    Label(fr1, text='Alcohol Brand').grid()
    Entry(fr1, width=15, textvariable=brandofcan1).grid(row=0, column=1)

    Label(fr1, text='Amount of Cans').grid(row=1)
    Entry(fr1, width=5, textvariable=amountofcans1).grid(row=1, column=1)

    Label(fr1, text='Price of Cans').grid(row=2)
    Entry(fr1, width=5, textvariable=priceofcans1).grid(row=2, column=1)

    Label(fr1, text='Alcohol Content').grid(row=3)
    Entry(fr1, width=5, textvariable=contentofcans1).grid(row=3, column=1)

    Label(fr1, text='Alcohol Brand').grid(row=0, column=3)
    Entry(fr1, width=15, textvariable=brandofcan2).grid(row=0, column=4)

    Label(fr1, text='Amount of Cans').grid(row=1, column=3)
    Entry(fr1, width=5, textvariable=amountofcans2).grid(row=1, column=4)

    Label(fr1, text='Price of Cans').grid(row=2, column=3)
    Entry(fr1, width=5, textvariable=priceofcans2).grid(row=2, column=4)

    Label(fr1, text='Alcohol Content').grid(row=3, column=3)
    Entry(fr1, width=5, textvariable=contentofcans2).grid(row=3, column=4)

    Button(fr1, text='Quit', command=root.quit).grid(row=4, column=1)
    Button(fr1, text='Calculate', command=calculate).grid(row=4, column=3)

    fr1.pack()


def bottle_to_bottle():
    t = Toplevel(root)
    t.transient(root)
    t.title('Bottle to Bottle Comparison')

    global brandofbottle1
    global amountofbottles1
    global priceofbottles1
    global contentofbottles1
    global brandofbottle2
    global amountofbottles2
    global priceofbottles2
    global contentofbottles2

    fr1 = Frame(t)
    fr2 = Frame(t)
    brandofbottle1 = StringVar(fr1)
    amountofbottles1 = IntVar(fr1)
    priceofbottles1 = DoubleVar(fr1)
    contentofbottles1 = DoubleVar(fr1)
    brandofbottle2 = StringVar(fr2)
    amountofbottles2 = IntVar(fr2)
    priceofbottles2 = DoubleVar(fr2)
    contentofbottles2 = DoubleVar(fr2)

    Label(fr1, text='Alcohol Brand').grid()
    Entry(fr1, width=15, textvariable=brandofbottle1).grid(row=0, column=1)

    Label(fr1, text='Amount of Bottles').grid(row=1)
    Entry(fr1, width=5, textvariable=amountofbottles1).grid(row=1, column=1)

    Label(fr1, text='Price of Bottles').grid(row=2)
    Entry(fr1, width=5, textvariable=priceofbottles1).grid(row=2, column=1)

    Label(fr1, text='Alcohol Content').grid(row=3)
    Entry(fr1, width=5, textvariable=contentofbottles1).grid(row=3, column=1)

    Label(fr1, text='Alcohol Brand').grid(row=0, column=3)
    Entry(fr1, width=15, textvariable=brandofbottle2).grid(row=0, column=4)

    Label(fr1, text='Amount of Bottles').grid(row=1, column=3)
    Entry(fr1, width=5, textvariable=amountofbottles2).grid(row=1, column=4)

    Label(fr1, text='Price of Bottles').grid(row=2, column=3)
    Entry(fr1, width=5, textvariable=priceofbottles2).grid(row=2, column=4)

    Label(fr1, text='Alcohol Content').grid(row=3, column=3)
    Entry(fr1, width=5, textvariable=contentofbottles2).grid(row=3, column=4)

    Button(fr1, text='Quit', command=root.quit).grid(row=4, column=1)
    Button(fr1, text='Calculate', command=calculate).grid(row=4, column=3)

    fr1.pack()


def calculate():
    if cantocan:
        price1 = priceofcans1.get()
        price2 = priceofcans2.get()
        content1 = contentofcans1.get()
        content2 = contentofcans2.get()
        alcohol1 = brandofcan1.get()
        alcohol2 = brandofcan2.get()
        amount1 = amountofcans1.get()
        amount2 = amountofcans2.get()
    else:
        price1 = priceofbottles1.get()
        price2 = priceofbottles2.get()
        content1 = contentofbottles1.get()
        content2 = contentofbottles2.get()
        alcohol1 = brandofbottle1.get()
        alcohol2 = brandofbottle2.get()
        amount1 = amountofbottles1.get()
        amount2 = amountofbottles2.get()

    priceperunit1 = price1 / amount1
    priceperunit2 = price2 / amount2

    contentpereuro1 = round(content1 / priceperunit1, 2)
    contentpereuro2 = round(content2 / priceperunit2, 2)

    if contentpereuro1 > contentpereuro2:
        tm.showinfo('Result', alcohol1 + ' is better value than ' + alcohol2)
    else:
        tm.showinfo('Result', alcohol2 + ' is better value than ' + alcohol1)


welcomescreen()
