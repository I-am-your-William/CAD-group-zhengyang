import tkinter as tk
from tkinter import *
from tkinter import ttk
import  tkinter.messagebox
from PIL import ImageTk, Image
import sqlite3
from contextlib import closing
import webbrowser

root = Tk()
root.geometry('1000x700')
root.resizable(0,0)
root.title('Tips View')

def ViewTips():
    db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM TIPS")
    displayrecord = c.fetchall()
    
    i = 0
    for TIPS in displayrecord:
        tips_frame = Frame(frame_inner, background="white", highlightbackground="black", highlightthickness=1, width=880, height=180)
        tips_frame.grid(row=i, column=1, padx=1, pady=1)

        tips_label = Label(tips_frame, border=0, text=TIPS[1], font=("Helvetica", 16), background="white")
        tips_label.place(x=10, y=10)

        tips_description = Label(tips_frame, border=0, text=TIPS[2], font=("Helvetica", 12), background="white")
        tips_description.place(x=10, y=40)

        tips_link = Label(tips_frame, border=0, text= TIPS[3], font=("Helvetica", 10), fg="blue", cursor="hand2", background="white")
        tips_link.place(x=10, y=130)
        tips_link.bind("<Button-1>", lambda e, url=TIPS[3]: open_link(url))

        i += 1

    conn.close()

def open_link(url):
    webbrowser.open_new(url)



top_frame1 = Frame(root, background="#D2E0FB")
top_frame1.place(height=60, width=1000, x=1, y=1)

TipsView_label  = Label(top_frame1 ,  text="Health Tips For You", font=("Helvetica", 24),background = "#D2E0FB")
TipsView_label .pack()

frame2 = Frame(root, background="#D2E0FB")
frame2.place(height=550, width=900, x=55, y=100)

tips_canvas = Canvas(frame2, background="#F9F3CC")
tips_canvas.place(height=550, width=900, x=0, y=0)

scrollbar = Scrollbar(frame2, orient=VERTICAL, command=tips_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

tips_canvas.configure(yscrollcommand=scrollbar.set)
tips_canvas.bind('<Configure>', lambda _: tips_canvas.configure(scrollregion=tips_canvas.bbox("all")))
frame_inner = Frame(tips_canvas)
tips_canvas.create_window((0, 0), window=frame_inner, anchor="nw")

ViewTips()

root.mainloop()