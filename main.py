from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Courier"
FONT_SIZE = 10
FONT_TYPE = "bold"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Old Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)
    messagebox.showinfo(title="New Password", message="New Password has been copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"Login Details= {website}", message=f'Email/Username: {username}\n'
                                                                               f'Password: {password}')
        else:
            messagebox.showinfo(title="Error", message="No details for the website exits.")

# ---------------------------- SHOW ALL ------------------------------- #

def show_all():
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        messagebox.showinfo(title="Login Details", message=f'{data}')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website label and entry box
website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
website_label.grid(column=0, row=1)
website_entry = Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1)

# username/email label and entry box
username_label = Label(text="Username/Email:", font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
username_label.grid(column=0, row=2)
username_entry = Entry(width=41)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "franqpr10@hotmail.com")

# Password label and entry box
password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE, FONT_TYPE))
password_label.grid(column=0, row=3)
password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Search button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

# Generate Password button
genpass_button = Button(text="Generate Password", command=generate_password)
genpass_button.grid(column=2, row=3)

# ADD button
genpass_button = Button(text="Add", width=35, command=save)
genpass_button.grid(column=1, row=4, columnspan=2)

# Show_all button
show_all_button = Button(text="Show All", width=35, command=show_all)
show_all_button.grid(column=1, row=5, columnspan=2)

window.mainloop()

