import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import Image, ImageTk
import sqlite3

root=Tk()
root.geometry("1440x900")
root.title("Testing")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.resizable(False, False)

frame1=tk.Frame(root) #Login
frame2=tk.Frame(root) #User Type Selection
frame3=tk.Frame(root) #Patient Register
frame4=tk.Frame(root) #Clinic Register
frame5=tk.Frame(root) #Homepage (Patient)
frame6=tk.Frame(root) #Homepage (Clinic)

def show_frame(frame):
    frame.tkraise()

for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0, column=0, sticky='nsew')
    frame.config(bg="#FFFFFF")


db_path = 'C:/DOC/Documents/ZzJS/Projects/VSCode/backup_cad.db'
db = sqlite3.connect(db_path)
cursor = db.cursor()

#F1 Login
logoi=Image.open("C:\DOC\Documents\ZzJS\Snips\CDA-Icon.png")
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
pwordbox=Entry(frame1,width=30,show="*",font=("Roboto",16),bd=2,bg="#B5DDF0")
pwordbox.place(x=550,y=450)
Login_Button=tk.Button(frame1, text="Login",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame5))
Login_Button.place(x=550,y=520)
Register_Button=tk.Button(frame1, text="Register",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame2))
Register_Button.place(x=780,y=520)



#F2 User Type Selection
userrole = None
def assignrole(widget):
    global userrole
    userrole = widget.winfo_name()
    if userrole == "patient":
        show_frame(frame3)
    elif userrole == "cadmin":
        show_frame(frame4)

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
patbtn=tk.Button(frame2,image=phi1,name="patient", borderwidth=0, highlightthickness=0,command=lambda:assignrole(patbtn))
patbtn.place(x=310,y=350)
clcadminbtn=tk.Button(frame2, image=phi2,name="cadmin", borderwidth=0, highlightthickness=0, command=lambda:assignrole(clcadminbtn))
clcadminbtn.place(x=830,y=350)



#F3 Patient Register
#Registration Function
def generate_user_id(userrole):
    if userrole == "Patient":
        prefix = "P"
    elif userrole == "ClinicAdmin":
        prefix = "C"
    else:
        return None 

    # Query the database to find the maximum user ID for the given role
    cursor.execute(f"SELECT MAX(user_id) FROM USER WHERE user_id LIKE '{prefix}___'")
    max_user_id = cursor.fetchone()[0]
    if max_user_id is None:
        new_user_id = f"{prefix}001"
    else:
        new_num = int(max_user_id[1:]) + 1
        new_user_id = f"{prefix}{new_num:03d}"

    return new_user_id

def check_fields(frame):
    empty_fields = []

    for widget in frame.winfo_children():
        if isinstance(widget, (tk.Entry, ttk.Combobox)):
            if widget.winfo_name() != "allergies" and not widget.get():
                empty_fields.append(widget)

    if empty_fields:
        messagebox.showerror("Error", f"Please fill in the following fields: {', '.join([widget.winfo_name() for widget in empty_fields])}")
        return False

    return True


def register_newuser1(user_id, username, password, userrole, addinfo):
    try:
        if check_fields(frame3):  # Check if fields are filled, using the check_fields function
            # Insert user_id, username, and password into the USER table
            cursor.execute("INSERT INTO USER (user_id, username, password) VALUES (?, ?, ?)", (user_id, username, password))
            userrole == "Patient"
            cursor.execute("INSERT INTO PatientInfo (name, icno, gender, bloodtype, allergy, address) VALUES (?, ?, ?, ?, ?, ?)", (addinfo['name'], addinfo['icno'], addinfo['gender'], addinfo['bloodtype'], addinfo['allergy'], addinfo['address']))
            db.commit()
            messagebox.showinfo("NICE", "Registration success!")

    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Insertion Fail: {str(e)}")


def register_newuser2(user_id, username, password, userrole, addinfo):
    try:
        if check_fields(frame4):
            cursor.execute("INSERT INTO USER (user_id, username, password) VALUES (?, ?, ?)", (user_id, username, password))
            userrole == "ClinicAdmin"
            cursor.execute("INSERT INTO ClinicInfo (user_id, name) VALUES (?, ?)", (user_id, addinfo['name']))
            db.commit()
            messagebox.showinfo("NICE", "Registration success!")

    except Exception as e:
        db.rollback()
        messagebox.showerror("Error", f"Insertion Fail: {str(e)}")


def patregister():
    userrole = "Patient"
    user_id = generate_user_id(userrole)
    username = patunamebox.get()
    password = patpwordbox.get()
    
    addinfo = {
        'name': patnamebox.get(),'icno': paticnobox.get(),'gender': patgenderbox.get(),
        'bloodtype': patbloodtypebox.get(),'allergy': patallergiesbox.get(),'address': pataddressbox.get()}

    register_newuser1(user_id, username, password, userrole, addinfo)

Logo3=Label(frame3,image=logophi,bg="#FFFFFF")
Logo3.place(x=605,y=20)
Slogan3=Label(frame3,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan3.place(x=450,y=185)
patregisterlbl=Label(frame3,text="Patient Registration",font=("Roboto",30,"bold","underline"),bg="#FFFFFF")
patregisterlbl.place(x=520,y=240)
newpatient_uname=Label(frame3,text="Create New Username:",font=("Roboto",16),bg="#FFFFFF")
newpatient_uname.place(x=250,y=350)
patunamebox=Entry(frame3,name="username",width=30,font=("Roboto",16), bd=2, bg="#B5DDF0")
patunamebox.place(x=250,y=380)
newpatient_pword=Label(frame3,text="Create New Password:",font=("Roboto",16),bg="#FFFFFF")
newpatient_pword.place(x=250,y=450)
patpwordbox=Entry(frame3,name="password",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patpwordbox.place(x=250,y=480)
patname=Label(frame3,text="Full Name (as per IC/Passport):",font=("Roboto",16),bg="#FFFFFF")
patname.place(x=250,y=550)
patnamebox=Entry(frame3,name="fullname",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patnamebox.place(x=250,y=580)
paticno=Label(frame3,text="IC/Mykad No.:",font=("Roboto",16),bg="#FFFFFF")
paticno.place(x=250,y=650)
paticnobox=Entry(frame3,name="idcardnum",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
paticnobox.place(x=250,y=680)
patgender=Label(frame3,text="Gender:",font=("Roboto",16),bg="#FFFFFF")
patgender.place(x=830,y=350)
patgenderbox=ttk.Combobox(frame3,name="gender",font=("Roboto",16),values=["Male","Female","Rather Not Say"],width=20)
patgenderbox.place(x=830,y=380)
patbloodtype=Label(frame3,text="Blood Type:",font=("Roboto",16),bg="#FFFFFF")
patbloodtype.place(x=830,y=450)
patbloodtypebox=ttk.Combobox(frame3,name="bloodtype",font=("Roboto",16),values=["A","B","AB","O"],width=20)
patbloodtypebox.place(x=830,y=480)
patallergies=Label(frame3,text="Allergies:",font=("Roboto",16),bg="#FFFFFF")
patallergies.place(x=830,y=550)
patallergiesbox=Entry(frame3,name="allergies",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
patallergiesbox.place(x=830,y=580)
pataddress=Label(frame3,text="Address:",font=("Roboto",16),bg="#FFFFFF")
pataddress.place(x=830,y=650)
pataddressbox=Entry(frame3,name="address",width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
pataddressbox.place(x=830,y=680)
patregisterbtn=tk.Button(frame3,text="Register",font=("Roboto",25,"bold"),bg="#054C76",fg="White",width=10,command=lambda:patregister())
patregisterbtn.place(x=610,y=750)

#F4 Clinic Register
def clcregister():
    userrole = "ClinicAdmin"
    user_id = generate_user_id(userrole)
    username = clcunamebox.get()
    password = clcpwordbox.get()
    addinfo = {'name': clcnamebox.get()}

    register_newuser2(user_id, username, password, userrole, addinfo)

Logo3=Label(frame4,image=logophi,bg="#FFFFFF")
Logo3.place(x=605,y=20)
Slogan3=Label(frame4,text="Healthcare at Your Doorstep, Just a Click Away",font=("Roboto",17,"bold"),bg="#FFFFFF",fg="#004C7D")
Slogan3.place(x=450,y=185)
clcregisterlbl=Label(frame4,text="Clinic Registration",font=("Roboto",30,"bold","underline"),bg="#FFFFFF")
clcregisterlbl.place(x=520,y=240)
newclc_uname=Label(frame4,text="Create New Username:",font=("Roboto",16),bg="#FFFFFF")
newclc_uname.place(x=250,y=350)
clcunamebox=Entry(frame4,width=30,font=("Roboto",16), bd=2, bg="#B5DDF0")
clcunamebox.place(x=250,y=380)
newpatient_pword=Label(frame4,text="Create New Password:",font=("Roboto",16),bg="#FFFFFF")
newpatient_pword.place(x=250,y=450)
clcpwordbox=Entry(frame4,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
clcpwordbox.place(x=250,y=480)
clcname=Label(frame4,text="Clinic Name:",font=("Roboto",16),bg="#FFFFFF")
clcname.place(x=250,y=550)
clcnamebox=Entry(frame4,width=30,font=("Roboto",16),bd=2,bg="#B5DDF0")
clcnamebox.place(x=250,y=580)
clcregisterbtn=tk.Button(frame4,text="Register",font=("Roboto",25,"bold"),bg="#054C76",fg="White",width=10,command=lambda:clcregister())
clcregisterbtn.place(x=610,y=750)


#F5 Homepage(Patient)
canvas1 = tk.Canvas(frame5, width = 1440, height = 900, bg = "#FFFFFF", highlightthickness=0)
canvas1.pack()
canvas1.create_rectangle(0, 0, 1440, 100, fill="#B5DFF0", outline = "#054C76")
logoir1=logoi.resize((100,70))
logophir1=ImageTk.PhotoImage(logoir1)
canvas1.create_image(80, 50, image = logophir1)
canvas1.create_text(480, 50, text = "Call A Doctor Home Page (Patient)", font = ("Roboto", 30, "bold"), fill = "#004C7D")
logoutbtn=Button(frame5,text="Logout",font=("Roboto",24),bg="#054C76",fg="White",width=8,command=lambda:show_frame(frame1))
logoutbtn.place(x=1250,y=20)

#Left Panel(Navigation)
canvas1.create_rectangle(0, 150, 420, 900, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame5,text="Clinic Search",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame5))
clcsearch.place(x=50,y=200)
dlpres=Button(frame5,text="Download Prescription",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2,command=lambda:show_frame(frame6))
dlpres.place(x=50,y=400)
addmedinfo=Button(frame5,text="Additional Medical Info",font=("Roboto",20),bg="#054C76",fg="White",width=20,height=2)
addmedinfo.place(x=50,y=600)

#Main Panel
canvas1.create_rectangle(520, 150, 1440, 900, fill="#B5DFF0", outline = "#054C76")


#F6 Homepage(Clinic)
canvas2 = tk.Canvas(frame6, width = 1440, height = 900, bg = "#FFFFFF", highlightthickness=0)
canvas2.pack()
canvas2.create_rectangle(0, 0, 1440, 100, fill="#B5DFF0", outline = "#054C76")
logoir2=logoi.resize((100,70))
logophir2=ImageTk.PhotoImage(logoir1)
canvas2.create_image(80, 50, image = logophir1)
canvas2.create_text(480, 50, text = "Call A Doctor Clinic Admin (Clinic)", font = ("Roboto", 30, "bold"), fill = "#004C7D")
logoutbtn=Button(frame5,text="Logout",font=("Roboto",24),bg="#054C76",fg="White",width=8,command=lambda:show_frame(frame1))
logoutbtn.place(x=1250,y=20)

#Left Panel(Navigation)
canvas2.create_rectangle(0, 150, 420, 900, fill="#B5DFF0", outline = "#054C76")

#Main Panel
canvas2.create_rectangle(520, 150, 1440, 900, fill="#B5DFF0", outline = "#054C76")



show_frame(frame1)
root.mainloop()