import random
import string
import tkinter as tk
from tkinter import *
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Popsoft - PASSWORD GENERATOR")

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Popsoft', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root, text='Password LENGTH', font='arial 15 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# password_length = int(input('what is the length of your password'))

pass_str = StringVar()


def password_generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
        for letter in range(pass_len.get() - 4):
            password = password + random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
            pass_str.set(password)


Button(root, text="GENERATE PASSWORD", command=password_generator).pack(pady=5)
Entry(root, textvariabl=pass_str).pack()


# def email_generator():
#     first_name = input("enter the first name")
#     last_name = input("enter you last name")
#     email_gen = first_name[0] + "-" + last_name + "@semicolon.com"
#     print(email_gen)

def copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=5)

password_generator()
# copy_password()
# email_generator()
