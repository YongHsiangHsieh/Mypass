import os
import sqlite3
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

SMALL_PAD_Y_BOTTOM = (0, 5)
SMALL_PAD_X_RIGHT = (0, 3)


# ---------------------------- JSON ------------------------------- #
def update_json_file(file_path, new_data):
    try:
        # Initialize data as an empty dictionary
        data = {}

        # Check if the file exists and is not empty
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as data_file:
                data = json.load(data_file)

        # Update the data
        data.update(new_data)

        # Write the updated data back to the file
        with open(file_path, 'w') as data_file:
            json.dump(data, data_file, indent=4)

    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")


# ---------------------------- Database ------------------------------- #
def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (website TEXT, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()


def save_password(website, email, password):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?, ?, ?)", (website, email, password))
    conn.commit()
    conn.close()


def get_all_passwords():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")
    records = c.fetchall()
    conn.close()

    # Check if records are empty
    if not records:
        return "No passwords found in the database."

    # Format the output
    formatted_output = "All Stored Passwords:\n\n"
    for idx, (website, email, password) in enumerate(records):
        formatted_output += f"{idx + 1}. Website: {website}\nEmail: {email}\nPassword: {password}\n\n"

    return formatted_output


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_text.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(2, 4)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for _ in range(nr_letters)] +
                     [random.choice(symbols) for _ in range(nr_symbols)] +
                     [random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = ''.join(password_list)

    pass_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    email = email_text.get().strip()
    website = web_text.get().strip()
    password = pass_text.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(message="Don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(message=f"{website}\n{email}\npassword: {password}\n")
    if is_ok:
        update_json_file('data.json', new_data)
        save_password(website, email, password)
        web_text.delete(0, END)
        pass_text.delete(0, END)


# ---------------------------- View History------------------------------- #

def search():
    website = web_text.get()
    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="File not found")
    except Exception as e:
        messagebox.showinfo(message="File is empty, no data found")
        print(f"Got error: {e}")
    else:
        if website in data:
            messagebox.showinfo(message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}\n")
            view_history()
        else:
            messagebox.showinfo(message=f"Password not found for {website}")


def view_history():
    print(get_all_passwords())


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.wm_resizable(False, False)
window.config(padx=50, pady=50)

# logo
logo = PhotoImage(file='logo.png')
bg_logo = Canvas(width=200, height=200)
bg_logo.create_image(100, 100, anchor='center', image=logo)
bg_logo.grid(column=1, row=0)

# ----- Website -----
# Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky='e')
# Text Entry
web_text = Entry()
web_text.grid(column=1, row=1, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM, padx=SMALL_PAD_X_RIGHT)
web_text.focus()
# Search button
search_but = Button(text="Search", width=15, command=search)
search_but.grid(column=2, row=1)

# ----- Email/Username -----
# Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky='e')
# Email Entry
email_text = Entry()
email_text.grid(column=1, row=2, columnspan=2, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM)
email_text.insert(0, "Wilson@email.com")

# ----- Password -----
# Label
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3, sticky='e')
# Password Entry
pass_text = Entry()
pass_text.grid(column=1, row=3, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM, padx=SMALL_PAD_X_RIGHT)
# Generate Button
gen_but = Button(text="Generate Password", command=generate_password)
gen_but.grid(column=2, row=3, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM)

# Add
# Button
add_but = Button(text="Add", command=save_data)
add_but.grid(column=1, row=4, columnspan=2, sticky='nsew')

init_db()
window.mainloop()
