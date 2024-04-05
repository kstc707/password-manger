from tkinter import messagebox
from tkinter import *
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password1 = "".join(password_list)
    entry2.insert(0, f"{password1}")
    pyperclip.copy(password1)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry.get()
    email = entry1.get()
    password = entry2.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty. ")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file,indent=4)
        finally:
            entry2.delete(0,END)
            entry.delete(0,END)

def search():
    web = entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except UnboundLocalError:
        messagebox.showinfo(title="Error", message="No details for the website exists ")
    else:
        if web in data:
            E = data[web]["email"]
            P = data[web]["password"]
            messagebox.showinfo(title=f"{web}", message=f"Email:  {E} \nPassword:  {P}")
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label = Label(text="Website:")
label.grid(column=0, row=1)

label1 = Label(text="Email/Username:")
label1.grid(column=0, row=2)

label2 = Label(text="Password:")
label2.grid(column=0, row=3)

entry = Entry(width=32)
entry.grid(column=1, row=1)
entry.focus()

entry1 = Entry(width=51)
entry1.grid(column=1, row=2, columnspan=2)
entry1.insert(0,"kstc707@gmail.com")

entry2 = Entry(width=32)
entry2.grid(column=1, row=3)


button = Button(text="Generate Password", command=generate_password)
button.grid(column=2,  row=3)

button2 = Button(text="Search", width=13, command=search)
button2.grid(column=2, row=1)

button1 = Button(text="Add",width=45,command=save)
button1.grid(column=1, row=4, columnspan=2)

window.mainloop()