import tkinter as tk
from tkinter import * 
from tkinter import ttk, messagebox, Toplevel
from PIL import Image, ImageTk
from datetime import datetime
from validate_email import validate_email
import webbrowser
import tkintermapview as tkmap
import smtplib
import sqlite3 




root=Tk()
root.geometry("1000x700")
root.title("CAD-Beta")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1=tk.Frame(root) #Login
frame2=tk.Frame(root) #Role Select
frame3=tk.Frame(root) #Patient Register
frame4=tk.Frame(root) #Clinic Register
frame5=tk.Frame(root) #Patient Homepage
frame6=tk.Frame(root) #Clinic Search
frame7=tk.Frame(root) #Download Prescription
frame8=tk.Frame(root) #Additional Medical Info


def show_frame(frame):
    frame.tkraise()

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
    frame.grid(row=0, column=0, sticky='nsew')
    frame.config(bg="#FFFFFF")


db = sqlite3.connect('cadtest1.db')
cursor = db.cursor()

#F1 Login
logoi=Image.open("C:/Users/Joe Shen/Documents/Project Stuff/projectimg/CAD-Icon.png") #Change Image Path
logophi=ImageTk.PhotoImage(logoi)
Logo=Label(frame1,image=logophi,bg="#FFFFFF")
Logo.place(x=383,y=20)
Slogan=Label(frame1,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan.place(x=230,y=200)
uname=Label(frame1,text="Username:",font=("Roboto",16),bg="#FFFFFF")
uname.place(x=333,y=290)
unamebox=Entry(frame1,width=30,font=("Roboto",16), bd=2, bg="#B5DDF0")
unamebox.place(x=333,y=320)
pword=Label(frame1,text="Password:",font=("Roboto",16),bg="#FFFFFF")
pword.place(x=333,y=360)
pwordbox=Entry(frame1,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
pwordbox.place(x=333,y=390)
forgetpword=Label(frame1,text="Forgot Password?",font=("Roboto",16),bg="#FFFFFF")
forgetpword.place(x=333,y=430)
forgetpword.bind("<Button-1>",lambda e:pwordpopup())
Login_Button=tk.Button(frame1, text="Login",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame5))
Login_Button.place(x=333,y=490)
Register_Button=tk.Button(frame1, text="Register",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame2))
Register_Button.place(x=569,y=490)



#Password Reset Popup
def pwordpopup():
    pwordpopup=Toplevel(root)
    pwordpopup.geometry("400x400")
    pwordpopup.title("Password Reset")
    pwordpopup.config(bg="#FFFFFF")
    pwordpopup.grab_set()

    premail=Label(pwordpopup,text="Email Address:",font=("Roboto",16),bg="#FFFFFF")
    premail.place(x=30,y=40)
    premailbox=Entry(pwordpopup,width=25,font=("Roboto",16),bd=2,bg="#B5DDF0")
    premailbox.place(x=30,y=70)
    prnwpword=Label(pwordpopup,text="New Password:",font=("Roboto",16),bg="#FFFFFF")
    prnwpword.place(x=30,y=120)
    prnwpwordbox=Entry(pwordpopup,width=25,font=("Roboto",16),bd=2,bg="#B5DDF0")
    prnwpwordbox.place(x=30,y=150)
    resetpwordbtn=Button(pwordpopup,text="Reset Password",font=("Roboto",20),bg="#054C76",fg="White",width=15,command=lambda:change_password())
    resetpwordbtn.place(x=70,y=250)

    def change_password():
        if premailbox.get()!='':
            query = 'SELECT * FROM PatientInfo WHERE emailadd = ?'
            cursor.execute(query, (premailbox.get(),))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Email address doesn't exist")
                pwordpopup.destroy()
            
            else:
                query = '''UPDATE PatientInfo SET password = ? WHERE emailadd = ?'''
                cursor.execute(query, (prnwpwordbox.get(), premailbox.get()))
                db.commit()
                db.close()
                messagebox.showinfo("Success", "Password resetted.")
                #Email Constraints
                sender = "p22014733@student.newinti.edu.my"
                recipient = premailbox.get()
                subject = " CAD - Your Password has been modified."
                message = "Your password has been modified. If you did not make this change, please contact us immediately at 03-12345678."

                #Format Email
                email = "Subject: {}\n\n{}".format(subject, message)

                #Get Sender Email
                password_file = open("pword.txt", "r")
                password = password_file.readline()
                password_file.close()

                #SMTP Session
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()

                #Authentication
                s.login(sender, password)

                #Send Email
                s.sendmail(sender, recipient, email)

                #Terminate Session
                s.quit()
                messagebox.showinfo("Email Sent", "An email has been sent to the relevant email for security purposes.")


#F2 Role Select
userrole = None
def assignrole(widget):
    global userrole
    userrole = widget.winfo_name()
    if userrole == "patient":
        show_frame(frame3)
    elif userrole == "cadmin":
        show_frame(frame4)

Logo2=Label(frame2,image=logophi,bg="#FFFFFF")
Logo2.place(x=383,y=20)
Slogan2=Label(frame2,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan2.place(x=230,y=200)
UserType=Label(frame2,text="Select Role",font=("Roboto",30,"bold"),bg="#FFFFFF")
UserType.place(x=390,y=230)
img1=Image.open("C:/Users/Joe Shen/Documents/Project Stuff/projectimg/patbtn2.png")
phi1=ImageTk.PhotoImage(img1)
img2=Image.open("C:/Users/Joe Shen/Documents/Project Stuff/projectimg/clcadminbtn2.png")
phi2=ImageTk.PhotoImage(img2)
patbtn=tk.Button(frame2,image=phi1, name="patient", borderwidth=0, highlightthickness=0,command=lambda:assignrole(patbtn))
patbtn.place(x=180,y=320)
clcadminbtn=tk.Button(frame2, image=phi2, name="cadmin", borderwidth=0, highlightthickness=0,command=lambda:assignrole(clcadminbtn))
clcadminbtn.place(x=600,y=320)
backbtn=tk.Button(frame2, text="Back",bg="#054C76",fg="White",width=8,font='Roboto 16',command=lambda:show_frame(frame1))
backbtn.place(x=445,y=640)



#F3 Patient Register

def test_validation():
    # Define a dictionary to map each widget to its validation rules
    validation_rules = {
        patunamebox: [
            {
                "func": lambda x: x.isalnum(),
                "error_message": "Username must contain only alphanumeric characters",
            },
            {
                "func": lambda x: 5 < len(x) < 12,
                "error_message": "Username must be between 5 to 12 characters",
            }
        ],
        patpwordbox: [
            {
                "func": lambda x: 5 < len(x) < 20,
                "error_message": "Password must be between 5 to 20 characters",
            },
        ],
        patemailaddbox: [
            {
                "func": lambda x: validate_email(x,verify=True),
                "error_message": "Invalid email address",
            },
        ],
        patnamebox: [
            {
                "func": lambda x: all(char.isalpha() or char.isspace() for char in x),
                "error_message": "Name must contain only alphabets",
            },
        ],
        paticnobox: [
            {
                "func": lambda x: x.isdigit(),
                "error_message": "IC/Mykad number must contain only digits",
            },
            {
                "func": lambda x: len(x) == 12,
                "error_message": "IC/Mykad number must be 12 digits",
            }
        ],
        patcontactnobox: [
            {
                "func": lambda x: x.isdigit(),
                "error_message": "Contact number must contain only digits",
            },
            {
                "func": lambda x: len(x) == 10,
                "error_message": "Contact number must be 10 digits",
            }
        ],
        patgenderbox: [
            {
                "func": lambda x: x in ["Male", "Female"],
                "error_message": "Invalid gender",
            },
        ],
        patbloodtypebox: [
            {
                "func": lambda x: x in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                "error_message": "Invalid blood type",
            },
        ],
        pataddressbox: [
            {
                "func": lambda x: len(x) > 10,
                "error_message": "Address cannot be empty",
            },
        ],
        patallergiesbox: [
            {
                "func": lambda x: all(char.isalnum() or char.isspace() for char in x) or len(x) == 0,
                "error_message": "Invalid allergies",
            },
        ],
        }

    for widget in frame3.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox)) and widget in validation_rules:
                rules = validation_rules[widget]
                for rule in rules:
                    if not rule["func"](widget.get()):
                        messagebox.showerror("Error", rule["error_message"])
                        return False

    return True

def patregister():
    if not test_validation():
        return  # Validation failed

    # Get the current date and time
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Insert data into the database
    cursor.execute("""
        INSERT INTO PatientInfo (username, password, emailadd, fullname, icno, gender, bloodtype, contactno, address, allergies, datecreated)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patunamebox.get(),
        patpwordbox.get(),
        patemailaddbox.get(),
        patnamebox.get(),
        paticnobox.get(),
        patgenderbox.get(),
        patbloodtypebox.get(),
        patcontactnobox.get(),
        pataddressbox.get(),
        patallergiesbox.get(),
        current_date_time
    ))

    # Commit the changes and close the connection
    db.commit()
    db.close()

    # Optionally, you can show a success message or navigate to another frame
    messagebox.showinfo("Success", "Registration successful!")
    # Add code to navigate to another frame if needed



Logo3=Label(frame3,image=logophi,bg="#FFFFFF")
Logo3.place(x=383,y=10)
Slogan3=Label(frame3,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan3.place(x=230,y=190)
patregisterlbl=Label(frame3,text="Patient Registration",font=("Roboto",30,"bold","underline"),bg="#FFFFFF")
patregisterlbl.place(x=310,y=220)
newpatient_uname=Label(frame3,text="Create New Username:  (Max12)",font=("Roboto",16),bg="#FFFFFF")
newpatient_uname.place(x=20,y=280)
patunamebox=Entry(frame3, name="username", width=30,font=("Roboto",16), bd=2, bg="#B5DDF0")
patunamebox.place(x=20,y=310)
newpatient_pword=Label(frame3,text="Create New Password:  (Max12)",font=("Roboto",16),bg="#FFFFFF")
newpatient_pword.place(x=20,y=350)
patpwordbox=Entry(frame3, name="password",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patpwordbox.place(x=20,y=380)
patemailadd=Label(frame3,text="Email Address:",font=("Roboto",16),bg="#FFFFFF")
patemailadd.place(x=20,y=420)
patemailaddbox=Entry(frame3, name="email address",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patemailaddbox.place(x=20,y=450)
patname=Label(frame3,text="Full Name (as per IC/Passport):",font=("Roboto",16),bg="#FFFFFF")
patname.place(x=20,y=490)
patnamebox=Entry(frame3, name="full name",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patnamebox.place(x=20,y=520)
paticno=Label(frame3,text="IC/Mykad No.:",font=("Roboto",16),bg="#FFFFFF")
paticno.place(x=20,y=550)
paticnobox=Entry(frame3, name="icno",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
paticnobox.place(x=20,y=580)
patgender=Label(frame3,text="Gender:",font=("Roboto",16),bg="#FFFFFF")
patgender.place(x=600,y=280)
patgenderbox=ttk.Combobox(frame3, name="gender",font=("Roboto",16),values=["Male","Female"],width=20)
patgenderbox.place(x=600,y=310)
patbloodtype=Label(frame3,text="Blood Type:",font=("Roboto",16),bg="#FFFFFF")
patbloodtype.place(x=600,y=350)
patbloodtypebox=ttk.Combobox(frame3, name="bloodtype",font=("Roboto",16),values=["A+","A-","B+","B-","AB+","AB-","O+","O-"],width=20)
patbloodtypebox.place(x=600,y=380)
patcontactno=Label(frame3,text="Contact No.:",font=("Roboto",16),bg="#FFFFFF")
patcontactno.place(x=600,y=420)
patcontactnobox=Entry(frame3, name="contactno",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patcontactnobox.place(x=600,y=450)
pataddress=Label(frame3,text="Address:",font=("Roboto",16),bg="#FFFFFF")
pataddress.place(x=600,y=490)
pataddressbox=Entry(frame3, name="address",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
pataddressbox.place(x=600,y=520)
patallergies=Label(frame3,text="Allergies:",font=("Roboto",16),bg="#FFFFFF")
patallergies.place(x=600,y=560)
patallergiesbox=Entry(frame3, name="allergies",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patallergiesbox.place(x=600,y=590)
patregisterbtn=tk.Button(frame3,text="Register",font=("Roboto",20,"bold"),bg="#054C76",fg="White",width=10,command=lambda:patregister())
patregisterbtn.place(x=407,y=640)
backbtn2=tk.Button(frame3, text="Back",bg="#054C76",fg="White",width=8,font='Roboto 16',command=lambda:show_frame(frame2))
backbtn2.place(x=10,y=10)



#F4 Clinic Register
#Paste ZY's Register Page Here



#F5 Homepage
canvas1 = tk.Canvas(frame5, width = 1000, height = 700, bg = "#FFFFFF", highlightthickness=0)
canvas1.pack()
canvas1.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline = "#054C76")
logoir1=logoi.resize((80,50))
logophir1=ImageTk.PhotoImage(logoir1)
canvas1.create_image(50, 35, image = logophir1)
canvas1.create_text(320, 35, text = "Call A Doctor Home Page (Patient)", font = ("Roboto", 20, "bold"), fill = "#004C7D")
logoutbtn=Button(frame5,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas1.create_window(920, 35, window = logoutbtn)

#Left Panel(Navigation)
canvas1.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame5,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas1.create_window(125, 150, window = clcsearch)
dlpres=Button(frame5,text="Download Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas1.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame5,text="Additional Medical Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas1.create_window(125, 550, window = addmedinfo)

#Main Panel
canvas1.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")



#F6 Clinic Search
canvas2 = tk.Canvas(frame6, width = 1000, height = 700, bg = "#FFFFFF", highlightthickness=0)
canvas2.pack()
canvas2.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline = "#054C76")
logoir2=logoi.resize((80,50))
logophir2=ImageTk.PhotoImage(logoir2)
returnhomebtn1=Button(frame6, image = logophir2,command=lambda:show_frame(frame5),borderwidth=0, highlightthickness=0)
canvas2.create_window(50, 35, window = returnhomebtn1)
canvas2.create_text(320, 35, text = "Search for Healthcare Facilities", font = ("Roboto", 20, "bold"), fill = "#004C7D")
logoutbtn=Button(frame6,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas2.create_window(920, 35, window = logoutbtn)

#Left Panel(Navigation)
canvas2.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame6,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas2.create_window(125, 150, window = clcsearch)
dlpres=Button(frame6,text="Download Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas2.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame6,text="Additional Medical Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas2.create_window(125, 550, window = addmedinfo)

#Main Panel
canvas2.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")

#F7 Download Prescription
canvas3 = tk.Canvas(frame7, width = 1000, height = 700, bg = "#FFFFFF", highlightthickness=0)
canvas3.pack()
canvas3.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline = "#054C76")
logoir3=logoi.resize((80,50))
logophir3=ImageTk.PhotoImage(logoir3)
returnhomebtn2=Button(frame7, image = logophir3,command=lambda:show_frame(frame5),borderwidth=0, highlightthickness=0)
canvas3.create_window(50, 35, window = returnhomebtn2)
canvas3.create_text(320, 35, text = "Download Your Prescriptions", font = ("Roboto", 20, "bold"), fill = "#004C7D")
logoutbtn=Button(frame7,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas3.create_window(920, 35, window = logoutbtn)

#Left Panel(Navigation)
canvas3.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame7,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas3.create_window(125, 150, window = clcsearch)
dlpres=Button(frame7,text="Download Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas3.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame7,text="Additional Medical Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas3.create_window(125, 550, window = addmedinfo)

#Main Panel
canvas3.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")

#F8 Additional Medical Info
canvas4 = tk.Canvas(frame8, width = 1000, height = 700, bg = "#FFFFFF", highlightthickness=0)
canvas4.pack()
canvas4.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline = "#054C76")
logoir4=logoi.resize((80,50))
logophir4=ImageTk.PhotoImage(logoir4)
returnhomebtn3=Button(frame8, image = logophir3,command=lambda:show_frame(frame5),borderwidth=0, highlightthickness=0)
canvas4.create_window(50, 35, window = returnhomebtn3)
canvas4.create_text(200, 35, text = "Medical Info", font = ("Roboto", 20, "bold"), fill = "#004C7D")
logoutbtn=Button(frame8,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas4.create_window(920, 35, window = logoutbtn)

#Left Panel(Navigation)
canvas4.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame8,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas4.create_window(125, 150, window = clcsearch)
dlpres=Button(frame8,text="Download Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas4.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame8,text="Additional Medical Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas4.create_window(125, 550, window = addmedinfo)

#Main Panel
canvas4.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")




show_frame(frame1)
root.mainloop()