import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import Image, ImageTk
import webbrowser

root=Tk()
root.geometry("1440x900")
root.title("Testing")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1=tk.Frame(root) #Login
frame2=tk.Frame(root) #User Type Selection
frame3=tk.Frame(root) #Patient Register
frame4=tk.Frame(root) #Homepage
frame5=tk.Frame(root) #Clinic Search
frame6=tk.Frame(root) #Download Prescription
frame7=tk.Frame(root) #Additional Medical Info

def show_frame(frame):
    frame.tkraise()

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7):
    frame.grid(row=0, column=0, sticky='nsew')
    frame.config(bg="#FFFFFF")

#F1 Login
logoi=Image.open("C:\DOC\Documents\ZzJS\Snips\CDA-Icon.png") #Change Image Path
logophi=ImageTk.PhotoImage(logoi)
Logo=Label(frame1,image=logophi,bg="#FFFFFF")
Logo.place(x=605,y=120)
Slogan=Label(frame1,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan.place(x=450,y=285)
uname=Label(frame1,text="Username:",font=("Roboto",16),bg="#FFFFFF")
uname.place(x=550,y=350)
unamebox=Entry(frame1,width=30,font=("Roboto",16), bd=2, bg="#B5DDF0")
unamebox.place(x=550,y=380)
pword=Label(frame1,text="Password:",font=("Roboto",16),bg="#FFFFFF")
pword.place(x=550,y=420)
pwordbox=Entry(frame1,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
pwordbox.place(x=550,y=450)
Login_Button=tk.Button(frame1, text="Login",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame4))
Login_Button.place(x=550,y=520)
Register_Button=tk.Button(frame1, text="Register",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame2))
Register_Button.place(x=780,y=520)



#F2 User Type Selection
Logo2=Label(frame2,image=logophi,bg="#FFFFFF")
Logo2.place(x=605,y=20)
Slogan2=Label(frame2,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan2.place(x=450,y=185)
UserType=Label(frame2,text="Select Role",font=("Roboto",30,"bold"),bg="#FFFFFF")
UserType.place(x=610,y=250)
img1=Image.open("C:\DOC\Documents\ZzJS\pStuff\patbtn.png")
phi1=ImageTk.PhotoImage(img1)
img2=Image.open("C:\DOC\Documents\ZzJS\pStuff\clcadminbtn.png")
phi2=ImageTk.PhotoImage(img2)
patbtn=tk.Button(frame2,image=phi1, borderwidth=0, highlightthickness=0,command=lambda:show_frame(frame3))
patbtn.place(x=310,y=350)
clcadminbtn=tk.Button(frame2, image=phi2, borderwidth=0, highlightthickness=0)
clcadminbtn.place(x=830,y=350)



#F3 Patient Register
Logo3=Label(frame3,image=logophi,bg="#FFFFFF")
Logo3.place(x=605,y=20)
Slogan3=Label(frame3,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan3.place(x=450,y=185)
patregisterlbl=Label(frame3,text="Patient Registration",font=("Roboto",30,"bold","underline"),bg="#FFFFFF")
patregisterlbl.place(x=520,y=240)
newpatient_uname=Label(frame3,text="Create New Username:",font=("Roboto",16),bg="#FFFFFF")
newpatient_uname.place(x=250,y=350)
patunamebox=Entry(frame3,width=30,font=("Roboto",16), bd=2, bg="#B5DDF0")
patunamebox.place(x=250,y=380)
newpatient_pword=Label(frame3,text="Create New Password:",font=("Roboto",16),bg="#FFFFFF")
newpatient_pword.place(x=250,y=450)
patpwordbox=Entry(frame3,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patpwordbox.place(x=250,y=480)
patname=Label(frame3,text="Full Name (as per IC/Passport):",font=("Roboto",16),bg="#FFFFFF")
patname.place(x=250,y=550)
patnamebox=Entry(frame3,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patnamebox.place(x=250,y=580)
paticno=Label(frame3,text="IC/Mykad No.:",font=("Roboto",16),bg="#FFFFFF")
paticno.place(x=250,y=650)
paticnobox=Entry(frame3,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
paticnobox.place(x=250,y=680)
patgender=Label(frame3,text="Gender:",font=("Roboto",16),bg="#FFFFFF")
patgender.place(x=830,y=350)
patgenderbox=ttk.Combobox(frame3,font=("Roboto",16),values=["Male","Female","Rather Not Say"],width=20)
patgenderbox.place(x=830,y=380)
patbloodtype=Label(frame3,text="Blood Type:",font=("Roboto",16),bg="#FFFFFF")
patbloodtype.place(x=830,y=450)
patbloodtypebox=ttk.Combobox(frame3,font=("Roboto",16),values=["A","B","AB","O"],width=20)
patbloodtypebox.place(x=830,y=480)
patallergies=Label(frame3,text="Allergies:",font=("Roboto",16),bg="#FFFFFF")
patallergies.place(x=830,y=550)
patallergiesbox=Entry(frame3,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patallergiesbox.place(x=830,y=580)
pataddress=Label(frame3,text="Address:",font=("Roboto",16),bg="#FFFFFF")
pataddress.place(x=830,y=650)
pataddressbox=Entry(frame3,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
pataddressbox.place(x=830,y=680)
patregisterbtn=tk.Button(frame3,text="Register",font=("Roboto",25,"bold"),bg="#054C76",fg="White",width=10)
patregisterbtn.place(x=610,y=750)



#F4 Homepage
canvas1 = tk.Canvas(frame4, width = 1440, height = 900, bg = "#FFFFFF", highlightthickness=0)
canvas1.pack()
canvas1.create_rectangle(0, 0, 1440, 100, fill="#B5DFF0", outline = "#054C76")
logoir1=logoi.resize((100,70))
logophir1=ImageTk.PhotoImage(logoir1)
canvas1.create_image(80, 50, image = logophir1)
canvas1.create_text(480, 50, text = "Call A Doctor Home Page (Patient)", font = ("Roboto", 30, "bold"), fill = "#004C7D")
logoutbtn=Button(frame4,text="Logout",font=("Roboto",24),bg="#054C76",fg="White",width=8,command=lambda:show_frame(frame1))
logoutbtn.place(x=1250,y=20)

#Left Panel(Navigation)
canvas1.create_rectangle(0, 150, 420, 900, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame4,text="Clinic Search",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame5))
clcsearch.place(x=50,y=200)
dlpres=Button(frame4,text="Download Prescription",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame6))
dlpres.place(x=50,y=400)
addmedinfo=Button(frame4,text="Additional Medical Info",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame7))
addmedinfo.place(x=50,y=600)

#Main Panel
canvas1.create_rectangle(520, 150, 1440, 900, fill="#B5DFF0", outline = "#054C76")



#F5 Clinic Search
canvas2 = tk.Canvas(frame5, width = 1440, height = 900, bg = "#FFFFFF", highlightthickness=0)
canvas2.pack()
canvas2.create_rectangle(0, 0, 1440, 100, fill="#B5DFF0", outline = "#054C76")
logoir2=logoi.resize((100,70))
logophir2=ImageTk.PhotoImage(logoir2)
returnhomebtn1=Button(frame5, image = logophir2,command=lambda:show_frame(frame4),borderwidth=0, highlightthickness=0)
returnhomebtn1.place(x=30,y=15)
canvas2.create_text(455, 50, text = "Search for Healthcare Facilities", font = ("Roboto", 30, "bold"), fill = "#004C7D")
logoutbtn=Button(frame5,text="Logout",font=("Roboto",24),bg="#054C76",fg="White",width=8,command=lambda:show_frame(frame1))
logoutbtn.place(x=1250,y=20)

#Left Panel(Navigation)
canvas2.create_rectangle(0, 150, 420, 900, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame5,text="Clinic Search",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame5))
clcsearch.place(x=50,y=200)
dlpres=Button(frame5,text="Download Prescription",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame6))
dlpres.place(x=50,y=400)
addmedinfo=Button(frame5,text="Additional Medical Info",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame7))
addmedinfo.place(x=50,y=600)

#Main Panel
canvas2.create_rectangle(520, 150, 1440, 900, fill="#B5DFF0", outline = "#054C76")

#F6 Download Prescription
canvas3 = tk.Canvas(frame6, width = 1440, height = 900, bg = "#FFFFFF", highlightthickness=0)
canvas3.pack()
canvas3.create_rectangle(0, 0, 1440, 100, fill="#B5DFF0", outline = "#054C76")
logoir3=logoi.resize((100,70))
logophir3=ImageTk.PhotoImage(logoir3)
returnhomebtn2=Button(frame6, image = logophir3,command=lambda:show_frame(frame4),borderwidth=0, highlightthickness=0)
returnhomebtn2.place(x=30,y=15)
canvas3.create_text(440, 50, text = "Save Your Prescriptions Here", font = ("Roboto", 30, "bold"), fill = "#004C7D")
logoutbtn=Button(frame6,text="Logout",font=("Roboto",24),bg="#054C76",fg="White",width=8,command=lambda:show_frame(frame1))
logoutbtn.place(x=1250,y=20)

#Left Panel(Navigation)
canvas3.create_rectangle(0, 150, 420, 900, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame6,text="Clinic Search",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame5))
clcsearch.place(x=50,y=200)
dlpres=Button(frame6,text="Download Prescription",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame6))
dlpres.place(x=50,y=400)
addmedinfo=Button(frame6,text="Additional Medical Info",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame7))
addmedinfo.place(x=50,y=600)

#Main Panel
canvas3.create_rectangle(520, 150, 1440, 900, fill="#B5DFF0", outline = "#054C76")

#F7 Additional Medical Info
canvas4 = tk.Canvas(frame7, width = 1440, height = 900, bg = "#FFFFFF", highlightthickness=0)
canvas4.pack()
canvas4.create_rectangle(0, 0, 1440, 100, fill="#B5DFF0", outline = "#054C76")
logoir4=logoi.resize((100,70))
logophir4=ImageTk.PhotoImage(logoir4)
returnhomebtn3=Button(frame7, image = logophir4,command=lambda:show_frame(frame4),borderwidth=0, highlightthickness=0)
returnhomebtn3.place(x=30,y=15)
canvas4.create_text(345, 50, text = "Medical Information", font = ("Roboto", 30, "bold"), fill = "#004C7D")
logoutbtn=Button(frame7,text="Logout",font=("Roboto",24),bg="#054C76",fg="White",width=8,command=lambda:show_frame(frame1))
logoutbtn.place(x=1250,y=20)

#Left Panel(Navigation)
canvas4.create_rectangle(0, 150, 420, 900, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame7,text="Clinic Search",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame5))
clcsearch.place(x=50,y=200)
dlpres=Button(frame7,text="Download Prescription",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame6))
dlpres.place(x=50,y=400)
addmedinfo=Button(frame7,text="Additional Medical Info",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame7))
addmedinfo.place(x=50,y=600)

#Main Panel
canvas4.create_rectangle(520, 150, 1440, 900, fill="#B5DFF0", outline = "#054C76")




show_frame(frame1)
root.mainloop()