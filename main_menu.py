# Import the required libraries
from tkinter import *
from tkinter import font
import custom_button
import garbled
import obscure
import password
import segments
import multi_level

def load_garbled(window, menu_frame):
    menu_frame.pack_forget()
    garbled.start(window)


def load_obscured(window, menu_frame):
    menu_frame.pack_forget()
    obscure.start(window)


def load_segmented(window, menu_frame):
    menu_frame.pack_forget()
    segments.start(window)


def load_password(window, menu_frame):
    menu_frame.pack_forget()
    password.start(window)

def sample_system(window,menu_frame):
    menu_frame.pack_forget()
    multi_level.start(window)

def start(win):
    win.geometry("1280x600")
    win.title("Graphical Authentication System")

    menu_frame = Frame(win, height=600, width=1280,bg="#F5F5DC")
    menu_frame.pack(fill='both', expand=1)

    label = Label(menu_frame, text="Main Menu", font=('Goudy Old Style', 35),bg="#F5F5DC")
    label.pack(padx=40, pady=30)

    btn_height = 90
    btn_width = 450
    btn_font = ('Footlight MT Light', 18,'bold')

    btn1 = custom_button.TkinterCustomButton(master=menu_frame, text="Garbled Image Authentication", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_garbled(win, menu_frame)).place(relx=0.3, rely=0.4,
                                                                                                  anchor=CENTER)
    btn2 = custom_button.TkinterCustomButton(master=menu_frame, text="Segmented Image Authentication", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_segmented(win, menu_frame)).place(relx=0.3,
                                                                                                    rely=0.6,
                                                                                                    anchor=CENTER)
    btn3 = custom_button.TkinterCustomButton(master=menu_frame, text="Obscured Image Authentication", text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_obscured(win, menu_frame)).place(relx=0.7,
                                                                                                   rely=0.4,
                                                                                                   anchor=CENTER)
    btn4 = custom_button.TkinterCustomButton(master=menu_frame, text="Password/Image Authentication",
                                             text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: load_password(win, menu_frame)).place(relx=0.7,
                                                                                                   rely=0.6,
                                                                                                   anchor=CENTER)
    btn5 = custom_button.TkinterCustomButton(master=menu_frame, text="Multi Level Authentication",
                                             text_font=btn_font,
                                             height=btn_height, width=btn_width, corner_radius=10,
                                             command=lambda: sample_system(win, menu_frame)).place(relx=0.5,
                                                                                                   rely=0.8,
                                                                                                   anchor=CENTER)                                       

    win.mainloop()


if __name__ == "__main__":
    win = Tk()
    start(win)





