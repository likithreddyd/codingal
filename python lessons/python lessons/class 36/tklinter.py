from  tkinter import *

win = Tk()
win.title("feedback")
win.geometry("500x500")

def saveinofo():
  print("hello")
  usernameinfo = Entryun.get()
  emailinfo = Entryemail.get()
  phonenumberinfo = Entryphonenumber.get()
  reviewtextinfo = Textarea.get(1.0, END)

  datadict = {
      "Username": usernameinfo,
      "Email": emailinfo,
      "Phone Number": phonenumberinfo,
      "Review": reviewtextinfo
  }

  with open(r"C:\Users\Likithreddy\OneDrive\Desktop\codingal\python lessons\feedback.txt", "a") as file:
     file.write(str(datadict) + "\n")
  

username = Label(win, text="username", font=("Arial ", 15))
username.grid(row=0, column=0 , padx=5, pady=10)

Entryun = Entry(win, font=("Arial ", 15))
Entryun.grid(row=0, column=1 , padx=5, pady=10)

email = Label(win, text="email", font=("Arial ", 15))
email.grid(row=1, column=0 , padx=5, pady=10)

Entryemail = Entry(win, font=("Arial ", 15))
Entryemail.grid(row=1, column=1 , padx=5, pady=10)

phonenumberlabel = Label(win, text="phonenumber", font=("Arial ", 15))
phonenumberlabel.grid(row=2, column=0 , padx=5, pady=10)

Entryphonenumber = Entry(win, font=("Arial ", 15))
Entryphonenumber.grid(row=2, column=1 , padx=5, pady=10)

reviewtext = Label(win, text="reviewtext", font=("Arial ", 15))
reviewtext.grid(row=3, column=0 , padx=5, pady=10)

Textarea = Text(win, font=("Arial ", 15))
Textarea.grid(row=3, column=1 , padx=5, pady=10)

sbmit = Button(win, text="submit", font=("Arial ", 15),command=saveinofo)
sbmit.grid(row=4, column=1 , padx=20, pady=10)

win.mainloop()