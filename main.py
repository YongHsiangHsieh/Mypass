from tkinter import *

SMALL_PAD_Y_BOTTOM = (0, 3)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    with open('data.txt', mode='a') as data:
        user = email_text.get()
        website = web_text.get()
        password = pass_text.get()
        data.write(f"{user} => Website: {website}, Password: {password}\n")
    web_text.delete(0, END)
    pass_text.delete(0, END)


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
gen_but = Button(text="Generate Password")
gen_but.grid(column=2, row=3, sticky='nsew', pady=SMALL_PAD_Y_BOTTOM)

# Add
# Button
add_but = Button(text="Add", command=save_data)
add_but.grid(column=1, row=4, columnspan=2, sticky='nsew')

window.mainloop()
