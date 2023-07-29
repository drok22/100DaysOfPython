from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip

class PasswordGeneratorView():
    def __init__(self):
        # UI elements
        self.window = Tk()
        self.logo_img = PhotoImage(file="Password Generator/logo.png")
        self.canvas = Canvas(height=200, width=200)
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.website_label = Label(text="Website: ")
        self.website_entry = Entry(text="", width=38)
        self.username_label = Label(text="Email/Username: ")
        self.username_entry = Entry(text="", width=38)
        self.password_label = Label(text="Password: ")
        self.password_entry = Entry(text="", width=21)
        self.gen_password_button = Button(text="Generate Password", command=self.generate_password)
        self.add_password_button = Button(text="Add Password", width=36, command=self.add_password)
        self.setup_ui()
        # Generator
        self.generator = PasswordGenerator()

    def setup_ui(self):
        # Window setup
        self.window.title("Password Manager")
        self.window.config(padx=50, pady = 50)

        # tkinter Grid Setup
        # Row 0
        self.canvas.grid(row= 0, column=1)
        # Row 1
        self.website_label.grid(row=1, column=0, sticky=E)
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.website_entry.focus()
        # Row 2
        self.username_label.grid(row=2, column=0, sticky=E)
        self.username_entry.grid(row=2, column=1, columnspan=2)
        self.username_entry.insert(0, "dustin.johns1@gmail.com")
        # Row 3
        self.password_label.grid(row=3, column=0, sticky=E)
        self.password_entry.grid(row=3, column=1)
        self.gen_password_button.grid(row=3, column=2)
        # Row 4
        self.add_password_button.grid(row=4, column=1, columnspan=2)
    
    def generate_password(self):
        password = self.generator.generate_password()
        self.password_entry.insert(0, password)
        self.copy_password_to_clipboard()
    
    def copy_password_to_clipboard(self):
        pyperclip.copy(self.password_entry.get())
        messagebox.showinfo(message="Password generated and copied to clipboard")

    def add_password(self):
        website_text = self.website_entry.get()
        username_text = self.username_entry.get()
        password_text = self.password_entry.get()

        if len(website_text) == 0 or len(username_text) == 0 or len(password_text) == 0:
            messagebox.showinfo(message="Please fill out all of the fields before saving.")

        else:
            '''
            is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nUser: {username_text} Password: {password_text} \nIs it ok to save?")
            if is_ok:
                with open() '''
            with open("Password Generator/data.txt", "a") as data_file:
                data_file.write(f"{website_text} | {username_text} | {password_text}\n")

            messagebox.showinfo(title="", message=f"Password saved for {website_text}")

            self.clear_inputs()

    def clear_inputs(self):
        self.website_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.website_entry.focus()