from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

default_email = "*@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    global password_input

    password_input.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    char_list = [random.choice(c) for c in letters][:nr_letters]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    symb_list = [random.choice(s) for s in symbols][:nr_symbols]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    num_list = [random.choice(n) for n in numbers][:nr_numbers]

    password_list += char_list
    password_list += symb_list
    password_list += num_list

    random.shuffle(password_list)

    # generated_password = ""
    # for char in password_list:
    #     generated_password += char

    generated_password = "".join([str(elem) for elem in password_list])

    # print(f"Your password is: {password}")

    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global default_email
    website = website_input.get().title()
    user = user_input.get()
    password = password_input.get()
    is_filled_out = True
    if website == "" or user == "" or password == "":
        messagebox.showinfo(title="Error", message="Please fill out all fields")
        is_filled_out = False
    if is_filled_out:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details you entered for {website}:\n Username: {user}\n Password: {password}\n \n Is it okay to save?")
        # if is_ok:
        #     f = open("passwords.txt", "a")
        #     f.write(f"{website} | {user} | {password} \n")
        #     f.close()
        #     default_email = user
        if is_ok:
            default_email = user
            new_data = {website: {
                "username": user,
                "password": password
            }}

            # read json file
            try:
                with open("passwords.json", "r") as password_file:
                    data = json.load(password_file)
            except FileNotFoundError:
                data = {}

            # updating json data
            data.update(new_data)

            # writing json data
            with open("passwords.json", "w") as password_file:
                json.dump(data, password_file, indent=4)

    clear_fields()


def clear_fields():
    global website_input
    global user_input
    global password_input

    website_input.delete(0, END)
    user_input.delete(0, END)
    user_input.insert(0, default_email)
    password_input.delete(0, END)


def find_password():
    website = website_input.get().title()

    # read json file
    try:
        with open("passwords.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="No websites have been saved yet")
    else:
        try:
            web_dict = data[website]
        except KeyError:
            messagebox.showinfo(title="Not Found", message="Website not found")
        else:
            username = web_dict["username"]
            password = web_dict["password"]
            messagebox.showinfo(title=website, message=f"Website: {website}\nUsername: {username}\nPassword: {password}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)

lock_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, sticky="W")
website_input.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=1, row=1, columnspan=2, sticky="E")

user_input = Entry(width=43)
user_input.grid(column=1, row=2, columnspan=2, sticky="W")
user_input.insert(0, default_email)

password_input = Entry(width=24)
password_input.grid(column=1, row=3, sticky="W")

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=1, row=3, columnspan=2, sticky="E")

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="W")

mainloop()
