from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2,4))]
    numbers_list = [choice(numbers) for _ in range(randint(2,4))]

    result = letters_list + symbols_list + numbers_list
    shuffle(result)
    result = ''.join(result)

    pwd_entry.delete(0, END)
    pwd_entry.insert(0, result)
    pyperclip.copy(result)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Fill in!", message="You've left some fields empty!\n"
                                                      "Don't do that!"
                                                      )
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pwd_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = web_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Data error", message="No Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Data error", message="Data File Is Empty")
    else:
        if website in data.keys():
            email = data[website]['email']
            pwd = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {pwd}")
        else:
            messagebox.showinfo(title=f"Search error", message=f"{website} was not found!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=W)

pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0, sticky=W)

# Entries
web_entry = Entry(width=51)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
web_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0,"taki_tam@probny.email")

pwd_entry = Entry(width=33)
pwd_entry.grid(row=3, column=1, sticky=W)

# Buttons
search_butt = Button(text="Search", bd=1, width=14, command=find_password)
search_butt.grid(row=1, column=2, sticky=E)

gen_pwd_butt = Button(text="Generate Password", bd=1, command=generate_password)
gen_pwd_butt.grid(row=3, column=2, sticky=W)

add_butt = Button(text="Add", width=43, bd=1, command=save)
add_butt.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
