from tkinter import messagebox
import random 
import tkinter
from tkinter import *
import custom_button
import main_menu
import os
import utils
from PIL import ImageTk, Image
from tkinter import Entry

import password_register
import password_login

def load_menu(window,frame):
    frame.pack_forget()
    main_menu.start(window)

def start(window):
    btn_font = ('Trebuchet MS', 16)
    window.title("Password Image Authentication System")
    password_selector = Frame(window, height=600, width=1280)
    password_selector.pack(fill='both', expand=1)
    img2 = Image.open("assets/register.png")
    img2 = img2.resize((50, 50))
    img2 = ImageTk.PhotoImage(img2)
    def login():
        password_selector.pack_forget()
        password_login.start(window)
    
    def register():
        password_selector.pack_forget()
        password_register.start(window)
        
    custom_button.TkinterCustomButton(master=window, text="Register", width=200, height=80, corner_radius=20, text_font=btn_font,fg_color="#999e9b",hover_color="#38f584",
                                      command=lambda: register, image=img2).place(relx=0.5, rely=0.3, anchor=CENTER)

    # Button to switch to the login page
    custom_button.TkinterCustomButton(master=window, text="Login", width=100,height=100, corner_radius=50,text_font=btn_font,fg_color="green",hover_color="#02ad49",
                                      command=lambda: login).place(relx=0.5, rely=0.5, anchor=CENTER)
    custom_button.TkinterCustomButton(master=window, text="Go Back", height=40, corner_radius=10,
                                      command=lambda: load_menu(window,password_selector)).place(relx=0.08, rely=0.08, anchor=CENTER)
    
   
