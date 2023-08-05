import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def set_alarm():
    alarm_time = alarm_entry.get()
    try:
        datetime.strptime(alarm_time, '%H:%M')
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        current_time = datetime.now().strftime("%H:%M:%S")
        time_diff = datetime.strptime(alarm_time, "%H:%M") - datetime.strptime(current_time, "%H:%M:%S")
        root.after(time_diff.seconds * 1000, ring_alarm)

    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter a valid time in 24-hour format (HH:MM)")

def ring_alarm():
    messagebox.showinfo("Time's up!", "The alarm time has been reached|.")

root = tk.Tk()
root.title("Alarm Clock")

time_label = tk.Label(root, font=("Arial", 24))
time_label.pack(pady=20)

date_label = tk.Label(root, font=("Arial", 16))
date_label.pack(pady=10)

alarm_entry = tk.Entry(root, font=("Arial", 16))
alarm_entry.pack(pady=10)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

def update_date():
    current_date = datetime.now().strftime("%d-%m-%Y")
    date_label.config(text=current_date)
    root.after(60000, update_date)

update_time()
update_date()

root.mainloop()
