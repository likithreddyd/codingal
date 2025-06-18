import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        strength_label.config(text="Please enter a password", fg="red")
    elif length < 5:
        strength_label.config(text="Weak Password", fg="red")
    elif length < 8:
        strength_label.config(text="Moderate Password", fg="orange")
    else:
        strength_label.config(text="Strong Password", fg="green")

win = tk.Tk()
win.title("Password Strength Checker")
win.geometry("300x200")

tk.Label(win, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(win, show="*")
password_entry.pack()

tk.Button(win, text="Check Strength", command=check_strength).pack(pady=10)

strength_label = tk.Label(win, text="", font=('Arial', 12))
strength_label.pack()

win.mainloop()
