import sqlite3
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

SMALL_PAD_Y_BOTTOM = (0, 3)


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
        formatted_output += f"{idx+1}. Website: {website}\nEmail: {email}\nPassword: {password}\n\n"

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
    user = email_text.get().strip()
    website = web_text.get().strip()
    password = pass_text.get().strip()

    if website == "" or password == "":
        messagebox.showinfo(message="Don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"Confirm {user} with password: {password}")
    if is_ok:
        save_password(website, user, password)
        web_text.delete(0, END)
        pass_text.delete(0, END)


# ---------------------------- View History------------------------------- #
def view_history():
    messagebox.showinfo(message=get_all_passwords())


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
logo = PhotoImage(file='logo.png')
bg_logo = Canvas(width=200, height=200, highlightthickness=0)
bg_logo.create_image(100, 100, anchor='center', image=logo)
bg_logo.grid(column=1, row=0)

# ----- Website -----
# Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky='e')
# Text Entry
web_text = Entry()
web_text.grid(column=1, row=1, columnspan=2, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM)
web_text.focus()

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
pass_text.grid(column=1, row=3, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM)
# Generate Button
gen_but = Button(text="Generate Password", command=generate_password)
gen_but.grid(column=2, row=3, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM)

# Add
# Button
add_but = Button(text="Add", command=save_data)
add_but.grid(column=1, row=4, sticky='nsew')

# View
view_but = Button(text="View history", command=view_history)
view_but.grid(column=2, row=4, sticky='nsew')

init_db()
window.mainloop()
