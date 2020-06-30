from tkinter import *
import tkinter.messagebox as tm

root = Tk()


def entryscreen():
    root.title('Alcohol Comparer')

    global alcohol1
    global amount1
    global price1
    global content1
    global alcohol2
    global amount2
    global price2
    global content2

    fr1 = Frame(root)
    fr2 = Frame(root)
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
    fr1.mainloop()


def calculate():
    number1 = amount1.get()
    number2 = amount2.get()
    cost1 = price1.get()
    cost2 = price2.get()
    percentage1 = content1.get()
    percentage2 = content2.get()

    pricepercan1 = cost1 / number1
    pricepercan2 = cost2 / number2

    print(pricepercan1)
    print(pricepercan2)





entryscreen()
