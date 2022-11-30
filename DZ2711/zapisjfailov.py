from tkinter import *
import subprocess

root = Tk()
fr_top = Frame(root)
fr_bot = Frame(root)
e = Entry(fr_top, width=20, font='arial 20')
b1 = Button(fr_top, text='открыть', width=30)
b2 = Button(fr_top, text='сохранить', width=30)
b3 = Button(fr_top, text='пуск', width=30)
tx = Text(fr_bot, width=100, height=4, font='arial 15')
tx2 = Text(fr_bot, width=100, height=4, font='arial 15')
scroll = Scrollbar(command=tx.yview)
scroll.pack(side=LEFT, fill=Y)

tx.config(yscrollcommand=scroll.set)
def otr():
    tx.delete(1.0, END)
    x = e.get()
    if x == '': return
    f = open(x, 'r')
    stext = f.read()
    tx.insert(1.0, stext)
b1.config(command=otr)
def zapis():
    x = e.get()
    if x == '': return
    funk_file = open(x, 'w')
    read_text = tx.get('1.0', END)
    funk_file.write(read_text)
    funk_file.close()
b2.config(command=zapis)

def runfile():
    s = e.get()
    if s == '': return
    output = subprocess.check_output(f'python {e.get()}')
    tx.insert(1.0, output)
b3.config(command=runfile)


fr_top.pack()
fr_bot.pack()
e.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
tx.pack()
tx2.pack()

mainloop()

