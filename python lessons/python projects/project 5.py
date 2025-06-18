import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        si = (p * r * t) / 100
        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

win = tk.Tk()
win.title("Interest Calculator")
win.geometry("300x300")

tk.Label(win, text="Principal Amount:").pack(pady=5)
principal_entry = tk.Entry(win)
principal_entry.pack()

tk.Label(win, text="Rate of Interest (%):").pack(pady=5)
rate_entry = tk.Entry(win)
rate_entry.pack()

tk.Label(win, text="Time (years):").pack(pady=5)
time_entry = tk.Entry(win)
time_entry.pack()

tk.Button(win, text="Calculate", command=calculate_interest).pack(pady=10)

result_label = tk.Label(win, text="", fg="blue")
result_label.pack()

win.mainloop()
