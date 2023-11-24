import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import StringVar, messagebox
from tkinter import messagebox
import sqlite3

LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.clinic_id = None

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginClinic, RegisterClinic, RegisterFounder, ClinicAccount, ClinicPending
                  , ClinicHomepage, DoctorList, UploadDoctor, ManageDoctor,ClinicDecline,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginClinic)

    def show_frame(self, frame_class):
        print(self.clinic_id)
        frame = self.frames[frame_class]
        frame.clinic_id = self.clinic_id 
        frame.tkraise()
        if isinstance(frame, ManageDoctor):
            frame.showdoctordetails()
        if isinstance(frame, ClinicPending):
            frame.display_status()
        if isinstance(frame, ClinicDecline):
            frame.display_status()


class LoginClinic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        clinic_username = StringVar()

        self.login_clinic = tk.Frame(self, background="white")
        self.login_clinic.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = tk.Label(self.login_clinic, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = tk.Label(self.login_clinic, text="Clinic Login", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=416, y=160)

        self.clnloginusername_label = tk.Label(self.login_clinic, text="Username", font=(25), background="white")
        self.clnloginusername_label.place(x=330, y=250)
        self.clnloginusername_entry = tk.Entry(self.login_clinic, textvariable=clinic_username)
        self.clnloginusername_entry.place(height=30, width=350, x=330, y=275)

        self.clnloginpassword_label = tk.Label(self.login_clinic, text="Password", font=(25), background="white")
        self.clnloginpassword_label.place(x=330, y=350)
        self.clnloginpassword_entry = tk.Entry(self.login_clinic)
        self.clnloginpassword_entry.place(height=30, width=350, x=330, y=375)

        login_btn = tk.Button(self.login_clinic, text="Login", background="thistle", command=self.login)
        login_btn.place(height=30, width=100, x=447, y=470)

        goRegister_btn = tk.Button(self.login_clinic, text="Don't have an account ?", font=('Helvetica', 13), borderwidth=0, background="white", command=lambda: controller.show_frame(RegisterClinic))
        goRegister_btn.place(height=30, width=250, x=380, y=610)

    def login(self):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if self.clnloginusername_entry.get() == "" or self.clnloginpassword_entry.get() == "":
            messagebox.showerror("Error", "Please fill in all the fields")
        else:
            cursor.execute("SELECT * FROM ClinicInformation WHERE clinic_username = ? AND clinic_password = ?", (self.clnloginusername_entry.get(), self.clnloginpassword_entry.get()))
            rows = cursor.fetchall()
            if rows:
                status = rows[0][13] 
                if status == 1:
                    self.controller.clinic_id = rows[0][0]
                    messagebox.showinfo("Success", "Login Successful")
                    self.controller.show_frame(ClinicHomepage)
                elif status == 2:
                    self.controller.clinic_id = rows[0][0]
                    messagebox.showerror("Info", "Login Declined")
                    self.controller.show_frame(ClinicDecline)
                elif status == 0:
                    self.controller.clinic_id = rows[0][0]
                    messagebox.showinfo("Info", "Login Pending")
                    self.controller.show_frame(ClinicPending)
                else:
                    messagebox.showerror("Error", "Invalid Username or Password")
            else:
                messagebox.showerror("Error", "Invalid Username or Password")

        conn.commit()
        conn.close()

class RegisterClinic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.register_clinic = Frame(self, background="white")
        self.register_clinic.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.register_clinic, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = Label(self.register_clinic, text="Clinic Information", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=374, y=160)

        self.clinicname_label = Label(self.register_clinic, text="Clinic name", font=(25), background="white")
        self.clinicname_label.place(x=100, y=230)
        self.clinicname_label_entry = Entry(self.register_clinic)
        self.clinicname_label_entry.place(height=30, width=820, x=100, y=255)

        self.clinictime_label = Label(self.register_clinic, text="Clinic operation time", font=(25), background="white")
        self.clinictime_label.place(x=100, y=310)
        self.clinictime_label_entry = Entry(self.register_clinic)
        self.clinictime_label_entry.place(height=30, width=350, x=100, y=335)

        self.cliniccoordinates_label = Label(self.register_clinic, text="Clinic location coordinates", font=(25), background="white")
        self.cliniccoordinates_label.place(x=100, y=390)
        self.cliniccoordinates_label_entry = Entry(self.register_clinic)
        self.cliniccoordinates_label_entry.place(height=30, width=350, x=100, y=415)

        self.clinicaddress_label = Label(self.register_clinic, text="Clinic address", font=(25), background="white")
        self.clinicaddress_label.place(x=100, y=470)
        self.clinicaddress_label_entry = Entry(self.register_clinic)
        self.clinicaddress_label_entry.place(height=80, width=350, x=100, y=495)

        self.cliniccontact_label = Label(self.register_clinic, text="Clinic contact number", font=(25), background="white")
        self.cliniccontact_label.place(x=570, y=310)
        self.cliniccontact_label_entry = Entry(self.register_clinic)
        self.cliniccontact_label_entry.place(height=30, width=350, x=570, y=335)

        self.clinicregno_label = Label(self.register_clinic, text="Clinic registration nummber", font=(25), background="white")
        self.clinicregno_label.place(x=570, y=390)
        self.clinicregno_label_entry = Entry(self.register_clinic)
        self.clinicregno_label_entry.place(height=30, width=350, x=570, y=415)

        self.clinicdesc_label = Label(self.register_clinic, text="Clinic description", font=(25), background="white")
        self.clinicdesc_label.place(x=570, y=470)
        self.clinicdesc_label_entry = Entry(self.register_clinic)
        self.clinicdesc_label_entry.place(height=80, width=350, x=570, y=495)

        nxtTOfounder_btn = Button(self.register_clinic, text = "Next", background="thistle",command=lambda: controller.show_frame(RegisterFounder))
        nxtTOfounder_btn.place(height=30, width=100,x=450, y=590)

    def get_clinic_information(self):
        clinic_name = self.clinicname_label_entry.get()
        clinic_time = self.clinictime_label_entry.get()
        clinic_coordinates = self.cliniccoordinates_label_entry.get()
        clinic_address = self.clinicaddress_label_entry.get()
        clinic_contact= self.cliniccontact_label_entry.get()
        clinic_registration_no = self.clinicregno_label_entry.get()
        clinic_description = self.clinicdesc_label_entry.get()
        return clinic_name, clinic_time, clinic_coordinates, clinic_address, clinic_contact, clinic_registration_no, clinic_description

class RegisterFounder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.register_founder = Frame(self, background="white")
        self.register_founder.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.register_founder, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = Label(self.register_founder, text="Clinic's Founder Information", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=310, y=160)

        self.foundername_label = Label(self.register_founder, text="Founder full name", font=(25), background="white")
        self.foundername_label.place(x=330, y=250)
        self.foundername_label_entry = Entry(self.register_founder)
        self.foundername_label_entry.place(height=30, width=350, x=330, y=275)

        self.foundercontact_label = Label(self.register_founder, text="Founder contact", font=(25), background="white")
        self.foundercontact_label.place(x=330, y=350)
        self.foundercontact_label_entry = Entry(self.register_founder)
        self.foundercontact_label_entry.place(height=30, width=350, x=330, y=375)

        self.founderemail_label = Label(self.register_founder, text="Founder email address", font=(25), background="white")
        self.founderemail_label.place(x=330, y=450)
        self.founderemail_label_entry = Entry(self.register_founder)
        self.founderemail_label_entry.place(height=30, width=350, x=330, y=475)

        nxtTOsignup_btn = Button(self.register_founder, text = "Next",background="thistle",command=lambda: controller.show_frame(ClinicAccount))
        nxtTOsignup_btn.place(height=30, width=100,x=450, y=570)

    def get_clinic_founder(self):
        founder_name = self.foundername_label_entry.get()
        founder_contact = self.foundercontact_label_entry.get()
        founder_email = self.founderemail_label_entry.get()
        return founder_name, founder_contact, founder_email

class ClinicAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.clinic_account = Frame(self, background="white")
        self.clinic_account.place(height=700, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 200, 160
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.clinic_account, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=400, y=0)

        heading_label = Label(self.clinic_account, text="Clinic Sign Up", font=("Helvetica", 22, "bold"), background="white")
        heading_label.place(x=416, y=145)

        self.clnregusername_label = Label(self.clinic_account, text="Username", font=(25), background="white")
        self.clnregusername_label.place(x=330, y=250)
        self.clnregusername_label_entry = Entry(self.clinic_account)
        self.clnregusername_label_entry.place(height=30, width=350, x=330, y=275)

        self.clnregpassword_label = Label(self.clinic_account, text="Password", font=(25), background="white")
        self.clnregpassword_label.place(x=330, y=350)
        self.clnloginpassword_label_entry = Entry(self.clinic_account)
        self.clnloginpassword_label_entry.place(height=30, width=350, x=330, y=375)

        clinicsignup_btn = Button(self.clinic_account, text="Send request to Call A Doctor", background="thistle",
                                  command=self.submit_clinic_registration)
        clinicsignup_btn.place(height=30, width=250, x=380, y=470)

    def submit_clinic_registration(self):
        clinic_information = self.controller.frames[RegisterClinic].get_clinic_information()
        clinic_founder = self.controller.frames[RegisterFounder].get_clinic_founder()
        clinic_username = self.clnregusername_label_entry.get()
        clinic_password = self.clnloginpassword_label_entry.get()

        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ClinicInformation (
                clinic_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                clinic_name TEXT NOT NULL,
                clinic_operation_time TEXT NOT NULL,
                clinic_coordinates TEXT NOT NULL,
                clinic_address TEXT NOT NULL,
                clinic_contact INT NOT NULL,
                clinic_registration_no INT NOT NULL,
                clinic_description TEXT NOT NULL,
                founder_name TEXT NOT NULL,
                founder_contact INT NOT NULL,
                founder_email TEXT NOT NULL,
                clinic_username TEXT NOT NULL,
                clinic_password TEXT NOT NULL,
                status INT NOT NULL          
            )
        ''')

        cursor.execute('''
            INSERT INTO ClinicInformation (clinic_name, clinic_operation_time, clinic_coordinates,
                                        clinic_address, clinic_contact, clinic_registration_no,
                                        clinic_description, founder_name, founder_contact,
                                        founder_email, clinic_username, clinic_password, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (clinic_information[0], clinic_information[1], clinic_information[2], clinic_information[3],
            clinic_information[4], clinic_information[5], clinic_information[6], clinic_founder[0],
            clinic_founder[1], clinic_founder[2], clinic_username, clinic_password, 0))
        
        self.controller.clinic_id = cursor.lastrowid
        messagebox.showinfo("Success", "Clinic registration successful")

        conn.commit()
        conn.close()

        self.controller.show_frame(ClinicPending)

class ClinicPending(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.clinic_pending = Frame(self, background="white")
        self.clinic_pending.place(height=700, width=1000, x=0, y=0)

        
        self.topframe = Frame(self.clinic_pending, background="cornsilk")
        self.topframe.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 50, 50
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS for resizing
        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.topframe, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=25, y=25)

        self.topframe_label = Label(self.topframe, text="Clinic Pending", font=("Helvetica", 25, "bold"), background="cornsilk")
        self.topframe_label.place(x=130, y=20)

        self.centerframe = Frame(self.clinic_pending, background="white", bd=12, relief=RIDGE)
        self.centerframe.place(height=610, width=1000, x=0, y=90)

        self.innercenterframe = Frame(self.centerframe, background="thistle")
        self.innercenterframe.place(height=540, width=930, x=30, y=30)

        self.clinicLogout_btn = Button(self.topframe, text="Logout", background="thistle", command=lambda: controller.show_frame(LoginClinic))
        self.clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.pending_label = Label(self.innercenterframe, text="Please wait. Your account is being processed.", font=(15), background="cornsilk")
        self.pending_label.place(height=70,width=480, x=200, y=300) 

    def display_status(self):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        clinic_id = self.clinic_id
        cursor.execute("SELECT status, clinic_name FROM ClinicInformation WHERE clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()

        status = rows[0][0]
        status = int(status)
        if status == 0:
            status = "Pending"
        clinic_name = rows[0][1]
        clinicname = tk.Label(self.innercenterframe, text="Dear " + str(clinic_name), font=(15), background="cornsilk")
        clinicname.place(height=70,width=480, x=200, y=100)
        
        status = tk.Label(self.innercenterframe, text="Account Status: " + str(status), font=(15), background="cornsilk")
        status.place(height=70,width=480, x=200, y=200)

        conn.commit()
        conn.close()

class ClinicDecline(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.clinic_decline = Frame(self, background="white")
        self.clinic_decline.place(height=700, width=1000, x=0, y=0)

        self.topframe = Frame(self.clinic_decline, background="cornsilk")
        self.topframe.place(height=90, width=1000, x=0, y=0)

        self.topframe_label = Label(self.topframe, text="Clinic Decline", font=("Helvetica", 25, "bold"), background="cornsilk")
        self.topframe_label.place(x=130, y=20)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 50, 50
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS for resizing
        # Create a PhotoImage from the resized image
        image = ImageTk.PhotoImage(image)

        label = Label(self.topframe, image=image)
        label.image = image  # Keep a reference to the image to prevent garbage collection
        label.place(height=label_height, width=label_width, x=25, y=25)

        self.topframe_label = Label(self.topframe, text="Clinic Pending", font=("Helvetica", 25, "bold"), background="cornsilk")
        self.topframe_label.place(x=130, y=20)

        self.centerframe = Frame(self.clinic_decline, background="white", bd=12, relief=RIDGE)
        self.centerframe.place(height=610, width=1000, x=0, y=90)

        self.innercenterframe = Frame(self.centerframe, background="thistle")
        self.innercenterframe.place(height=540, width=930, x=30, y=30)

        self.clinicLogout_btn = Button(self.topframe, text="Logout", background="thistle", command=lambda: controller.show_frame(LoginClinic))
        self.clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.decline_label = Label(self.innercenterframe, text="Sorry, Your request has been decline", font=(15), background="thistle")
        self.decline_label.place(height=70,width=480, x=200, y=280) 
    
    def display_status(self):
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        clinic_id = self.clinic_id
        cursor.execute("SELECT status, clinic_name, reason FROM ClinicInformation WHERE clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()

        status = rows[0][0]
        status = int(status)
        if status == 2:
            status = "Decline"
        clinic_name = rows[0][1]
        reason = rows[0][2]
        clinicname = tk.Label(self.innercenterframe, text="Dear " + str(clinic_name), font=(15), background="cornsilk")
        clinicname.place(height=70, width=480, x=200, y=50)
        
        status = tk.Label(self.innercenterframe, text=" Account Status: " + str(status), font=(15), background="cornsilk")
        status.place(height=70, width=480, x=200, y=120)

        self.decline_reason = Label(self.innercenterframe, text="Reason: " + str(reason), font=(15), background="cornsilk",anchor="center",wraplength=300)
        self.decline_reason.place(height=100, width=480, x=200, y=190)

        conn.commit()
        conn.close()

class ClinicHomepage(LoginClinic, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.clinic_homepage = tk.Frame(self, background="white")
        self.clinic_homepage.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = tk.Frame(self.clinic_homepage, background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(self.clinic_homepage, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = tk.Label(self.clinic_homepage, text="Clinic Home", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicLogout_btn = tk.Button(self.clinic_homepage, text="Logout", background="thistle", command=lambda: controller.show_frame(LoginClinic))
        clinicLogout_btn.place(height=30, width=60, x=910, y=25)

        self.clinicleft_frame = tk.Frame(self.clinic_homepage, background="cornsilk")
        self.clinicleft_frame.place(height=530, width=320, x=40, y=130)

        viewDoctor_btn = tk.Button(self.clinic_homepage, text=" Doctor List ", font=(20), background="white", command=lambda: controller.show_frame(DoctorList))
        viewDoctor_btn.place(height=70, width=200, x=100, y=200)

        uploadDoctor_btn = tk.Button(self.clinic_homepage, text=" Upload Doctor ", font=(20), background="white", command=lambda: controller.show_frame(UploadDoctor))
        uploadDoctor_btn.place(height=70, width=200, x=100, y=350)

        manageDoctor_btn = tk.Button(self.clinic_homepage, text=" Manage Doctor ", font=(20), background="white", command=lambda: controller.show_frame(ManageDoctor))
        manageDoctor_btn.place(height=70, width=200, x=100, y=500)

        self.clinicright_frame = tk.Frame(self.clinic_homepage, background="cornsilk")
        self.clinicright_frame.place(height=530, width=540, x=410, y=130)

        self.patient_label = tk.Label(self.clinic_homepage, text="Patient", font=(25), background="white")
        self.patient_label.place(height=70, width=480, x=440, y=160)

class DoctorList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.doctor_list = Frame(self, background="white")
        self.doctor_list.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.doctor_list , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.doctor_list, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.doctor_list, text="Doctor List", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.doctor_list, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

class UploadDoctor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.upload_doctor = Frame(self, background="white")
        self.upload_doctor.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.upload_doctor , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.upload_doctor, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.upload_doctor, text="Uplaod Doctor", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.upload_doctor, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        self.clinicmain_frame = Frame(self.upload_doctor , background="cornsilk")
        self.clinicmain_frame.place(height=530, width=915, x=40, y=130)

        mainframe_label = Label(self.upload_doctor, text="Doctor Information", font=("Helvetica", 25, "bold"), background="cornsilk", fg="mediumpurple")
        mainframe_label.place(x=370, y=150)

        self.doctorname_label = Label(self.upload_doctor, text="Full name :", font=(28), background="cornsilk")
        self.doctorname_label.place(x=100, y=220)
        self.doctorname_label_entry = Entry(self.upload_doctor)
        self.doctorname_label_entry.place(height=30, width=590, x=290, y=220)

        self.doctorqualification_label = Label(self.upload_doctor, text="Qualification :", font=(28), background="cornsilk")
        self.doctorqualification_label.place(x=100, y=275)
        self.doctorqualification_label_entry = Entry(self.upload_doctor)
        self.doctorqualification_label_entry.place(height=30, width=590, x=290, y=275)

        self.doctorregno_label = Label(self.upload_doctor, text="Registration number :", font=(28), background="cornsilk")
        self.doctorregno_label.place(x=100, y=330)
        self.doctorregno_label_entry = Entry(self.upload_doctor)
        self.doctorregno_label_entry.place(height=30, width=590, x=290, y=330)

        self.doctorcontact_label = Label(self.upload_doctor, text="Contact number :", font=(28), background="cornsilk")
        self.doctorcontact_label.place(x=100, y=385)
        self.doctorcontact_label_entry = Entry(self.upload_doctor)
        self.doctorcontact_label_entry.place(height=30, width=590, x=290, y=385)

        self.doctoremail_label = Label(self.upload_doctor, text="Email :", font=(28), background="cornsilk")
        self.doctoremail_label.place(x=100, y=440)
        self.doctoremail_label_entry = Entry(self.upload_doctor)
        self.doctoremail_label_entry.place(height=30, width=590, x=290, y=440)

        self.doctorusername_label = Label(self.upload_doctor, text="Username :", font=(28), background="cornsilk")
        self.doctorusername_label.place(x=100, y=495)
        self.doctorusername_label_entry = Entry(self.upload_doctor)
        self.doctorusername_label_entry.place(height=30, width=590, x=290, y=495)

        self.doctorpassword_label = Label(self.upload_doctor, text="Password :", font=(28), background="cornsilk")
        self.doctorpassword_label.place(x=100, y=550)
        self.doctorpassword_label_entry = Entry(self.upload_doctor)
        self.doctorpassword_label_entry.place(height=30, width=590, x=290, y=550)

        clinicupload_btn = Button(self.upload_doctor, text = " Upload",background="thistle",
                                  command=self.submit_doctor_registration)
        clinicupload_btn.place(height=30, width=90, x=485, y=610)

    def submit_doctor_registration(self):
        doctor_name = self.doctorname_label_entry.get()
        doctor_qualification = self.doctorqualification_label_entry.get()
        doctor_registration_no = self.doctorregno_label_entry.get()
        doctor_contact = self.doctorcontact_label_entry.get()
        doctor_email = self.doctoremail_label_entry.get()
        doctor_username = self.doctorusername_label_entry.get()
        doctor_password = self.doctorpassword_label_entry.get()
        clinic_id = self.controller.clinic_id

        dbpath = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS DoctorInformation (
                             doctor_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                             doctor_name TEXT NOT NULL,
                             doctor_qualification TEXT NOT NULL,
                             doctor_registration_no INT NOT NULL,
                             doctor_contact INT NOT NULL,
                             doctor_email TEXT NOT NULL,
                             doctor_username TEXT NOT NULL,
                             doctor_password TEXT NOT NULL,
                             clinic_id INT FOREIGNKEY REFERENCES ClinicInformation(clinic_id),
                             status INT NOT NULL
                        )
                    ''')
            
        cursor.execute('''
                        INSERT INTO DoctorInformation (doctor_name, doctor_qualification, 
                                                        doctor_registration_no, doctor_contact, 
                                                        doctor_email, doctor_username, doctor_password, 
                                                        clinic_id, status)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                       , (doctor_name, doctor_qualification, doctor_registration_no, 
                          doctor_contact, doctor_email, doctor_username, doctor_password, clinic_id , 0))
        
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Doctor uploaded successfully")
        self.controller.show_frame(ClinicHomepage)
        self.controller.clinic_id = clinic_id
        
class ManageDoctor(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global doctor_details_tree
        self.doctor_details_tree = None
        self.clinic_id = None

        self.manage_doctor = Frame(self, background="white")
        self.manage_doctor.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.manage_doctor , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        image = Image.open("C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_logo.jpg")
        label_width, label_height = 112, 92
        image = image.resize((label_width, label_height), Image.Resampling.LANCZOS)  
        image = ImageTk.PhotoImage(image)
        label = Label(self.manage_doctor, image=image)
        label.image = image
        label.place(height=label_height, width=label_width, x=0, y=0)

        heading_label = Label(self.manage_doctor, text="Manage Doctor", font=("Helvetica", 25, "bold"), background="cornsilk")
        heading_label.place(x=130, y=20)

        clinicbackTOHome_btn = Button(self.manage_doctor, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        clinicbackTOHome_btn.place(height=30, width=110, x=865, y=25)

        dataframe = Frame(self.manage_doctor, bd=12, relief=RIDGE, background="cornsilk")
        dataframe.place(height=560, width=930, x=30, y=110)

        ####################################### Dataframe #########################################
        dataframeheading = LabelFrame(dataframe, bd=7, padx=20, relief=RIDGE, font=("Helvetica", 12, "bold"), text="Doctor Information", background="cornsilk")
        dataframeheading.place(height=245, width=885, x=10, y=7)

        self.doctorname_label = Label(dataframeheading, text="Doctor Full Name: ", font=(12), background="cornsilk", pady=9)
        self.doctorname_label.grid(row=0, column=0, sticky=W)
        self.doctorname_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorname_label_entry.grid(row=0, column=1, sticky=W)

        self.doctorqualification_label = Label(dataframeheading, text="Qualification: ", font=(12), background="cornsilk", pady=9)
        self.doctorqualification_label.grid(row=1, column=0, sticky=W)
        self.doctorqualification_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorqualification_label_entry.grid(row=1, column=1, sticky=W)

        self.doctorregno_label = Label(dataframeheading, text="Registration nummber:             ", font=(12), background="cornsilk", pady=9)
        self.doctorregno_label.grid(row=2, column=0, sticky=W)
        self.doctorregno_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorregno_label_entry.grid(row=2, column=1, sticky=W)

        self.doctorcontactno_label = Label(dataframeheading, text="Contact number: ", font=(12), background="cornsilk", pady=9)
        self.doctorcontactno_label.grid(row=3, column=0, sticky=W)
        self.doctorcontactno_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctorcontactno_label_entry.grid(row=3, column=1, sticky=W)
        
        self.doctoremail_label = Label(dataframeheading, text="Email Address: ", font=(12), background="cornsilk", pady=9)
        self.doctoremail_label.grid(row=4, column=0, sticky=W)
        self.doctoremail_label_entry = Entry(dataframeheading, font=(10), width=67)
        self.doctoremail_label_entry.grid(row=4, column=1, sticky=W)
        
        ########################################## Buttonframe ######################################
        buttonframe = Frame(dataframe, bd=7, relief=RIDGE, background="cornsilk")
        buttonframe.place(height=40, width=885, x=10, y=269)

        update_btn = Button(buttonframe, text="Update", background="thistle", width=47, font=("Helvetica", 11, "bold"))
        update_btn.grid(column=0, row=0)

        delete_btn = Button(buttonframe, text="Delete", background="thistle", width=48, font=("Helvetica", 11, "bold"))
        delete_btn.grid(column=1, row=0)

        ########################################## Detailsframe ######################################
        delailsframe = Frame(dataframe, bd=7, relief=RIDGE, background="cornsilk")
        delailsframe.place(height=198, width=885, x=10, y=325)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", bg="#D3D3D3", fg="black", rowheight=15, fieldbackground="#F8F8F8")
        style.map("Treeview", bg=[('selected', "#F9ECE4")])

        doctordetailsframe = Frame(delailsframe)
        doctordetailsframe.place(x=8,y=5)
        treescroll = Scrollbar(doctordetailsframe)
        treescroll.pack(side=RIGHT, fill=Y)

        self.doctor_details_tree = ttk.Treeview(doctordetailsframe, yscrollcommand=treescroll.set, selectmode="extended")
        self.doctor_details_tree.pack()
        treescroll.config(command=self.doctor_details_tree.yview)

        self.doctor_details_tree['column'] = ('1', '2', '3', '4')
        self.doctor_details_tree['show'] = 'headings'

        self.doctor_details_tree.column('1', width=40, anchor='c')
        self.doctor_details_tree.column('2', width=265, anchor='c')
        self.doctor_details_tree.column('3', width=330, anchor='c')
        self.doctor_details_tree.column('4', width=205, anchor='c')

        self.doctor_details_tree.heading('1', text='ID')
        self.doctor_details_tree.heading('2', text='Full Name')
        self.doctor_details_tree.heading('3', text='Qualification')
        self.doctor_details_tree.heading('4', text='Registration Number')
    
        self.doctor_details_tree.tag_configure('odd', background="cornsilk")
        self.doctor_details_tree.tag_configure('even', background="cornsilk") 

        self.showdoctordetails()

        self.doctor_details_tree.bind('<ButtonRelease-1>', self.selectdoctor)


    def showdoctordetails(self):
        clinic_id = self.clinic_id
        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT doctor_id, doctor_name, doctor_qualification, doctor_registration_no FROM DoctorInformation WHERE clinic_id = ?", (clinic_id,))
        rows = cursor.fetchall()
        self.doctor_details_tree.delete(*self.doctor_details_tree.get_children())
        for row in rows:
            if row[0] % 2 == 0:
                self.doctor_details_tree.insert("", tk.END, values=row, tags=('even',))
            else:
                self.doctor_details_tree.insert("", tk.END, values=row, tags=('odd',))
        conn.commit()
        conn.close()

    def selectdoctor(self, event):
        item = self.doctor_details_tree.selection()[0]
        doctor_id = self.doctor_details_tree.item(item, "values")[0]

        db_path = "C:/Users/choon/Documents/Chi Ling/BCSCUN/Software Engineering/CAD_Database.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT doctor_name, doctor_qualification, doctor_registration_no, doctor_contact, doctor_email FROM DoctorInformation WHERE doctor_id = ?", (doctor_id,))
        row = cursor.fetchone()

        if row is not None:
            self.doctorname_label_entry.delete(0, END)
            self.doctorname_label_entry.insert(0, row[0])
            self.doctorqualification_label_entry.delete(0, END)
            self.doctorqualification_label_entry.insert(0, row[1])
            self.doctorregno_label_entry.delete(0, END)
            self.doctorregno_label_entry.insert(0, row[2])
            self.doctorcontactno_label_entry.delete(0, END)
            self.doctorcontactno_label_entry.insert(0, row[3])
            self.doctoremail_label_entry.delete(0, END)
            self.doctoremail_label_entry.insert(0, row[4])

        conn.close()

class PatientRequest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.patient_request = Frame(self, background="white")
        self.patient_request.place(height=700, width=1000, x=0, y=0)

        self.clinictop_frame = Frame(self.patient_request , background="cornsilk")
        self.clinictop_frame.place(height=90, width=1000, x=0, y=0)

        self.backTOHome_btn = Button(self.patient_request, text = " Back to homepage",background="thistle",command=lambda: controller.show_frame(ClinicHomepage))
        self.backTOHome_btn.place(height=30, width=110, x=865, y=25)

        self 

if __name__ == "__main__":
    app = Application()
    app.geometry('1000x700+100+0')
    app.resizable(True, True)
    app.title('Call A Doctor')
    app.mainloop()