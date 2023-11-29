import tkinter as tk
from tkinter import * 
from tkinter import ttk, messagebox, Toplevel
from PIL import Image, ImageTk
from datetime import datetime
from geopy.geocoders import GoogleV3         #Need to PIP install geopy
from validate_email import validate_email    #Need to PIP install validate_email
import requests
import webbrowser
import tkintermapview as tkmap               #Need to PIP install tkintermapview
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
frame7=tk.Frame(root) #View Prescription
frame8=tk.Frame(root) #Additional Medical Info


def show_frame(frame):
    frame.tkraise()

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8):
    frame.grid(row=0, column=0, sticky='nsew')
    frame.config(bg="#FFFFFF")


db = sqlite3.connect('CAD_Database.db') #Put CAD_Database.db in your VSCode workspace folder
cursor = db.cursor()

#F1 Login
def check_login(uname,pword):
    query = 'SELECT * FROM PatientInfo WHERE username = ? AND password = ?'
    cursor.execute(query, (unamebox.get(), pwordbox.get()))
    row = cursor.fetchone()
    if row is None:
        messagebox.showerror("Error", "Invalid username or password")
    else:
        return True
        
def get_name(uname):
    query = 'SELECT fullname FROM PatientInfo WHERE username = ?'
    cursor.execute(query, (unamebox.get(),))
    row = cursor.fetchone()
    return row[0]

ptname = StringVar()
ptname.set("")
def Login():
    if check_login(unamebox.get(),pwordbox.get()):
        global ptname
        ptname.set(get_name(unamebox.get()))
        show_frame(frame5)    


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
Login_Button=tk.Button(frame1, text="Login",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:Login())
Login_Button.place(x=333,y=490)
Register_Button=tk.Button(frame1, text="Register",bg="#054C76",fg="White",width=10,font='Roboto 16',command=lambda:show_frame(frame2))
Register_Button.place(x=569,y=490)



#Password Reset Popup
def pwordpopup():
    pwordpopup=Toplevel(root)
    pwordpopup.geometry("400x400")
    pwordpopup.title("Password Reset")
    pwordpopup.config(bg="#FFFFFF")

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

        else:
            messagebox.showerror("Error", "No input detected.")


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
img1=Image.open("C:/Users/Joe Shen/Documents/Project Stuff/projectimg/patbtn2.png")         #Change Image Path
phi1=ImageTk.PhotoImage(img1)
img2=Image.open("C:/Users/Joe Shen/Documents/Project Stuff/projectimg/clcadminbtn2.png")    #Change Image Path
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
            {"func": lambda x: x.isalnum(),"error_message": "Username must contain only alphanumeric characters",},
            {"func": lambda x: 4 < len(x) < 12,"error_message": "Username must be between 5 to 12 characters",}
        ],
        patpwordbox: [
            {"func": lambda x: 4 < len(x) < 20,"error_message": "Password must be between 5 to 20 characters",},
        ],
        patemailaddbox: [
            {"func": lambda x: validate_email(x,verify=True),"error_message": "Invalid email address",},
        ],
        patnamebox: [
            {"func": lambda x: all(char.isalpha() or char.isspace() for char in x),"error_message": "Name must contain only alphabets",},
        ],
        paticnobox: [
            {"func": lambda x: x.isdigit(),"error_message": "IC/Mykad number must contain only digits",},
            {"func": lambda x: len(x) == 12,"error_message": "IC/Mykad number must be 12 digits",}
        ],
        patcontactnobox: [
            {"func": lambda x: x.isdigit(),"error_message": "Contact number must contain only digits",},
            {"func": lambda x: len(x) == 10,"error_message": "Contact number must be 10 digits",}
        ],
        patgenderbox: [
            {"func": lambda x: x in ["Male", "Female"],"error_message": "Invalid gender",},
        ],
        patbloodtypebox: [
            {"func": lambda x: x in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],"error_message": "Invalid blood type",},
        ],
        pataddressbox: [
            {"func": lambda x: len(x) > 30,"error_message": "Address cannot be empty",},
        ],
        patallergiesbox: [
            {"func": lambda x: all(char.isalnum() or char.isspace() for char in x) or len(x) == 0,"error_message": "Invalid allergies",
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
        
    username = patunamebox.get()
    email = patemailaddbox.get()
    icno = paticnobox.get()
    contactno = patcontactnobox.get()
    # Check if the username is already taken
    cursor.execute("SELECT * FROM PatientInfo WHERE username=?", (username,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Username is already taken")
        return False
    # Check if the email address is already taken
    cursor.execute("SELECT * FROM PatientInfo WHERE emailadd=?", (email,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Email address is already registered")
        return False
    # Check if the IC/Mykad number is already taken
    cursor.execute("SELECT * FROM PatientInfo WHERE icno=?", (icno,))
    if cursor.fetchone():
        messagebox.showerror("Error", "IC/Mykad number is already registered")
        return False
    # Check if the contact number is already taken
    cursor.execute("SELECT * FROM PatientInfo WHERE contactno=?", (contactno,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Contact number is already registered")
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
        patunamebox.get(),patpwordbox.get(),patemailaddbox.get(),patnamebox.get(),paticnobox.get(),patgenderbox.get(),
        patbloodtypebox.get(),patcontactnobox.get(),pataddressbox.get(),patallergiesbox.get(),current_date_time))

    # Commit the changes and close the connection
    db.commit()
    db.close()

    messagebox.showinfo("Success", "Registration successful!")



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
canvas1.create_text(650, 35, text = "Welcome, ", font = ("Roboto", 14, "bold"), fill = "#004C7D")
dyname=Label(canvas1,textvariable=ptname,font=("Roboto",14, "bold"),bg="#B5DFF0",fg="#004C7D")
canvas1.create_window(770, 35, window = dyname)
logoutbtn=Button(frame5,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas1.create_window(930, 35, window = logoutbtn)


#Left Panel(Navigation)
canvas1.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame5,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas1.create_window(125, 150, window = clcsearch)
dlpres=Button(frame5,text="View Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas1.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame5,text="Health Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas1.create_window(125, 550, window = addmedinfo)


#Main Panel
canvas1.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")
canvas1.create_text(460, 125, text = "Pending/Approved Checkups:", font = ("Roboto", 14, "bold"), fill = "#004C7D")
refreshbtn=Button(frame5,text="Refresh",font=("Roboto",14),bg="#054C76",fg="White",width=6, command=lambda:fetch_checkups())
canvas1.create_window(670, 120, window = refreshbtn)
listcontainer = tk.Frame(canvas1, bg="#FFFFFF", width=666, height=555)
listcontainer.pack(fill=BOTH, expand=True)
canvas1.create_window(650, 420, window=listcontainer)
checkuplist = tk.Canvas(listcontainer, bg="#FFFFFF", highlightthickness=0, width=666, height=555,scrollregion=(0, 0, 0, 1000))
checkuplist.pack(fill=BOTH, expand=True)
homescroll = ttk.Scrollbar(checkuplist, orient=tk.VERTICAL)
homescroll.place(relx=1, rely=0, relheight=1, anchor=NE)
checkuplist.configure(yscrollcommand=homescroll.set)
homescroll.config(command=checkuplist.yview)
checkuplist.bind("<MouseWheel>", lambda e: checkuplist.yview_scroll(int(-1*(e.delta/120)), "units"))

def fetch_checkups():
    patientname = ptname.get()
    db = sqlite3.connect('CAD_Database.db')  # Put CAD_Database.db in your VSCode workspace folder
    cursor.execute("SELECT patID FROM PatientInfo WHERE fullname = ?", (patientname,))
    result = cursor.fetchone()
    if result is not None:
        # Fetch appointments for the patient
        cursor.execute("SELECT * FROM Appointment WHERE patID = ?", (result))
        rows = cursor.fetchall()

        for index, row in enumerate(rows):
            if row[6] == 0:
                status = "Pending"
            elif row[6] == 1:
                status = "Approved"

            # Fetch clinic name based on clinic_id
            cursor.execute("SELECT clinic_name FROM ClinicInformation WHERE clinic_id = ?", (row[4],))
            clinic_name = cursor.fetchone()[0]
            item = {
                "clinic": clinic_name,
                "time": row[2],
                "date": row[3],
                "status": status}
            itemframe = Frame(checkuplist, bg="#FFFFFF", highlightbackground="black", highlightthickness=1, width=630, height=80)
            checkuplist.create_window(330, 50 + index * 90, window=itemframe)

            clinic_label = Label(itemframe, text=f"Clinic: {clinic_name}", font=("Roboto", 14), bg="#FFFFFF")
            clinic_label.place(relx=0.05, rely=0.2, anchor="w")
            time_label = Label(itemframe, text=f"Time: {row[2]}", font=("Roboto", 14), bg="#FFFFFF")
            time_label.place(relx=0.5, rely=0.2, anchor="w")
            date_label = Label(itemframe, text=f"Date: {row[3]}", font=("Roboto", 14), bg="#FFFFFF")
            date_label.place(relx=0.05, rely=0.7, anchor="w")
            status_label = Label(itemframe, text=f"Status: {status}", font=("Roboto", 14), bg="#FFFFFF")
            status_label.place(relx=0.5, rely=0.7, anchor="w")

        checkuplist.update_idletasks()
    db.close()



#F6 Clinic Search
canvas2 = tk.Canvas(frame6, width=1000, height=700, bg="#FFFFFF", highlightthickness=0)
canvas2.pack()
canvas2.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline="#054C76")
logoir2 = logoi.resize((80, 50))
logophir2=ImageTk.PhotoImage(logoir2)
returnhomebtn1=Button(frame6, image = logophir2,command=lambda:show_frame(frame5),borderwidth=0, highlightthickness=0)
canvas2.create_window(50, 35, window = returnhomebtn1)
canvas2.create_text(320, 35, text = "Search for Healthcare Facilities", font = ("Roboto", 20, "bold"), fill = "#004C7D")
canvas2.create_text(650, 35, text = "Welcome, ", font = ("Roboto", 14, "bold"), fill = "#004C7D")
dyname2=Label(canvas2,textvariable=ptname,font=("Roboto",14, "bold"),bg="#B5DFF0",fg="#004C7D")
canvas2.create_window(770, 35, window = dyname2)
logoutbtn=Button(frame6,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas2.create_window(920, 35, window = logoutbtn)


#Left Panel(Navigation)
canvas2.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
dlpres=Button(frame6,text="View Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=1,command=lambda:show_frame(frame7))
canvas2.create_window(125, 130, window = dlpres)
addmedinfo=Button(frame6,text="Health Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=1,command=lambda:show_frame(frame8))
canvas2.create_window(125, 180, window = addmedinfo)
canvas2.create_text(70, 230, text = "Clinic List:", font = ("Roboto", 16, "bold"), fill = "#004C7D")

#Clinic List
def fetch_clinics():
    query = 'SELECT * FROM ClinicInformation WHERE status = 1'
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        clclist.insert(END, row[1])

def goto_clinic(event):
    selected_clinic = clclist.get(clclist.curselection())
    query = 'SELECT * FROM ClinicInformation WHERE clinic_name = ?'
    cursor.execute(query, (selected_clinic,))
    clinic_info = cursor.fetchone()
    address = clinic_info[4]
    key_file = open("gmapikey.txt", "r")
    API_KEY = key_file.readline()
    
    prmeter = {
        'key': API_KEY,
        'address': address
    }
    baseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
    response = requests.get(baseurl, params=prmeter).json()
    response.keys()
    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
    else:
        print("Error")
    marker = map_widget.set_position(lat, lon, marker=True)
    marker.set_text(clinic_info[1])
    map_slider.config(value=15)


def view_clinic_info(event):
    selected_clinic = clclist.get(clclist.curselection())
    query = 'SELECT * FROM ClinicInformation WHERE clinic_name = ?'
    cursor.execute(query, (selected_clinic,))
    clinic_info = cursor.fetchone()

    clcinfo = Toplevel(frame6)
    clcinfo.geometry("700x700")
    clcinfo.title("Clinic Information")
    clcinfo.config(bg="#FFFFFF")

    infocv = tk.Canvas(clcinfo, bg="#B5DFF0", highlightthickness=0, scrollregion=(0, 0, 0, 1500))
    infocv.pack(fill=BOTH, expand=True)
    infoscroll = ttk.Scrollbar(clcinfo, orient=tk.VERTICAL, command=infocv.yview)
    infocv.configure(yscrollcommand=infoscroll.set)
    infoscroll.place(relx=1, rely=0, relheight=1, anchor=NE)
    infocv.bind("<MouseWheel>", lambda e: infocv.yview_scroll(int(-1*(e.delta/120)), "units"))
    infocv.create_text(100, 50, text = "Clinic Info:", font = ("Roboto", 20, "bold"), fill = "#004C7D")
    clcinfoframe = Frame(infocv, bg="#FFFFFF", width=600, height=600)
    clcinfoframe.bind("<MouseWheel>", lambda e: infocv.yview_scroll(int(-1*(e.delta/120)), "units"))
    infocv.create_window(333, 370, window = clcinfoframe)
    clcnamelbl = Label(clcinfoframe, text = "Clinic Name:", font = ("Roboto", 16), bg = "#FFFFFF")
    clcnamelbl.place(x=10, y=10)
    clcnametxt = Label(clcinfoframe, text = clinic_info[1], font = ("Roboto", 16), bg = "#FFFFFF")
    clcnametxt.place(x=160, y=10)
    clcwkhrlbl = Label(clcinfoframe, text = "Working Hours:", font = ("Roboto", 16), bg = "#FFFFFF")
    clcwkhrlbl.place(x=10, y=80)
    clcwkhrtxt = Label(clcinfoframe, text = clinic_info[2], font = ("Roboto", 16), bg = "#FFFFFF")
    clcwkhrtxt.place(x=160, y=80)
    clccoorlbl = Label(clcinfoframe, text = "Coordinates:", font = ("Roboto", 16), bg = "#FFFFFF")
    clccoorlbl.place(x=10, y=150)
    clccoortxt = Label(clcinfoframe, text = clinic_info[3] , font = ("Roboto", 16), bg = "#FFFFFF")
    clccoortxt.place(x=160, y=150)
    clcaddrlbl = Label(clcinfoframe, text = "Address:", font = ("Roboto", 16), bg = "#FFFFFF")
    clcaddrlbl.place(x=10, y=220)
    clcaddrtxt = Label(clcinfoframe, text = clinic_info[4], font = ("Roboto", 16), bg = "#FFFFFF", wraplength=400, justify=LEFT)
    clcaddrtxt.place(x=160, y=220)
    clccontlbl = Label(clcinfoframe, text = "Contact No.:", font = ("Roboto", 16), bg = "#FFFFFF")
    clccontlbl.place(x=10, y=290)
    clcconttxt = Label(clcinfoframe, text = clinic_info[5], font = ("Roboto", 16), bg = "#FFFFFF")
    clcconttxt.place(x=160, y=290)
    clcdescrlbl = Label(clcinfoframe, text = "Description:", font = ("Roboto", 16), bg = "#FFFFFF")
    clcdescrlbl.place(x=10, y=360)
    clcdescrtxt = Label(clcinfoframe, text = clinic_info[7], font = ("Roboto", 16), bg = "#FFFFFF", wraplength=400, justify=LEFT)
    clcdescrtxt.place(x=160, y=360)
    
    def request_checkup():
        if not reqchkdatebox.get() or not reqchktimebox.get() or not reqchksickbox.get():
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        db = sqlite3.connect('CAD_Database.db') #Put CAD_Database.db in your VSCode workspace folder
        cursor = db.cursor()

        selected_clinic = clclist.get(clclist.curselection())
        cursor.execute("SELECT clinic_id FROM ClinicInformation WHERE clinic_name = ?", (selected_clinic,))
        clinic_id = cursor.fetchone()[0]  # Fetch the clinic_id

        patient_name = ptname.get()

        cursor.execute("SELECT patID FROM PatientInfo WHERE fullname = ?", (patient_name,))
        result = cursor.fetchone()

        if result is not None:
            patID = result[0]
            cursor.execute("INSERT INTO Appointment (clinic_id, patID, appointment_date, appointment_time, symptoms, appstatus) VALUES (?, ?, ?, ?, ?, ?)",
                                (clinic_id, patID, reqchkdatebox.get(), reqchktimebox.get(), reqchksickbox.get(), 0))
            db.commit()
            messagebox.showinfo("Success", "Checkup booked!")



    infocv.create_text(200, 780, text = "Request for Checkup:", font = ("Roboto", 20, "bold"), fill = "#004C7D")
    reqchkframe = Frame(infocv, bg="#FFFFFF", width=600, height=600)
    reqchkframe.bind("<MouseWheel>", lambda e: infocv.yview_scroll(int(-1*(e.delta/120)), "units"))
    infocv.create_window(333, 1100, window = reqchkframe)
    reqchkdate = Label(reqchkframe, text = "Date:", font = ("Roboto", 16), bg = "#FFFFFF")
    reqchkdate.place(x=50, y=30)
    reqchkdatebox = Entry(reqchkframe, width=30, font = ("Roboto", 16), bd=2, bg="#B5DDF0")
    reqchkdatebox.place(x=120, y=30)
    reqchktime = Label(reqchkframe, text = "Time:", font = ("Roboto", 16), bg = "#FFFFFF")
    reqchktime.place(x=50, y=100)
    reqchktimebox = Entry(reqchkframe, width=30, font = ("Roboto", 16), bd=2, bg="#B5DDF0")
    reqchktimebox.place(x=120, y=100)
    reqchksick = Label(reqchkframe, text = "Describe Your Condition:", font = ("Roboto", 16), bg = "#FFFFFF")
    reqchksick.place(x=50, y=170)
    reqchksickbox = Entry(reqchkframe, width=40, font = ("Roboto", 16), bd=2, bg="#B5DDF0")
    reqchksickbox.place(x=50, y=200)
    reqchkbtn = Button(reqchkframe, text = "Request Appointment", font = ("Roboto", 16), bg = "#054C76", fg = "White", width = 18, command=lambda: request_checkup())
    reqchkbtn.place(x=180, y=350)
    
clclist=Listbox(frame6,name="cliniclist", width=20,height=16,font=("Roboto",16))
canvas2.create_window(125, 450, window = clclist)
fetch_clinics()

def clinichandler(event):
    view_clinic_info(event)
    goto_clinic(event)

clclist.bind("<Double-Button-1>", clinichandler)


#Main Panel
canvas2.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")
canvas2.create_text(380, 120, text = "Search Here:", font = ("Roboto", 14, "bold"), fill = "#004C7D")
sbox=Entry(frame6, name="searchbox", width=45,font=("Roboto",14))
canvas2.create_window(700, 120, window = sbox)
sbox.insert(0, "Search clinic by address or coordinates")
keyin=StringVar()
style = ttk.Style()
style.configure("Custom.TRadiobutton", background="#B5DFF0")
rbutton1 = ttk.Radiobutton(canvas2, text='Address', style="Custom.TRadiobutton", variable=keyin, value='address')
canvas2.create_window(500, 150, window=rbutton1)
rbutton2=ttk.Radiobutton(canvas2,text='Coordinate', style="Custom.TRadiobutton", variable=keyin, value='coordinate')
canvas2.create_window(600, 150, window = rbutton2)
rbutton3=ttk.Radiobutton(canvas2,text='Google', style="Custom.TRadiobutton", variable=keyin, value='google')
canvas2.create_window(700, 150, window = rbutton3)
rbutton4=ttk.Radiobutton(canvas2, text='Edge', style="Custom.TRadiobutton", variable=keyin, value='edge')
canvas2.create_window(800, 150, window = rbutton4)
keyin.set('address')
si=Image.open("C:/Users/Joe Shen/Documents/Project Stuff/projectimg/search.png")
sphi=ImageTk.PhotoImage(si)
sbtn=Button(canvas2,image=sphi,width=30,height=30,bg="#B5DFF0",bd=0,command=lambda:search())
canvas2.create_window(973, 120, window = sbtn)

def goto_place():
    key_file = open("gmapikey.txt", "r")
    API_KEY = key_file.readline()
    address = sbox.get()
    prmeter = {
        'key': API_KEY,
        'address': address
    }
    baseurl = "https://maps.googleapis.com/maps/api/geocode/json?"
    response = requests.get(baseurl, params=prmeter).json()
    response.keys()
    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
    else:
        print("Error")
    marker = map_widget.set_position(lat, lon, marker=True)
    marker.set_text(sbox.get())

def search():
        address = None
        if sbox.get()!='':
            if keyin.get()=='google':
                webbrowser.open(f'https://www.google.com/search?q={sbox.get()}')
            elif keyin.get()=='edge':
                webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open(f'https://www.google.com/search?q={sbox.get()}')
            elif keyin.get()=='address':
                goto_place()
            elif keyin.get()=='coordinate':
                 map_widget.set_position(sbox.get(), marker=True)
                 map_slider.config(value=15)
        else:
            messagebox.showinfo("No Input","No Input Detected.")
sbox.bind("<Return>", lambda e: search())

def remove_hint_text(event):
    if sbox.get() == "Search clinic by address or coordinates":
        sbox.delete(0, END)
sbox.bind("<FocusIn>", remove_hint_text)

map_widget=tkmap.TkinterMapView(canvas2, width=600, height=460, corner_radius=0)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
canvas2.create_window(630, 440, window = map_widget)

#Slide Function
def slide(e):
    map_widget.set_zoom(map_slider.get())

map_slider = ttk.Scale(canvas2, from_=5, to=25, orient=tk.HORIZONTAL, command=slide,length=200)
map_slider.set(18)
canvas2.create_window(430, 185, window = map_slider)

#Default Map Location (INTI)
marker1=map_widget.set_position(5.3416,100.2819, marker=True)

def left_click_event(coordinates_tuple):
    print("Left click event with coordinates:", coordinates_tuple)
    
map_widget.add_left_click_map_command(left_click_event)



#F7 View Prescription
canvas3 = tk.Canvas(frame7, width = 1000, height = 700, bg = "#FFFFFF", highlightthickness=0)
canvas3.pack()
canvas3.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline = "#054C76")
logoir3=logoi.resize((80,50))
logophir3=ImageTk.PhotoImage(logoir3)
returnhomebtn2=Button(frame7, image = logophir3,command=lambda:show_frame(frame5),borderwidth=0, highlightthickness=0)
canvas3.create_window(50, 35, window = returnhomebtn2)
canvas3.create_text(320, 35, text = "View Your Prescriptions", font = ("Roboto", 20, "bold"), fill = "#004C7D")
canvas3.create_text(650, 35, text = "Welcome, ", font = ("Roboto", 14, "bold"), fill = "#004C7D")
dyname3=Label(canvas3,textvariable=ptname,font=("Roboto",14, "bold"),bg="#B5DFF0",fg="#004C7D")
canvas3.create_window(770, 35, window = dyname3)
logoutbtn=Button(frame7,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas3.create_window(920, 35, window = logoutbtn)


#Left Panel(Navigation)
canvas3.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame7,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas3.create_window(125, 150, window = clcsearch)
dlpres=Button(frame7,text="View Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas3.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame7,text="Health Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas3.create_window(125, 550, window = addmedinfo)


#Main Panel
canvas3.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")
canvas3.create_text(410, 125, text = "Your Prescriptions:", font = ("Roboto", 14, "bold"), fill = "#004C7D")
refreshbtn2=Button(frame7,text="Refresh",font=("Roboto",14),bg="#054C76",fg="White",width=6, command=lambda:fetch_prescription())
canvas3.create_window(670, 120, window = refreshbtn2)
listcontainer2 = tk.Frame(canvas3, bg="#FFFFFF", width=666, height=555)
listcontainer2.pack(fill=BOTH, expand=True)
canvas3.create_window(650, 420, window=listcontainer2)
presclist = tk.Canvas(listcontainer2, bg="#FFFFFF", highlightthickness=0, width=666, height=555,scrollregion=(0, 0, 0, 1000))
presclist.pack(fill=BOTH, expand=True)
prescscroll = ttk.Scrollbar(presclist, orient=tk.VERTICAL)
prescscroll.place(relx=1, rely=0, relheight=1, anchor=NE)
presclist.configure(yscrollcommand=prescscroll.set)
prescscroll.config(command=presclist.yview)
presclist.bind("<MouseWheel>", lambda e: presclist.yview_scroll(int(-1*(e.delta/120)), "units"))
def fetch_prescription():
    patientname = ptname.get()
    db = sqlite3.connect('CAD_Database.db')  # Put CAD_Database.db in your VSCode workspace folder
    cursor.execute("SELECT patID FROM PatientInfo WHERE fullname = ?", (patientname,))
    result = cursor.fetchone()

    if result is not None:
        # Fetch appointments for the patient
        cursor.execute("SELECT * FROM PRESCRIPTIONS WHERE patID = ?", (result))
        rows = cursor.fetchall()

        for index, row in enumerate(rows):
           
            # Fetch clinic name based on clinic_id
            cursor.execute("SELECT clinic_name FROM ClinicInformation WHERE clinic_id = ?", (row[4],))
            clinic_name = cursor.fetchone()[0]

            item = {
                "clinic": clinic_name,
                "title": row[1],
                "content": row[2],
            }

            itemframe2 = Frame(presclist, bg="#FFFFFF", highlightbackground="black", highlightthickness=1, width=630, height=80)
            presclist.create_window(330, 50 + index * 90, window=itemframe2)

            clinic_label = Label(itemframe2, text=f"Clinic: {clinic_name}", font=("Roboto", 14), bg="#FFFFFF")
            clinic_label.place(relx=0.05, rely=0.2, anchor="w")

            title_label = Label(itemframe2, text=f"Title: {row[1]}", font=("Roboto", 14), bg="#FFFFFF")
            title_label.place(relx=0.5, rely=0.2, anchor="w")

            content_label = Label(itemframe2, text=f"Content: {row[2]}", font=("Roboto", 14), bg="#FFFFFF")
            content_label.place(relx=0.05, rely=0.7, anchor="w")

        # Adjust the scroll region of the canvas
        presclist.update_idletasks()
    db.close()


#F8 Health Info
canvas4 = tk.Canvas(frame8, width = 1000, height = 700, bg = "#FFFFFF", highlightthickness=0)
canvas4.pack()
canvas4.create_rectangle(0, 0, 1000, 70, fill="#B5DFF0", outline = "#054C76")
logoir4=logoi.resize((80,50))
logophir4=ImageTk.PhotoImage(logoir4)
returnhomebtn3=Button(frame8, image = logophir3,command=lambda:show_frame(frame5),borderwidth=0, highlightthickness=0)
canvas4.create_window(50, 35, window = returnhomebtn3)
canvas4.create_text(200, 35, text = "Health Info", font = ("Roboto", 20, "bold"), fill = "#004C7D")
canvas4.create_text(650, 35, text = "Welcome, ", font = ("Roboto", 14, "bold"), fill = "#004C7D")
dyname4=Label(canvas4,textvariable=ptname,font=("Roboto",14, "bold"),bg="#B5DFF0",fg="#004C7D")
canvas4.create_window(770, 35, window = dyname4)
logoutbtn=Button(frame8,text="Logout",font=("Roboto",20),bg="#054C76",fg="White",width=7,command=lambda:show_frame(frame1))
canvas4.create_window(920, 35, window = logoutbtn)


#Left Panel(Navigation)
canvas4.create_rectangle(0, 100, 250, 700, fill="#B5DFF0", outline = "#054C76")
clcsearch=Button(frame8,text="Clinic Search",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame6))
canvas4.create_window(125, 150, window = clcsearch)
dlpres=Button(frame8,text="View Prescription",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame7))
canvas4.create_window(125, 350, window = dlpres)
addmedinfo=Button(frame8,text="Health Info",font=("Roboto",16),bg="#054C76",fg="White",width=18,height=2,command=lambda:show_frame(frame8))
canvas4.create_window(125, 550, window = addmedinfo)


#Main Panel
canvas4.create_rectangle(300, 100, 1000, 700, fill="#B5DFF0", outline = "#054C76")
canvas4.create_text(410, 125, text = "Medical/Health Info:", font = ("Roboto", 14, "bold"), fill = "#004C7D")
listcontainer3 = tk.Frame(canvas4, bg="#FFFFFF", width=666, height=555)
listcontainer3.pack(fill=BOTH, expand=True)
canvas4.create_window(650, 420, window=listcontainer3)
hinfolist = tk.Canvas(listcontainer3, bg="#FFFFFF", highlightthickness=0, width=666, height=555,scrollregion=(0, 0, 0, 2000))
hinfolist.pack(fill=BOTH, expand=True)
hinfoscroll = ttk.Scrollbar(hinfolist, orient=tk.VERTICAL)
hinfoscroll.place(relx=1, rely=0, relheight=1, anchor=NE)
hinfolist.configure(yscrollcommand=hinfoscroll.set)
hinfoscroll.config(command=hinfolist.yview)
hinfolist.bind("<MouseWheel>", lambda e: hinfolist.yview_scroll(int(-1*(e.delta/120)), "units"))
def fetch_hinfo():
    db = sqlite3.connect('CAD_Database.db')  # Put CAD_Database.db in your VSCode workspace folder
    cursor.execute("SELECT * FROM TIPS")
    rows = cursor.fetchall()

    for index, row in enumerate(rows):
        item = {
            "title": row[1],
            "content": row[2],
            "link": row[3],
        }

        itemframe3 = Frame(hinfolist, bg="#FFFFFF", highlightbackground="black", highlightthickness=1, width=630, height=145)
        itemframe3.bind("<MouseWheel>", lambda e: hinfolist.yview_scroll(int(-1*(e.delta/120)), "units"))
        hinfolist.create_window(330, 63 + index * 150, window=itemframe3)

        title_label = Label(itemframe3, text=f"Title: {row[1]}", font=("Roboto", 12), bg="#FFFFFF")
        title_label.place(relx=0, rely=0.15, anchor="w")

        content_label = Label(itemframe3, text=f"Content: {row[2]}", font=("Roboto", 12), bg="#FFFFFF")
        content_label.place(relx=0, rely=0.5, anchor="w")

        link_label = Label(itemframe3, text=f"Link: {row[3]}", font=("Roboto", 12), bg="#FFFFFF")
        link_label.place(relx=0, rely=0.8, anchor="w")

        # Adjust the scroll region of the canvas
        hinfolist.update_idletasks()
    db.close()

fetch_hinfo()


show_frame(frame1)
root.mainloop()