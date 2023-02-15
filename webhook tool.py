# https://github.com/loupblueredyt (Loup-BlueRed#9866)

from discord_webhook import DiscordWebhook
import tkinter.messagebox
from tkinter import *
import tkinter as tk
import time
import os
import requests

root= tk.Tk()
root.geometry('500x550')

# Entry 1

root.title("Webhook Tool")
canvas1 = tk.Canvas(root, width=400, height=190)
canvas1.pack()

entry1 = tk.Entry(root) 
canvas1.create_window(200, 140,height=20, width=280 , window=entry1)

label2 = tk.Label(root, text='Webhook:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

def get_webhook():
    webhook = entry1.get()
    
    def delete():
        requests.delete(webhook)
        check = requests.get(webhook)
        if check.status_code == 404:
            tkinter.messagebox.showinfo("Webhook Tool", "Webhook Deleted")
            os.system("pause >nul")
        elif check.status_code == 200:
            tkinter.messagebox.showerror("Webhook Tool", "Failed")
            os.system("pause >nul")

    test = requests.get(webhook)
    if test.status_code == 404:
        tkinter.messagebox.showinfo("Webhook Tool", "Webhook Invalid")
        os.system("pause >nul")
        root.destroy()
    elif test.status_code == 200:
        if "discord.com/api/webhook" in webhook:
            tkinter.messagebox.showinfo("Webhook Tool", "Webhook Valid")
            root.destroy()
            delete()

button1 = tk.Button(text='Delete', command=get_webhook)
canvas1.create_window(200, 180, window=button1)

# Entry 2

canvas2 = tk.Canvas(root, width=400, height=190)
canvas2.pack()

entry2 = tk.Entry(root) 
canvas2.create_window(200, 140,height=20, width=280 , window=entry2)

label2 = tk.Label(root, text='Message:')
label2.config(font=('helvetica'))
canvas2.create_window(200, 100, window=label2)

def get_msg():
    msg = entry2.get()
    webhook = entry1.get()
    webhook = DiscordWebhook(url=(webhook), rate_limit_retry=True,
    content=(msg))
    response = webhook.execute()

button2 = tk.Button(text='Send', command=get_msg)
canvas2.create_window(200, 180, window=button2)

#Check 

canvas3 = tk.Canvas(root, width=400, height=190)
canvas3.pack()

entry3 = tk.Entry(root) 

label3 = tk.Label(root)
label3.config(font=('helvetica'))

canvas3.create_window(200, 100, window=label3)

def check_webhook():
    webhook = entry1.get()
    test = requests.get(webhook)
    if test.status_code == 404:

        tkinter.messagebox.showerror("Webhook Tool", "Webhook Invalid")
        os.system("pause >nul")
        root.destroy()
        exit()
    elif test.status_code == 200:
        if "discord.com/api/webhook" in webhook:
            tkinter.messagebox.showinfo("Webhook Tool", "Webhook Valid")
            root.destroy()
            exit()

button3 = tk.Button(text='Check Webhook', command=check_webhook)
canvas3.create_window(200, 100, window=button3)

root.mainloop()
