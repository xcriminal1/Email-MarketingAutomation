import tkinter as tk
from tkinter import messagebox, filedialog, StringVar, Radiobutton, Label, Button, Entry, Text, DISABLED, NORMAL, END, Toplevel
import os
import pandas as pd
from PIL import ImageTk
import code_email
import time

root = tk.Tk()

class Email:
    def __init__(self, root):
        self.root = root
        self.root.title("My Email Sender")
        self.root.geometry("1000x550+200+50")
        self.root.resizable(False, False)
        self.root.config(bg="skyblue")


    def setting_window(self):
        self.check_file_exist()
        self.root2 = Toplevel()
        self.root2.title("Setting")
        self.root2.resizable(False, False)
        self.root2.geometry("700x450+350+90")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="lightgrey")
        Label(self.root2, text="Bulk Email Sender", padx=10, compound=LEFT,
              font=("Goudy Old Style", 48, "bold"), bg="black", fg="white").place(x=0, y=0, relwidth=1)
        Label(self.root2, text="Enter your valid Email Id and Password", font=("Calibri (body)", 14),
              bg="yellow", fg="black").place(x=0, y=80, relwidth=1)
        Label(self.root2, text="Email Address", font=("times new roman", 18, "bold"), bg="lightgrey",
              fg="black").place(x=50, y=150)
        Label(self.root2, text="Password", font=("times new roman", 18, "bold"), bg="lightgrey",
              fg="black").place(x=50, y=200)
        self.uname_entry = Entry(self.root2, font=("times new roman", 18), bg="lightyellow")
        self.uname_entry.place(x=250, y=150, width=330, height=30)
        self.pasw_entry = Entry(self.root2, font=("times new roman", 18), bg="lightyellow", show="*")
        self.pasw_entry.place(x=250, y=200, width=330, height=30)

        Button(self.root2, activebackground="skyblue", text="SAVE", font=("times new roman", 20, "bold"),
               bg="black", fg="white", command=self.save_setting).place(x=250, y=250, width=130, height=30)
        Button(self.root2, activebackground="skyblue", text="CLEAR", font=("times new roman", 20, "bold"),
               bg="#ffcccb", command=self.setting_clear, fg="black").place(x=400, y=250, width=130, height=30)

        self.uname_entry.insert(0, self.uname)
        self.pasw_entry.insert(0, self.pasw)

    def check_file_exist(self):
        if not os.path.exists("important.txt"):
            with open('important.txt', 'w') as f:
                f.write(",")
        with open('important.txt', 'r') as f2:
            self.credentials = [line.strip().split(",") for line in f2]
        self.uname = self.credentials[0][0]
        self.pasw = self.credentials[0][1]

    def save_setting(self):
        if not self.uname_entry.get() or not self.pasw_entry.get():
            messagebox.showinfo("ERROR", "All fields are required", parent=self.root2)
        else:
            with open('important.txt', 'w') as f:
                f.write(self.uname_entry.get() + "," + self.pasw_entry.get())
            messagebox.showinfo("Success", "Email and password are saved successfully", parent=self.root2)
            self.check_file_exist()

obj = Email(root)
root.mainloop()