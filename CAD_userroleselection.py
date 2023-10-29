import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import Image, ImageTk

root=Tk()
root.geometry("1440x900")
root.title("User Role Selection")
frame=tk.Frame(root, width=1440, height=900)
frame.config(bg="#FFFFFF")
frame.pack()

logoi=Image.open("C:\DOC\Documents\ZzJS\Snips\CDA-Icon.png") #Change your path here
logophi=ImageTk.PhotoImage(logoi)
Logo2=Label(frame,image=logophi,bg="#FFFFFF")
Logo2.place(x=605,y=20)
Slogan2=Label(frame,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan2.place(x=450,y=185)
UserType=Label(frame,text="Select Role",font=("Roboto",30,"bold"),bg="#FFFFFF")
UserType.place(x=610,y=250)

img1=Image.open("C:\DOC\Documents\ZzJS\pStuff\patbtn.png") #Change your path here
phi1=ImageTk.PhotoImage(img1)
img2=Image.open("C:\DOC\Documents\ZzJS\pStuff\clcadminbtn.png") #Change your path here
phi2=ImageTk.PhotoImage(img2)
patbtn=tk.Button(frame,image=phi1, borderwidth=0, highlightthickness=0) #Patient Button(Leave the Command Empty)
patbtn.place(x=310,y=350)
clcadminbtn=tk.Button(frame, image=phi2, borderwidth=0, highlightthickness=0) #Clinic Admin Button
clcadminbtn.place(x=830,y=350)


root.mainloop()