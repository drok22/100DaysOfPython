from tkinter import *
from tkinter import messagebox
import pandas
from password_generator import PasswordGenerator
import pyperclip
import json

class PasswordGeneratorView():
    def __init__(self):
        # UI elements
        self.window = Tk()
        self.logo_img = PhotoImage(file="Password Generator/logo.png")
        self.canvas = Canvas(height=200, width=200)
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.website_label = Label(text="Website: ")
        self.website_entry = Entry(text="", width=28)
        self.search_button = Button(text="Search", command=self.find_password)
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
        self.website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
        self.website_entry.focus()
        self.search_button.grid(row=1, column=2, sticky=E)
        # Row 2
        self.username_label.grid(row=2, column=0, sticky=E)
        self.username_entry.grid(row=2, column=1, columnspan=2, sticky=W)
        self.username_entry.insert(0, "dustin.johns1@gmail.com")
        # Row 3
        self.password_label.grid(row=3, column=0, sticky=E)
        self.password_entry.grid(row=3, column=1, sticky=W)
        self.gen_password_button.grid(row=3, column=2, sticky=E)
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

        password_dict = {
            website_text: {
                "username": username_text,
                "password": password_text
            }
        }

        if len(website_text) == 0 or len(username_text) == 0 or len(password_text) == 0:
            messagebox.showinfo(message="Please fill out all of the fields before saving.")

        else:
            try:
                with open("Password Generator/data.json", "r") as data_file:
                    json_data = json.load(data_file)

            except FileNotFoundError:
                with open("Password Generator/data.json", "w") as data_file:
                    json.dump(password_dict, data_file, indent=4)

            else:
                json_data.update(password_dict)

                with open("Password Generator/data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)

            finally:
                messagebox.showinfo(title="", message=f"Password saved for {website_text}")
                self.clear_inputs()

    def find_password(self):
        website_text = self.website_entry.get()

        try:
            with open("Password Generator/data.json", "r") as data_file:
                json_data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        
        else:
            if website_text in json_data:
                username_text = json_data[website_text]["username"]
                password_text = json_data[website_text]["password"]
                messagebox.showinfo(title=website_text, message=f"User Name: {username_text}\nPassword: {password_text}")
            else:
                messagebox.showinfo(title=website_text, message=f"No password data found for {website_text}")
        
        finally:
            pass

    def clear_inputs(self):
        self.website_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.website_entry.focus()