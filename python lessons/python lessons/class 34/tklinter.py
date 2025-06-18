from  tkinter import *

win = Tk()

win.title("Basic caluculator")

win.geometry("300x500")

def addfunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a + b
    result.config(text=f"add:{res}")

def subfunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a - b
    result.config(text=f"sub:{res}")

def mulfunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a * b
    result.config(text=f"add:{res}")

def divfunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a / b
    result.config(text=f"div:{res}")

def percentagefunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a % b
    result.config(text=f"percentage:{res}")

def powfunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a ** b
    result.config(text=f"pow:{res}")

def randomfunction():
    a = int(entry1.get())
    b = int(entry2.get())
    res = a ^ b
    result.config(text=f"random:{res}")

entry1 = Entry(win, width=20, borderwidth=3)
entry1.pack(pady=10)

entry2 = Entry(win, width=20, borderwidth=3)
entry2.pack(pady=10)

add = Button(win, text="+",width=10,borderwidth=3, command=addfunction)
add.pack(pady=10)

sub = Button(win, text="-",width=10,borderwidth=3, command=subfunction)
sub.pack(pady=10)

mul = Button(win, text="*",width=10,borderwidth=3, command=mulfunction)
mul.pack(pady=10)

div = Button(win, text="/",width=10,borderwidth=3, command=divfunction)
div.pack(pady=10)


pow = Button(win, text="**",width=10,borderwidth=3, command=powfunction)
pow.pack(padx=10)

percentage = Button(win, text="%",width=10,borderwidth=3, command=percentagefunction)
percentage.pack(pady=10)

random = Button(win, text="^",width=10,borderwidth=3, command=randomfunction)
random.pack(padx=10)

result = Label(win, text="Result", width=10, borderwidth=3)
result.pack(pady=10)

win.mainloop()
