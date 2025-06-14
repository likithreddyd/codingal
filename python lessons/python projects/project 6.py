import tkinter as tk
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        birth_date = date(year, month, day)

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid date values.")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Enter Date of Birth").grid(row=0, column=1)

tk.Label(root, text="Day:").grid(row=1, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=1, column=1)

tk.Label(root, text="Month:").grid(row=2, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1)

tk.Label(root, text="Year:").grid(row=3, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1)

tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=4, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1)

root.mainloop()
