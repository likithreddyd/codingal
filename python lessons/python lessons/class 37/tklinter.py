from tkinter import *

win = Tk()
win.title("Feedback form")
win.geometry('300x300')

def key_pressed(event):
    print("key pressed: {event.char}")
    label.config(text= f"keypressrd :{ event.char}")

def mousemove(event):
    print("mouse move: {event.x} {event.y}")
    label.config(text= f"mouse move :{ event.x} {event.y}")

label = Label(win, text="detect key press")
label.pack()

Label1 = Label(win, text="detect mouse movement",font=("Arial",15))
Label1.pack()

win.bind("<Key>", key_pressed)
win.bind("<Motion>", mousemove)

win.mainloop()